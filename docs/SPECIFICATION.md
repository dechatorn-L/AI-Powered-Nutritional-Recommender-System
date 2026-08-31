# 📋 System Specification & API Contract

This document provides the technical specification, dataset schemas, mathematical definitions, and complete REST API contracts for the **AI-Powered Nutritional Recommender System**.

---

## 1. Data Schema & Feature Definitions

### 1.1 Nutrition Feature Vectors (11-D Space)

| Feature | Standard Column Name | Unit | DataType | Scaling Strategy |
|---|---|---|---|---|
| Energy | `Calories (kcal)` | kcal | `float64` | StandardScaler |
| Carbohydrates | `Carbohydrates (g)` | g | `float64` | StandardScaler |
| Protein | `Protein (g)` | g | `float64` | StandardScaler |
| Fats | `Fats (g)` | g | `float64` | StandardScaler |
| Free Sugar | `Free Sugar (g)` | g | `float64` | StandardScaler |
| Fibre | `Fibre (g)` | g | `float64` | StandardScaler |
| Sodium | `Sodium (mg)` | mg | `float64` | StandardScaler |
| Calcium | `Calcium (mg)` | mg | `float64` | StandardScaler |
| Iron | `Iron (mg)` | mg | `float64` | StandardScaler |
| Vitamin C | `Vitamin C (mg)` | mg | `float64` | Median Impute + Scaler |
| Folate | `Folate (µg)` | µg | `float64` | Median Impute + Scaler |

### 1.2 Derived Features

- **`Health_Score`**: NRF 5.3 composite value (Float, unbounded; higher is healthier).
- **`Grade`**: Categorical string in `{'A (Healthy)', 'B (Moderate)', 'C (Limit)'}`.
- **`Cluster`**: Integer `[0, 4]`.
- **`Category`**: Profile label string (e.g. `"💪 High Protein"`, `"🍭 Sweet/Dessert"`).
- **`pca_x`, `pca_y`**: 2D Principal Component projections.

---

## 2. REST API Specification

### Base URL
`http://localhost:8000`

---

### 2.1 System Health & Status
- **Endpoint**: `GET /api/status`
- **Response `200 OK`**:
```json
{
  "status": "ready",
  "dataset_count": 1014,
  "clusters_count": 5,
  "model_trained": true,
  "model_accuracy": 0.9803,
  "uptime_seconds": 12.4
}
```

---

### 2.2 List Dishes Catalog
- **Endpoint**: `GET /api/dishes`
- **Query Parameters**:
  - `q` (optional): Filter by name substring.
  - `category` (optional): Filter by cluster category.
  - `grade` (optional): Filter by Nutri-Grade (`A`, `B`, `C`).
  - `limit` (default: 50): Number of results.
- **Response `200 OK`**:
```json
{
  "total": 1014,
  "count": 50,
  "dishes": [
    {
      "id": 0,
      "name": "Hot tea (Garam Chai)",
      "calories": 16.14,
      "carbs": 2.5,
      "protein": 0.6,
      "fats": 0.4,
      "sugar": 2.1,
      "fibre": 0.1,
      "sodium": 8.0,
      "health_score": 12.45,
      "grade": "A (Healthy)",
      "category": "🥗 Light/Snack"
    }
  ]
}
```

---

### 2.3 Dish-to-Dish Recommendation
- **Endpoint**: `GET /api/recommend/dish`
- **Query Parameters**:
  - `name` (required): Name of the dish (e.g. `Butter Chicken`).
  - `k` (optional, default: 5): Number of similar recommendations.
- **Response `200 OK`**:
```json
{
  "query": "Butter Chicken",
  "target_dish": {
    "name": "Butter Chicken",
    "calories": 320.0,
    "protein": 28.5,
    "carbs": 8.2,
    "fats": 19.8,
    "health_score": 24.1,
    "grade": "B (Moderate)",
    "category": "💪 High Protein"
  },
  "recommendations": [
    {
      "id": 42,
      "name": "Chicken Tikka",
      "match_pct": 94.2,
      "distance": 0.061,
      "health_score": 31.5,
      "grade": "A (Healthy)",
      "category": "💪 High Protein",
      "calories": 280.0,
      "protein": 30.2,
      "carbs": 4.1,
      "fats": 12.0,
      "sugar": 1.5,
      "sodium": 280.0
    }
  ]
}
```

---

### 2.4 Target Nutrient Recommendation
- **Endpoint**: `POST /api/recommend/target`
- **Request Body**:
```json
{
  "Calories": 200,
  "Protein": 25,
  "Carbohydrates": 10,
  "Fats": 5,
  "Sodium": 250,
  "k": 5
}
```
- **Response `200 OK`**:
```json
{
  "target": {
    "Calories": 200,
    "Protein": 25,
    "Carbohydrates": 10,
    "Fats": 5,
    "Sodium": 250
  },
  "recommendations": [
    {
      "name": "Tandoori Fish",
      "match_pct": 91.8,
      "health_score": 45.2,
      "grade": "A (Healthy)",
      "category": "💪 High Protein",
      "calories": 195.0,
      "protein": 26.1,
      "carbs": 6.3,
      "fats": 4.8
    }
  ]
}
```

---

### 2.5 Nutri-Grade AI Classification
- **Endpoint**: `POST /api/grade/predict`
- **Request Body**:
```json
{
  "sugar": 2.5,
  "fat": 4.0,
  "sodium": 180.0,
  "protein": 18.0,
  "carb": 8.0
}
```
- **Response `200 OK`**:
```json
{
  "grade": "A (Healthy)",
  "confidence": 0.945,
  "estimated_calories": 140.0,
  "atwater_used": false,
  "probabilities": {
    "A (Healthy)": 0.945,
    "B (Moderate)": 0.052,
    "C (Limit)": 0.003
  },
  "warnings": []
}
```

---

### 2.6 Clusters & 2D PCA Map
- **Endpoint**: `GET /api/clusters`
- **Response `200 OK`**:
```json
{
  "clusters": [
    {
      "id": 0,
      "name": "💪 High Protein",
      "count": 210,
      "color": "#10b981",
      "centroid": {"x": 1.45, "y": -0.82},
      "avg_nutrients": {"Protein": 22.4, "Calories": 280.1}
    }
  ],
  "points": [
    {
      "name": "Butter Chicken",
      "cluster_id": 0,
      "x": 1.32,
      "y": -0.74,
      "health_score": 24.1,
      "grade": "B (Moderate)"
    }
  ]
}
```

---

### 2.7 Model Evaluation & Insights
- **Endpoint**: `GET /api/evaluation`
- **Response `200 OK`**:
```json
{
  "accuracy": 0.965,
  "report": {
    "A (Healthy)": {"precision": 0.97, "recall": 0.95, "f1_score": 0.96, "support": 68},
    "B (Moderate)": {"precision": 0.96, "recall": 0.97, "f1_score": 0.96, "support": 84},
    "C (Limit)": {"precision": 0.98, "recall": 0.97, "f1_score": 0.98, "support": 51}
  },
  "confusion_matrix": {
    "labels": ["A (Healthy)", "B (Moderate)", "C (Limit)"],
    "matrix": [[65, 3, 0], [2, 81, 1], [0, 1, 50]]
  },
  "feature_importances": [
    {"feature": "Free Sugar (g)", "importance": 0.284},
    {"feature": "Sodium (mg)", "importance": 0.261},
    {"feature": "Fats (g)", "importance": 0.235},
    {"feature": "Calories (kcal)", "importance": 0.082}
  ]
}
```
