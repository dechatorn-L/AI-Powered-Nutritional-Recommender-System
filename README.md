# 🥗 AI-Powered Nutritional Recommender System & Health Intelligence

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3%2B-orange.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg)](LICENSE)
[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-success.svg)](#)

> **ระบบแนะนำอาหารเพื่อสุขภาพและวิเคราะห์โภชนาการอัจฉริยะ**
> An end-to-end Machine Learning and Nutritional Science platform combining **NRF 5.3 Indexing**, **KNN Euclidean Similarity Search**, **K-Means 2D PCA Clustering**, and **Random Forest Nutri-Grade AI (98.0% Accuracy)** with Atwater energy consistency checking.

---

## 🌟 Key Highlights & Core Capabilities

| Capability | Algorithm / Technique | Description |
|---|---|---|
| 🔍 **Dish-to-Dish Hybrid Recommender** | KNN on 11-D StandardScaler Space | Finds healthiest and closest nutritional alternatives for any selected dish with percentage match scores. |
| 🎯 **Target Nutrient Matching** | Vector Space Euclidean Distance | Recommends dishes matching custom nutritional targets (e.g. 25g Protein, <300 kcal, low sodium). |
| 🧪 **Nutri-Grade Classification AI** | Random Forest Classifier (100 Trees) | Automatically categorizes foods into **Grade A (Healthy)**, **Grade B (Moderate)**, and **Grade C (Limit)** with 98.0% accuracy. |
| ⚡ **Atwater Energy Consistency Engine** | Caloric Density Balancing | Validates nutrient inputs ($\text{Fat}\times 9 + \text{Prot}\times 4 + \text{Carb}\times 4$) to avoid out-of-distribution hallucinations. |
| 📊 **Nutrient Rich Foods (NRF 5.3) Index** | Science-Based %DV Scoring | Evaluates 5 positive nutrients against 3 negative/qualifying nutrients to give an objective Health Score. |
| 🗺️ **2D PCA & Cluster Segmentation** | K-Means ($K=5$) + PCA Projection | Unsupervised clustering into 5 culinary profiles with 2D coordinate projections for spatial visualization. |
| 🌐 **NutriPulse Intelligence Web UI** | Vanilla CSS + HTML5 + Chart.js | HealthTech Enterprise aesthetic, single-bar navigation, zero scrollbars, Bento Grid layout, 1,014 Dish Catalog Popup Modal, dark/light theme, bilingual (TH/EN), live radar charts, and interactive PCA scatter. |

---

## 🏗️ System Architecture

```mermaid
graph TD
    subgraph Data Acquisition & Preprocessing Layer
        A1["Raw Nutrition Dataset<br/>(data/raw/Indian_Food_Nutrition_Raw.csv)"] --> A2["Data Ingestion & Cleaning<br/>(src/preprocessing/data_processor.py)"]
        A2 --> A3["Median Imputation<br/>(Vitamin C & Folate)"]
        A3 --> A4["Feature Engineering<br/>(NRF 5.3 Index, Binary Tags, Nutri-Grades)"]
        A4 --> A5["StandardScaler Transformation<br/>(11-Dimensional Macro & Micro Vector Space)"]
        A6["Curated Embedded Fallback<br/>(src/default_data.py)"] -.->|Self-Healing Fallback| A5
    end

    subgraph Core ML & Nutrition Intelligence Engine (src/engine.py)
        A5 --> B1["Unified NutritionAIEngine<br/>(Singleton & In-Memory Cache)"]
        B1 --> B2["KNN Recommender Subsystem<br/>(Dish-to-Dish & Target-to-Dish)"]
        B1 --> B3["K-Means Clusterer<br/>(K=5 Culinary Profiles)"]
        B1 --> B4["2D PCA Dimensionality Reduction<br/>(Recipe Vectors & Centroids)"]
        B1 --> B5["Random Forest Nutri-Grade AI<br/>(Classification + Atwater Consistency Check)"]
        B1 --> B6["Model Evaluation & Insights<br/>(Confusion Matrix & Feature Importances)"]
    end

    subgraph Service Delivery & Interface Layer
        B1 --> C1["Production REST API Server<br/>(server.py / src/web/server.py)"]
        B1 --> C2["Interactive Streamlit Dashboard<br/>(app_streamlit.py)"]
        B1 --> C3["Python SDK Facade<br/>(engine.py)"]
        C1 --> D1["NutriPulse Intelligence Web UI<br/>(web/index.html + app.js + style.css)"]
    end
```

---

## 📐 Mathematical & Algorithmic Formulation

### 1. Nutrient Rich Foods Index (NRF 5.3)
$$\text{NRF 5.3} = \sum_{i=1}^5 \left( \frac{\text{Nutrient}_i^+}{\text{DV}_i^+} \times 100 \right) - \sum_{j=1}^3 \left( \frac{\text{Nutrient}_j^-}{\text{DV}_j^-} \times 100 \right)$$
- **Encouraged Nutrients ($+$)**: Protein ($50\text{g}$), Fibre ($28\text{g}$), Vitamin C ($90\text{mg}$), Calcium ($1300\text{mg}$), Iron ($18\text{mg}$).
- **Limiting Nutrients ($-$)**: Free Sugar ($50\text{g}$), Total Fats ($78\text{g}$), Sodium ($2300\text{mg}$).

### 2. Standardized Euclidean Distance & Match Percentage
$$\text{Match Percentage} = \frac{100}{1 + d(\vec{z}_{\text{target}}, \vec{z}_{\text{candidate}})}, \quad \text{where } d(\vec{z}_q, \vec{z}_d) = \sqrt{\sum_{k=1}^{11} (z_{qk} - z_{dk})^2}$$

### 3. Atwater Caloric Consistency Balancing
$$\text{Estimated Calories} = (\text{Fat} \times 9) + (\text{Protein} \times 4) + (\text{Carbohydrates} \times 4)$$

---

## 📂 Project Structure

```
AI-Powered-Nutritional-Recommender-System-main/
├── .agents/
│   ├── rules/
│   │   └── style.md                     # Agent response & development rules
│   └── skills/
│       └── nutrition_ai/
│           └── SKILL.md                 # Antigravity skill specification
├── docs/
│   ├── ARCHITECTURE.md                  # Comprehensive engineering & mathematical design
│   ├── INDEX.md                         # Documentation index & quick guide
│   ├── ROADMAP.md                       # Engineering roadmap & milestones
│   ├── SPECIFICATION.md                 # REST API specification & JSON contracts
│   └── STYLE_GUIDE.md                   # HealthTech Enterprise UI/UX design tokens
├── data/
│   ├── raw/
│   │   └── Indian_Food_Nutrition_Raw.csv
│   └── processed/
│       └── Indian_Food_Nutrition_Processed.csv
├── src/
│   ├── __init__.py                      # Package root
│   ├── default_data.py                  # Self-healing embedded fallback dataset
│   ├── engine.py                        # Unified NutritionAIEngine singleton
│   ├── preprocessing/
│   │   ├── __init__.py
│   │   └── data_processor.py            # Median imputation, NRF 5.3 scoring, scaling
│   ├── modeling/
│   │   ├── __init__.py
│   │   ├── recommender.py               # KNN dish-to-dish & target-to-dish engine
│   │   ├── clusterer.py                 # K-Means clustering & 2D PCA mapping
│   │   ├── classifier.py                # Random Forest Nutri-Grade AI classifier
│   │   └── evaluator.py                 # Model evaluation metrics & confusion matrix
│   └── web/
│       ├── __init__.py
│       └── server.py                    # Production REST HTTP server & static handler
├── web/
│   ├── index.html                       # Single-Bar Nav, Bento Grid, 1,014 Dish Catalog Modal, bilingual TH/EN
│   ├── style.css                        # HealthTech Enterprise design system, zero scrollbars, dark/light theme
│   └── app.js                           # Frontend controller, Chart.js radar/bar charts, live PCA map, modal filter
├── app_streamlit.py                     # Streamlit interactive dashboard alternative
├── engine.py                            # Top-level entrypoint facade
├── server.py                            # Top-level server CLI runner
├── requirements.txt                     # Pinned project dependencies
├── .gitignore                           # Production gitignore
├── README.md                            # Project overview & documentation
├── Indian_Food_Nutrition_Processed.csv  # Root dataset (preserved for notebook compatibility)
├── data.ipynb                           # Original exploratory data analysis notebook
└── model1.ipynb                         # Original machine learning notebook
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites & Installation
```bash
# Clone the repository
git clone https://github.com/your-username/AI-Powered-Nutritional-Recommender-System.git
cd AI-Powered-Nutritional-Recommender-System

# Install dependencies
pip install -r requirements.txt
```

### 2. Launch the Web Application
```bash
python server.py --port 8000
```
Open **`http://localhost:8000`** in your browser to experience the full interactive interface.

### 3. Launch the Streamlit Dashboard
```bash
streamlit run app_streamlit.py
```

### 4. Run CLI Quick Test
```bash
python engine.py
```

---

## 🐍 Python SDK Usage

```python
from src.engine import get_engine

# Initialize unified Nutrition AI engine
engine = get_engine()

# 1. Dish-to-Dish Recommendation
recs = engine.recommend_dish("Butter Chicken", top_k=5)
print(f"Target: {recs['target_dish']['name']} (Health Score: {recs['target_dish']['health_score']})")
for r in recs['recommendations']:
    print(f"- {r['name']} | Match: {r['match_pct']}% | Grade: {r['grade']}")

# 2. Target Nutrient Search
target = {'Calories': 200, 'Protein': 25, 'Carbohydrates': 10, 'Fats': 5}
matches = engine.recommend_target(target, top_k=3)
for m in matches['recommendations']:
    print(f"- {m['name']} | Match: {m['match_pct']}%")

# 3. Nutri-Grade AI Prediction
pred = engine.predict_grade(sugar=2.5, fat=4.0, sodium=150.0)
print(f"Predicted Grade: {pred['grade']} (Confidence: {pred['confidence']:.1%})")
```

---

## 📡 REST API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/status` | System health, uptime, dataset count, and model accuracy |
| `GET` | `/api/dishes` | List indexed dishes with pagination and filter params (`q`, `category`, `grade`) |
| `GET` | `/api/recommend/dish` | Dish-to-dish recommendations (`?name=Butter+Chicken&k=5`) |
| `POST` | `/api/recommend/target` | Target nutrient profile vector matching |
| `POST` | `/api/grade/predict` | Real-time Nutri-Grade AI classification with confidence score |
| `GET` | `/api/clusters` | 2D PCA coordinates, cluster statistics, and centroids |
| `GET` | `/api/evaluation` | Confusion matrix, classification report, and feature importances |
| `GET` | `/api/distribution` | Statistical distributions (min, max, median, std) for all 11 nutrients |

---

## 👤 Author & Credits

**Dechatorn Laikhain**
* **Role:** Data Scientist / Machine Learning Engineer
* **LinkedIn:** [linkedin.com/in/dechatorn-laikhain-0b89953a2](https://www.linkedin.com/in/dechatorn-laikhain-0b89953a2)

---
*Built with clean production architecture, mathematical rigor, and modern web aesthetics.*