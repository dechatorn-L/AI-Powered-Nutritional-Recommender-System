"""
Random Forest Classification Subsystem for Nutri-Grade AI
with Atwater Factor Caloric Consistency Checking.
"""

from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from ..preprocessing.data_processor import CLASSIFICATION_FEATURES, NAME_MAP


class NutriGradeClassifier:
    def __init__(self, n_estimators: int = 100, random_state: int = 42):
        self.n_estimators = n_estimators
        self.random_state = random_state
        self.model: Optional[RandomForestClassifier] = None
        self.features: List[str] = CLASSIFICATION_FEATURES
        self.classes: List[str] = ['A (Healthy)', 'B (Moderate)', 'C (Limit)']
        self.feature_means: Dict[str, float] = {}
        self.train_test_data: Optional[Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]] = None

    def fit(self, df: pd.DataFrame, test_size: float = 0.2) -> "NutriGradeClassifier":
        """
        Train Random Forest model using Stratified Train-Test split.
        """
        if 'Grade' not in df.columns:
            raise ValueError("Dataset must contain 'Grade' column for classification.")

        # Cache empirical feature means for consistency checks
        for feat in self.features:
            self.feature_means[feat] = float(df[feat].mean()) if feat in df.columns else 0.0

        X = df[self.features]
        y = df['Grade']

        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=test_size,
            random_state=self.random_state,
            stratify=y
        )
        self.train_test_data = (X_train, X_test, y_train, y_test)

        self.model = RandomForestClassifier(
            n_estimators=self.n_estimators,
            random_state=self.random_state
        )
        self.model.fit(X_train, y_train)
        self.classes = list(self.model.classes_)
        return self

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
        Predict Nutri-Grade with automatic Atwater energy consistency check.
        """
        if self.model is None:
            raise ValueError("Classifier model has not been trained.")

        warnings = []
        atwater_used = False

        # Fill missing macronutrients with empirical population averages
        p_val = float(protein) if protein is not None else self.feature_means.get('Protein (g)', 10.0)
        c_val = float(carb) if carb is not None else self.feature_means.get('Carbohydrates (g)', 20.0)
        f_val = float(fiber) if fiber is not None else self.feature_means.get('Fibre (g)', 3.0)

        # Caloric Consistency Calculation via Atwater Factors
        if calories is None:
            # 1g Fat = 9 kcal, 1g Protein = 4 kcal, 1g Carb = 4 kcal
            cal_val = (fat * 9.0) + (p_val * 4.0) + (c_val * 4.0)
            atwater_used = True
        else:
            cal_val = float(calories)
            theoretical_cal = (fat * 9.0) + (p_val * 4.0) + (c_val * 4.0)
            if abs(cal_val - theoretical_cal) > 200.0:
                warnings.append(
                    f"Calorie input ({cal_val} kcal) deviates noticeably from macronutrient total (~{theoretical_cal:.0f} kcal)."
                )

        input_row = {
            'Calories (kcal)': cal_val,
            'Carbohydrates (g)': c_val,
            'Protein (g)': p_val,
            'Fats (g)': float(fat),
            'Free Sugar (g)': float(sugar),
            'Fibre (g)': f_val,
            'Sodium (mg)': float(sodium)
        }

        input_df = pd.DataFrame([input_row])[self.features]

        predicted_grade = self.model.predict(input_df)[0]
        probabilities = self.model.predict_proba(input_df)[0]

        prob_dict = {cls_name: round(float(prob), 4) for cls_name, prob in zip(self.classes, probabilities)}
        max_prob = max(prob_dict.values())

        return {
            "success": True,
            "grade": predicted_grade,
            "confidence": round(float(max_prob), 4),
            "estimated_calories": round(cal_val, 1),
            "atwater_used": atwater_used,
            "probabilities": prob_dict,
            "inputs": {
                "sugar_g": float(sugar),
                "fat_g": float(fat),
                "sodium_mg": float(sodium),
                "protein_g": round(p_val, 1),
                "carb_g": round(c_val, 1),
                "fiber_g": round(f_val, 1),
                "calories_kcal": round(cal_val, 1)
            },
            "warnings": warnings
        }

    def get_feature_importances(self) -> List[Dict[str, Any]]:
        """
        Get feature importances sorted in descending order.
        """
        if self.model is None:
            raise ValueError("Classifier model has not been trained.")

        importances = self.model.feature_importances_
        results = []
        for feat, imp in zip(self.features, importances):
            results.append({
                "feature": feat,
                "importance": round(float(imp), 4),
                "importance_pct": round(float(imp) * 100.0, 2)
            })
        return sorted(results, key=lambda x: x['importance'], reverse=True)
