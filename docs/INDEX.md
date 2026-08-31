# 📚 Documentation Index

Welcome to the comprehensive technical documentation for the **AI-Powered Nutritional Recommender System**.

---

## 🗂️ Documentation Sitemap

| Document | Description |
|---|---|
| 🏗️ [System Architecture](ARCHITECTURE.md) | High-level system architecture, component diagrams, mathematical formulation (NRF 5.3, KNN, K-Means, PCA, Random Forest), and data flow pipelines. |
| 📋 [API & System Specification](SPECIFICATION.md) | Full REST API contracts, JSON schemas, 11-D nutrient vector definitions, and error codes. |
| 🎨 [UI/UX Design System](STYLE_GUIDE.md) | Visual design tokens, HealthTech Enterprise aesthetic, single-bar navigation, color palettes, responsive Bento layouts, and typography. |
| 🗺️ [Engineering Roadmap](ROADMAP.md) | Development milestones, completed features, and future system expansions. |

---

## ⚡ Quick Start Guide

### 1. Run the Web Application
```bash
python server.py --port 8000
```
Open `http://localhost:8000` in your web browser.

### 2. Run the Streamlit Dashboard
```bash
streamlit run app_streamlit.py
```

### 3. Programmatic Usage in Python
```python
from src.engine import get_engine

engine = get_engine()
recs = engine.recommend_dish("Butter Chicken", top_k=5)
print(recs)
```
