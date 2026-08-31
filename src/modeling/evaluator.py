"""
Model Evaluation, Quantitative Metrics, Confusion Matrix,
and Nutritional Statistical Profiling.
"""

from typing import Any, Dict, List, Optional
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from .classifier import NutriGradeClassifier
from ..preprocessing.data_processor import NUMERICAL_FEATURES


class ModelEvaluator:
    def __init__(self, classifier: NutriGradeClassifier, df: pd.DataFrame):
        self.classifier = classifier
        self.df = df

    def evaluate_classifier(self) -> Dict[str, Any]:
        """
        Evaluate Nutri-Grade classifier on test split.
        """
        if self.classifier.train_test_data is None or self.classifier.model is None:
            raise ValueError("Classifier train/test data is not available.")

        X_train, X_test, y_train, y_test = self.classifier.train_test_data
        y_pred = self.classifier.model.predict(X_test)

        acc = float(accuracy_score(y_test, y_pred))
        report_dict = classification_report(y_test, y_pred, output_dict=True)

        # Standardize labels
        target_labels = ['A (Healthy)', 'B (Moderate)', 'C (Limit)']
        existing_labels = [l for l in target_labels if l in self.classifier.classes]
        cm = confusion_matrix(y_test, y_pred, labels=existing_labels)

        per_class_metrics = {}
        for label in existing_labels:
            if label in report_dict:
                per_class_metrics[label] = {
                    "precision": round(float(report_dict[label]['precision']), 4),
                    "recall": round(float(report_dict[label]['recall']), 4),
                    "f1_score": round(float(report_dict[label]['f1-score']), 4),
                    "support": int(report_dict[label]['support'])
                }

        feature_imp = self.classifier.get_feature_importances()

        return {
            "accuracy": round(acc, 4),
            "macro_f1": round(float(report_dict.get('macro avg', {}).get('f1-score', acc)), 4),
            "weighted_f1": round(float(report_dict.get('weighted avg', {}).get('f1-score', acc)), 4),
            "per_class": per_class_metrics,
            "confusion_matrix": {
                "labels": existing_labels,
                "matrix": cm.tolist()
            },
            "feature_importances": feature_imp,
            "test_sample_count": len(y_test)
        }

    def compute_nutritional_distributions(self) -> Dict[str, Dict[str, float]]:
        """
        Compute statistical distributions (mean, std, min, 25%, 50%, 75%, max) for all nutrients.
        """
        stats: Dict[str, Dict[str, float]] = {}
        for col in NUMERICAL_FEATURES:
            if col in self.df.columns:
                series = self.df[col].dropna()
                stats[col] = {
                    "mean": round(float(series.mean()), 2),
                    "std": round(float(series.std()), 2),
                    "median": round(float(series.median()), 2),
                    "min": round(float(series.min()), 2),
                    "max": round(float(series.max()), 2),
                    "p25": round(float(series.quantile(0.25)), 2),
                    "p75": round(float(series.quantile(0.75)), 2)
                }
        return stats

    def compute_grade_distribution(self) -> Dict[str, Any]:
        """
        Compute proportions of Grade A, B, C across entire dataset.
        """
        if 'Grade' not in self.df.columns:
            return {}

        counts = self.df['Grade'].value_counts()
        total = len(self.df)
        dist = {}
        for grade_name in ['A (Healthy)', 'B (Moderate)', 'C (Limit)']:
            c = int(counts.get(grade_name, 0))
            dist[grade_name] = {
                "count": c,
                "percentage": round((c / total) * 100.0, 1) if total > 0 else 0.0
            }
        return dist
