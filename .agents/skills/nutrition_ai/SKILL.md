---
name: nutrition_ai
description: Search, recommend, cluster, score (NRF 5.3 Index), and classify (Nutri-Grade A/B/C) food nutrition data using Machine Learning (KNN, K-Means, Random Forest) and nutritional science principles.
---

# Nutrition AI Intelligence Skill

This skill provides comprehensive capabilities for querying, analyzing, clustering, recommending, and classifying food dishes based on nutritional composition, NRF 5.3 Health Scores, and Nutri-Grade AI.

## Capabilities

1. **Nutrient-Aware Dish Recommender (KNN Euclidean Distance)**:
   - **Dish-to-Dish Search**: Finds similar dishes based on 11 standardized macro and micronutrients.
   - **Target-to-Dish Matching**: Allows users to specify arbitrary nutritional targets (e.g. Calories=200, Protein=25, Fat=5) and computes top-matching dishes with inverted distance percentage scores.

2. **Scientific Health Scoring (NRF 5.3 Index)**:
   - Calculates Nutrient Rich Foods 5.3 Index comparing % Daily Values of 5 positive nutrients (Protein, Fibre, Vitamin C, Calcium, Iron) against 3 qualifying/negative nutrients (Free Sugar, Fats, Sodium).

3. **Nutri-Grade Classification AI (Random Forest)**:
   - Predicts food grade: `Grade A (Healthy)`, `Grade B (Moderate)`, `Grade C (Limit)`.
   - Built-in Atwater factor calorie consistency checking (`Fat*9 + Protein*4 + Carb*4`) to prevent out-of-distribution hallucinations and confidence drop.

4. **Culinary Nutrition Clustering & 2D PCA**:
   - Unsupervised K-Means clustering ($K=5$) with semantic profile labels (`Sweet/Dessert`, `Rich/High Fat`, `High Protein`, `Light/Snack`, `Balanced Meal`).
   - 2D Principal Component Analysis (PCA) projection for dish coordinates and cluster centroids.

5. **Statistical Distributions & Model Evaluation**:
   - Computes Precision, Recall, F1-scores, Confusion Matrix, and Feature Importances for model interpretability.

---

## Dataset Schema

The primary dataset is stored in `data/processed/Indian_Food_Nutrition_Processed.csv`:

| Column | Unit | Description |
|---|---|---|
| `Dish Name` | text | Name of the dish |
| `Calories (kcal)` | kcal | Energy density per serving |
| `Carbohydrates (g)` | g | Total carbohydrates |
| `Protein (g)` | g | Protein content |
| `Fats (g)` | g | Total lipid/fat content |
| `Free Sugar (g)` | g | Free/added sugars |
| `Fibre (g)` | g | Dietary fiber |
| `Sodium (mg)` | mg | Sodium mineral content |
| `Calcium (mg)` | mg | Calcium mineral content |
| `Iron (mg)` | mg | Iron mineral content |
| `Vitamin C (mg)` | mg | Vitamin C micronutrient |
| `Folate (µg)` | µg | Folate / Folic acid |
| `Health_Score` | float | NRF 5.3 Scientific Health Score |
| `Grade` | text | Ground truth / predicted Nutri-Grade (A/B/C) |
| `Cluster` | int | Cluster ID (0-4) |
| `Category` | text | Human-readable cluster profile name |

---

## Programmatic Usage

### 1. Load Engine via Python SDK

```python
import sys
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path("c:/Projects/GO_ON/AI-Powered-Nutritional-Recommender-System-main")
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.engine import get_engine

# Initialize unified Nutrition AI engine instance
engine = get_engine()
print(f"Loaded {len(engine.df)} dishes with 5 clusters.")
```

### 2. Dish-to-Dish Recommendation

```python
# Recommend dishes similar to Butter Chicken
results = engine.recommend_dish("Butter Chicken", top_k=5)
print(f"Target: {results['target_dish']['name']} (Health Score: {results['target_dish']['health_score']})")

for r in results['recommendations']:
    print(f"- {r['name']} | Match: {r['match_pct']}% | Cal: {r['calories']} | Prot: {r['protein']}g | Grade: {r['grade']}")
```

### 3. Target-to-Dish Recommendation

```python
# Find dishes matching clean high-protein profile
target = {'Calories': 180, 'Protein': 25, 'Carbohydrates': 10, 'Fats': 4}
results = engine.recommend_target(target, top_k=5)

for r in results['recommendations']:
    print(f"- {r['name']} | Match: {r['match_pct']}% | NRF: {r['health_score']:.1f}")
```

### 4. Real-time Nutri-Grade AI Prediction

```python
# Predict Nutri-Grade with automatic Atwater consistency check
pred = engine.predict_grade(sugar=2.5, fat=4.0, sodium=150.0)
print(f"Grade: {pred['grade']} | Confidence: {pred['confidence']:.1%} | Est. Calories: {pred['estimated_calories']}")
```
