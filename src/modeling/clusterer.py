"""
K-Means Clustering and 2D PCA Dimensionality Reduction
for Food Profiling and Spatial Visualization.
"""

from typing import Any, Dict, List, Optional, Tuple
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from ..preprocessing.data_processor import NUMERICAL_FEATURES

CLUSTER_COLOR_MAP: Dict[str, str] = {
    "🍭 Sweet/Dessert": "#ec4899",
    "🧀 Rich/High Fat": "#f59e0b",
    "💪 High Protein": "#10b981",
    "🥗 Light/Snack": "#06b6d4",
    "🍛 Balanced Meal": "#8b5cf6"
}


class NutritionClusterer:
    def __init__(self, n_clusters: int = 5, random_state: int = 42):
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.kmeans: Optional[KMeans] = None
        self.scaler: Optional[StandardScaler] = None
        self.pca: Optional[PCA] = None
        self.cluster_names: Dict[int, str] = {}
        self.df: Optional[pd.DataFrame] = None
        self.pca_coordinates: Optional[np.ndarray] = None
        self.centroid_pca: Optional[np.ndarray] = None

    def fit_predict(self, df: pd.DataFrame, features: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Fit K-Means and PCA, assigning 'Cluster', 'Category', 'pca_x', 'pca_y' columns to df.
        """
        self.df = df.copy()
        feat_cols = features if features else [f for f in NUMERICAL_FEATURES if f in self.df.columns]

        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(self.df[feat_cols])

        # K-Means Clustering
        self.kmeans = KMeans(n_clusters=self.n_clusters, random_state=self.random_state, n_init=10)
        self.df['Cluster'] = self.kmeans.fit_predict(X_scaled)

        # Profile Naming
        cluster_means = self.df.groupby('Cluster')[feat_cols].mean()
        self.cluster_names = {}
        for i, row in cluster_means.iterrows():
            if row.get('Free Sugar (g)', 0) > 15.0:
                name = "🍭 Sweet/Dessert"
            elif row.get('Fats (g)', 0) > 20.0:
                name = "🧀 Rich/High Fat"
            elif row.get('Protein (g)', 0) > 15.0:
                name = "💪 High Protein"
            elif row.get('Calories (kcal)', 0) < 150.0:
                name = "🥗 Light/Snack"
            else:
                name = "🍛 Balanced Meal"
            self.cluster_names[int(i)] = name

        self.df['Category'] = self.df['Cluster'].map(self.cluster_names)

        # 2D PCA Dimensionality Reduction
        self.pca = PCA(n_components=2, random_state=self.random_state)
        self.pca_coordinates = self.pca.fit_transform(X_scaled)
        self.df['pca_x'] = np.round(self.pca_coordinates[:, 0], 4)
        self.df['pca_y'] = np.round(self.pca_coordinates[:, 1], 4)

        # Centroid Projections
        if self.kmeans.cluster_centers_ is not None:
            self.centroid_pca = self.pca.transform(self.kmeans.cluster_centers_)

        return self.df

    def get_cluster_summary(self) -> List[Dict[str, Any]]:
        """
        Get aggregated statistical metrics for each cluster.
        """
        if self.df is None or self.kmeans is None:
            raise ValueError("Clusterer has not been fitted.")

        summaries = []
        cluster_counts = self.df['Cluster'].value_counts().to_dict()

        for c_id, c_name in self.cluster_names.items():
            sub = self.df[self.df['Cluster'] == c_id]
            centroid_x = float(self.centroid_pca[c_id, 0]) if self.centroid_pca is not None else 0.0
            centroid_y = float(self.centroid_pca[c_id, 1]) if self.centroid_pca is not None else 0.0

            summaries.append({
                "id": int(c_id),
                "name": c_name,
                "color": CLUSTER_COLOR_MAP.get(c_name, "#6366f1"),
                "count": int(cluster_counts.get(c_id, 0)),
                "centroid": {"x": round(centroid_x, 3), "y": round(centroid_y, 3)},
                "avg_nutrients": {
                    "calories": round(float(sub['Calories (kcal)'].mean()), 1),
                    "protein": round(float(sub['Protein (g)'].mean()), 1),
                    "carbs": round(float(sub['Carbohydrates (g)'].mean()), 1),
                    "fats": round(float(sub['Fats (g)'].mean()), 1),
                    "sugar": round(float(sub['Free Sugar (g)'].mean()), 1),
                    "sodium": round(float(sub['Sodium (mg)'].mean()), 1),
                    "health_score": round(float(sub['Health_Score'].mean()), 2)
                }
            })
        return summaries

    def get_points_for_scatter(self, sample_size: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Get 2D scatter coordinates for all dishes.
        """
        if self.df is None:
            return []

        target_df = self.df if sample_size is None else self.df.sample(min(sample_size, len(self.df)), random_state=42)
        points = []
        for idx, row in target_df.iterrows():
            c_name = str(row.get('Category', 'Balanced Meal'))
            points.append({
                "id": int(idx),
                "name": str(row.get('Dish Name', 'Unknown')),
                "cluster_id": int(row.get('Cluster', 0)),
                "category": c_name,
                "color": CLUSTER_COLOR_MAP.get(c_name, "#6366f1"),
                "x": float(row.get('pca_x', 0.0)),
                "y": float(row.get('pca_y', 0.0)),
                "calories": round(float(row.get('Calories (kcal)', 0.0)), 1),
                "protein": round(float(row.get('Protein (g)', 0.0)), 1),
                "health_score": round(float(row.get('Health_Score', 0.0)), 2),
                "grade": str(row.get('Grade', 'B (Moderate)'))
            })
        return points
