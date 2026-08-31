"""
Unified Nutrition AI Intelligence Engine (NutritionAIEngine).
Coordinates Data Ingestion, KNN Recommendations, K-Means Clustering,
2D PCA Projections, and Nutri-Grade AI Classification.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Union
import time
import pandas as pd
import numpy as np

from .preprocessing.data_processor import (
    load_and_preprocess_data,
    compute_nrf_score,
    assign_nutri_grade,
    NUMERICAL_FEATURES
)
from .modeling.recommender import KNNRecommender
from .modeling.clusterer import NutritionClusterer
from .modeling.classifier import NutriGradeClassifier
from .modeling.evaluator import ModelEvaluator
from .default_data import DEFAULT_RECIPES_DATA

PROJECT_ROOT = Path(__file__).resolve().parent.parent

POSSIBLE_DATA_PATHS = [
    PROJECT_ROOT / "data" / "processed" / "Indian_Food_Nutrition_Processed.csv",
    PROJECT_ROOT / "Indian_Food_Nutrition_Processed.csv",
    PROJECT_ROOT / "data" / "raw" / "Indian_Food_Nutrition_Raw.csv",
    Path("data/processed/Indian_Food_Nutrition_Processed.csv"),
    Path("Indian_Food_Nutrition_Processed.csv")
]

DEFAULT_DATA_PATH = None
for p in POSSIBLE_DATA_PATHS:
    if p.exists():
        DEFAULT_DATA_PATH = p.resolve()
        break


class NutritionAIEngine:
    def __init__(self, data_path: Optional[Union[str, Path]] = None, n_clusters: int = 5):
        self.data_path = Path(data_path) if data_path else DEFAULT_DATA_PATH
        self.n_clusters = n_clusters
        self.init_time = time.time()

        self.df: Optional[pd.DataFrame] = None
        self.recommender: Optional[KNNRecommender] = None
        self.clusterer: Optional[NutritionClusterer] = None
        self.classifier: Optional[NutriGradeClassifier] = None
        self.evaluator: Optional[ModelEvaluator] = None
        self._evaluation_cache: Optional[Dict[str, Any]] = None

        self._load_and_initialize()

    def _load_and_initialize(self) -> None:
        """
        Load dataset with self-healing fallback and train all ML models.
        """
        try:
            if self.data_path and self.data_path.exists():
                self.df = load_and_preprocess_data(self.data_path)
            else:
                # Self-healing fallback from embedded curated data
                raw_df = pd.DataFrame(DEFAULT_RECIPES_DATA)
                self.df = load_and_preprocess_data_from_df(raw_df)
        except Exception as e:
            raw_df = pd.DataFrame(DEFAULT_RECIPES_DATA)
            self.df = load_and_preprocess_data_from_df(raw_df)

        # 1. Clusterer & 2D PCA Dimensionality Reduction
        self.clusterer = NutritionClusterer(n_clusters=self.n_clusters, random_state=42)
        self.df = self.clusterer.fit_predict(self.df)

        # 2. KNN Recommender Engine
        self.recommender = KNNRecommender(metric='euclidean')
        self.recommender.fit(self.df)

        # 3. Nutri-Grade AI Random Forest Classifier
        self.classifier = NutriGradeClassifier(n_estimators=100, random_state=42)
        self.classifier.fit(self.df)

        # 4. Model Evaluator
        self.evaluator = ModelEvaluator(self.classifier, self.df)

    def recommend_dish(self, dish_name: str, top_k: int = 5) -> Dict[str, Any]:
        """
        Recommend dishes similar to a target dish name.
        """
        if self.recommender is None:
            return {"success": False, "error": "Recommender not initialized"}
        return self.recommender.recommend_dish(dish_name, top_k=top_k)

    def recommend_target(self, target_nutrients: Dict[str, float], top_k: int = 5) -> Dict[str, Any]:
        """
        Recommend dishes matching custom nutrient targets.
        """
        if self.recommender is None:
            return {"success": False, "error": "Recommender not initialized"}
        return self.recommender.recommend_target(target_nutrients, top_k=top_k)

    def predict_grade(
        self,
        sugar: float,
        fat: float,
        sodium: float,
        protein: Optional[float] = None,
        carb: Optional[float] = None,
        fiber: Optional[float] = None,
        calories: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Predict Nutri-Grade (A/B/C) with automatic Atwater factor consistency checking.
        """
        if self.classifier is None:
            return {"success": False, "error": "Classifier not initialized"}
        return self.classifier.predict_grade(
            sugar=sugar,
            fat=fat,
            sodium=sodium,
            protein=protein,
            carb=carb,
            fiber=fiber,
            calories=calories
        )

    def get_dishes(
        self,
        query: Optional[str] = None,
        category: Optional[str] = None,
        grade: Optional[str] = None,
        limit: int = 50,
        offset: int = 0
    ) -> Dict[str, Any]:
        """
        Query and filter the dishes catalog with pagination.
        """
        if self.df is None:
            return {"total": 0, "count": 0, "dishes": []}

        sub = self.df.copy()
        if query:
            sub = sub[sub['Dish Name'].str.lower().str.contains(query.strip().lower(), regex=False)]
        if category:
            sub = sub[sub['Category'] == category]
        if grade:
            sub = sub[sub['Grade'].str.startswith(grade)]

        total_matches = len(sub)
        paged = sub.iloc[offset: offset + limit]

        dishes = []
        for idx, row in paged.iterrows():
            dishes.append({
                "id": int(idx),
                "name": str(row.get('Dish Name', '')),
                "category": str(row.get('Category', '')),
                "grade": str(row.get('Grade', '')),
                "health_score": round(float(row.get('Health_Score', 0.0)), 2),
                "calories": round(float(row.get('Calories (kcal)', 0.0)), 1),
                "protein": round(float(row.get('Protein (g)', 0.0)), 1),
                "carbs": round(float(row.get('Carbohydrates (g)', 0.0)), 1),
                "fats": round(float(row.get('Fats (g)', 0.0)), 1),
                "sugar": round(float(row.get('Free Sugar (g)', 0.0)), 1),
                "sodium": round(float(row.get('Sodium (mg)', 0.0)), 1),
                "tags": {
                    "high_protein": bool(row.get('High_Protein', 0) == 1),
                    "low_carb": bool(row.get('Low_Carb', 0) == 1),
                    "low_calorie": bool(row.get('Low_Calorie', 0) == 1)
                }
            })

        return {
            "total": total_matches,
            "count": len(dishes),
            "offset": offset,
            "limit": limit,
            "dishes": dishes
        }

    def get_dish_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a single dish profile by name.
        """
        if self.df is None or 'Dish Name' not in self.df.columns:
            return None
        matches = self.df[self.df['Dish Name'].str.lower() == name.strip().lower()]
        if matches.empty:
            matches = self.df[self.df['Dish Name'].str.lower().str.contains(name.strip().lower(), regex=False)]
        if matches.empty:
            return None
        row = matches.iloc[0]
        return self.recommender._format_dish_record(row) if self.recommender else None

    def get_clusters_data(self) -> Dict[str, Any]:
        """
        Get cluster summaries, centroids, and 2D scatter coordinates.
        """
        if self.clusterer is None:
            return {"clusters": [], "points": []}
        return {
            "clusters": self.clusterer.get_cluster_summary(),
            "points": self.clusterer.get_points_for_scatter()
        }

    def get_evaluation_metrics(self) -> Dict[str, Any]:
        """
        Get model evaluation report, confusion matrix, and feature importances.
        """
        if self._evaluation_cache is None and self.evaluator is not None:
            self._evaluation_cache = self.evaluator.evaluate_classifier()
        return self._evaluation_cache or {}

    def get_nutritional_distributions(self) -> Dict[str, Any]:
        """
        Get statistical distributions of all nutrients.
        """
        if self.evaluator is None:
            return {}
        return {
            "distributions": self.evaluator.compute_nutritional_distributions(),
            "grades": self.evaluator.compute_grade_distribution()
        }

    def get_system_status(self) -> Dict[str, Any]:
        """
        Get real-time system status and dataset metadata.
        """
        uptime = round(time.time() - self.init_time, 2)
        total_dishes = len(self.df) if self.df is not None else 0
        eval_metrics = self.get_evaluation_metrics()

        return {
            "status": "ready",
            "uptime_seconds": uptime,
            "dataset_count": total_dishes,
            "clusters_count": self.n_clusters,
            "model_trained": bool(self.classifier and self.classifier.model is not None),
            "model_accuracy": eval_metrics.get('accuracy', 0.0),
            "data_source": str(self.data_path) if self.data_path else "embedded_fallback"
        }


def load_and_preprocess_data_from_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Helper function to preprocess a DataFrame in-memory.
    """
    if 'Vitamin C (mg)' in df.columns:
        df['Vitamin C (mg)'] = df['Vitamin C (mg)'].fillna(df['Vitamin C (mg)'].median())
    if 'Folate (µg)' in df.columns:
        df['Folate (µg)'] = df['Folate (µg)'].fillna(df['Folate (µg)'].median())

    for col in NUMERICAL_FEATURES:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0.0)

    df['High_Protein'] = (df['Protein (g)'] > 10.0).astype(int)
    df['Low_Carb'] = (df['Carbohydrates (g)'] < 15.0).astype(int)
    df['Low_Calorie'] = (df['Calories (kcal)'] < 150.0).astype(int)
    df['Health_Score'] = compute_nrf_score(df)
    df['Grade'] = df.apply(assign_nutri_grade, axis=1)
    return df


_GLOBAL_ENGINE: Optional[NutritionAIEngine] = None


def get_engine(data_path: Optional[Union[str, Path]] = None, force_reload: bool = False) -> NutritionAIEngine:
    """
    Singleton accessor for unified NutritionAIEngine instance.
    """
    global _GLOBAL_ENGINE
    if _GLOBAL_ENGINE is None or force_reload:
        _GLOBAL_ENGINE = NutritionAIEngine(data_path=data_path)
    return _GLOBAL_ENGINE
