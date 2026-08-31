"""
KNN-Based Smart Nutritional Recommender Subsystem.
Supports Dish-to-Dish and Target-to-Dish Hybrid Recommendations.
"""

from typing import Any, Dict, List, Optional, Union
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

from ..preprocessing.data_processor import NUMERICAL_FEATURES, NAME_MAP


class KNNRecommender:
    def __init__(self, metric: str = 'euclidean'):
        self.metric = metric
        self.scaler: Optional[StandardScaler] = None
        self.knn_model: Optional[NearestNeighbors] = None
        self.df: Optional[pd.DataFrame] = None
        self.scaled_features: Optional[np.ndarray] = None
        self.features: List[str] = NUMERICAL_FEATURES

    def fit(self, df: pd.DataFrame, features: Optional[List[str]] = None) -> "KNNRecommender":
        """
        Fit the StandardScaler and NearestNeighbors model on feature matrix.
        """
        self.df = df.copy().reset_index(drop=True)
        if features:
            self.features = features
        else:
            self.features = [f for f in NUMERICAL_FEATURES if f in self.df.columns]

        self.scaler = StandardScaler()
        self.scaled_features = self.scaler.fit_transform(self.df[self.features])

        self.knn_model = NearestNeighbors(
            n_neighbors=min(25, len(self.df)),
            metric=self.metric,
            algorithm='auto'
        )
        self.knn_model.fit(self.scaled_features)
        return self

    def find_dish_index(self, query: str) -> Optional[int]:
        """
        Find row index for a dish name using exact or case-insensitive matching.
        """
        if self.df is None or 'Dish Name' not in self.df.columns:
            return None

        clean_query = query.strip().lower()
        exact_matches = self.df[self.df['Dish Name'].str.lower() == clean_query]
        if not exact_matches.empty:
            return exact_matches.index[0]

        contains_matches = self.df[self.df['Dish Name'].str.lower().str.contains(clean_query, regex=False)]
        if not contains_matches.empty:
            return contains_matches.index[0]

        return None

    def recommend_dish(self, dish_name: str, top_k: int = 5) -> Dict[str, Any]:
        """
        Recommend dishes similar to a target dish name.
        """
        if self.knn_model is None or self.df is None or self.scaled_features is None:
            raise ValueError("Recommender model has not been fitted.")

        idx = self.find_dish_index(dish_name)
        if idx is None:
            return {
                "success": False,
                "error": f"Dish '{dish_name}' not found in database.",
                "query": dish_name,
                "recommendations": []
            }

        target_row = self.df.iloc[idx]
        input_vector = self.scaled_features[idx].reshape(1, -1)

        # Retrieve top_k + 1 to exclude self
        k_retrieve = min(top_k + 1, len(self.df))
        distances, indices = self.knn_model.kneighbors(input_vector, n_neighbors=k_retrieve)

        recs = []
        for d, i in zip(distances[0], indices[0]):
            if i == idx and len(recs) < top_k:
                continue
            cand = self.df.iloc[i]
            match_pct = 100.0 / (1.0 + float(d))
            recs.append(self._format_dish_record(cand, match_pct=match_pct, distance=float(d)))
            if len(recs) >= top_k:
                break

        return {
            "success": True,
            "query": dish_name,
            "mode": "dish-to-dish",
            "target_dish": self._format_dish_record(target_row),
            "count": len(recs),
            "recommendations": recs
        }

    def recommend_target(self, target_nutrients: Dict[str, float], top_k: int = 5) -> Dict[str, Any]:
        """
        Recommend dishes matching a target nutritional profile.
        """
        if self.knn_model is None or self.df is None or self.scaler is None:
            raise ValueError("Recommender model has not been fitted.")

        # Construct base vector with population mean
        base_vector = self.df[self.features].mean().values.copy()
        col_map = {col: i for i, col in enumerate(self.features)}

        # Update base vector with user targets
        mapped_target = {}
        for key, val in target_nutrients.items():
            if key == 'k' or key == 'top_k':
                continue
            target_col = NAME_MAP.get(key, key)
            if target_col in col_map:
                base_vector[col_map[target_col]] = float(val)
                mapped_target[target_col] = float(val)

        input_df = pd.DataFrame([base_vector], columns=self.features)
        input_vector = self.scaler.transform(input_df)

        k_retrieve = min(top_k, len(self.df))
        distances, indices = self.knn_model.kneighbors(input_vector, n_neighbors=k_retrieve)

        recs = []
        for d, i in zip(distances[0], indices[0]):
            cand = self.df.iloc[i]
            match_pct = 100.0 / (1.0 + float(d))
            recs.append(self._format_dish_record(cand, match_pct=match_pct, distance=float(d)))

        return {
            "success": True,
            "query": target_nutrients,
            "mode": "target-to-dish",
            "target_profile": mapped_target,
            "count": len(recs),
            "recommendations": recs
        }

    def _format_dish_record(self, row: pd.Series, match_pct: Optional[float] = None, distance: Optional[float] = None) -> Dict[str, Any]:
        """
        Format a DataFrame row into a clean dictionary.
        """
        record: Dict[str, Any] = {
            "id": int(row.name) if isinstance(row.name, (int, np.integer)) else 0,
            "name": str(row.get('Dish Name', 'Unknown')),
            "category": str(row.get('Category', 'Balanced Meal')),
            "grade": str(row.get('Grade', 'B (Moderate)')),
            "health_score": round(float(row.get('Health_Score', 0.0)), 2),
            "calories": round(float(row.get('Calories (kcal)', 0.0)), 1),
            "protein": round(float(row.get('Protein (g)', 0.0)), 1),
            "carbs": round(float(row.get('Carbohydrates (g)', 0.0)), 1),
            "fats": round(float(row.get('Fats (g)', 0.0)), 1),
            "sugar": round(float(row.get('Free Sugar (g)', 0.0)), 1),
            "fibre": round(float(row.get('Fibre (g)', 0.0)), 1),
            "sodium": round(float(row.get('Sodium (mg)', 0.0)), 1),
            "calcium": round(float(row.get('Calcium (mg)', 0.0)), 1),
            "iron": round(float(row.get('Iron (mg)', 0.0)), 1),
            "vitamin_c": round(float(row.get('Vitamin C (mg)', 0.0)), 2),
            "folate": round(float(row.get('Folate (µg)', 0.0)), 1),
            "tags": {
                "high_protein": bool(row.get('High_Protein', 0) == 1),
                "low_carb": bool(row.get('Low_Carb', 0) == 1),
                "low_calorie": bool(row.get('Low_Calorie', 0) == 1)
            }
        }
        if match_pct is not None:
            record["match_pct"] = round(match_pct, 1)
        if distance is not None:
            record["distance"] = round(distance, 4)
        return record
