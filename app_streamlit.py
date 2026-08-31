"""
Interactive Streamlit Dashboard for AI-Powered Nutritional Recommender System.
Provides visual analytics, KNN recommendations, K-Means clustering, and Nutri-Grade AI simulation.
"""

import sys
from pathlib import Path
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure src is in python path
SRC_DIR = Path(__file__).resolve().parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from engine import get_engine

st.set_page_config(
    page_title="Nutrition AI · ระบบแนะนำอาหารและวิเคราะห์โภชนาการอัจฉริยะ",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #10b981;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        color: #94a3b8;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }
    .metric-badge {
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.3);
        padding: 0.4rem 0.8rem;
        border-radius: 8px;
        display: inline-block;
    }
    .preset-pill {
        display: inline-block;
        padding: 0.2rem 0.6rem;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.05);
        margin-right: 0.4rem;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_nutrition_engine():
    return get_engine()


engine = load_nutrition_engine()
status = engine.get_system_status()

# Sidebar Navigation
st.sidebar.markdown("## 🥗 Nutrition AI Studio")
nav_choice = st.sidebar.radio(
    "Select Feature Tab / เลือกเมนู:",
    [
        "🔍 Dish-to-Dish Recommendation",
        "🎯 Target Nutrient Matching",
        "🧪 Nutri-Grade AI Classifier",
        "📊 2D PCA Nutrition Map",
        "📈 ML Evaluation & Insights",
        "📖 Dataset Explorer"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown(f"**Dataset:** {status['dataset_count']} Dishes")
st.sidebar.markdown(f"**Clusters:** {status['clusters_count']} Profiles")
st.sidebar.markdown(f"**AI Accuracy:** {status['model_accuracy'] * 100:.1f}%")
st.sidebar.markdown("---")
st.sidebar.caption("Author: **Dechatorn Laikhain**")


# ==========================================
# 1. DISH-TO-DISH RECOMMENDATION
# ==========================================
if nav_choice == "🔍 Dish-to-Dish Recommendation":
    st.markdown('<div class="main-header">🔍 Dish-to-Dish Smart Recommender</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">ค้นหาเมนูอาหารและแนะนำเมนูทดแทนที่ดีต่อสุขภาพด้วย KNN Euclidean Distance บนเวกเตอร์ 11 มิติ</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])
    with col1:
        dish_name_input = st.text_input("Enter Dish Name / ชื่อเมนู:", value="Butter Chicken")
    with col2:
        top_k = st.slider("Recommendations (K):", min_value=3, max_value=15, value=5)

    if st.button("Search & Recommend ➜", type="primary"):
        res = engine.recommend_dish(dish_name_input, top_k=top_k)
        if not res.get("success"):
            st.error(res.get("error"))
        else:
            t = res["target_dish"]
            st.success(f"🎯 Found target dish: **{t['name']}** | Category: `{t['category']}` | Grade: **{t['grade']}** | NRF Health Score: **{t['health_score']}**")

            # Metrics row
            m1, m2, m3, m4, m5 = st.columns(5)
            m1.metric("Calories", f"{t['calories']} kcal")
            m2.metric("Protein", f"{t['protein']} g")
            m3.metric("Carbs", f"{t['carbs']} g")
            m4.metric("Fats", f"{t['fats']} g")
            m5.metric("Sodium", f"{t['sodium']} mg")

            st.markdown("### ✨ Recommended Similar Dishes")
            recs_df = pd.DataFrame(res["recommendations"])
            display_cols = ["name", "category", "match_pct", "health_score", "grade", "calories", "protein", "carbs", "fats", "sugar", "sodium"]
            st.dataframe(recs_df[display_cols], use_container_width=True)


# ==========================================
# 2. TARGET NUTRIENT MATCHING
# ==========================================
elif nav_choice == "🎯 Target Nutrient Matching":
    st.markdown('<div class="main-header">🎯 Target Nutrient Profile Matching</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">กำหนดเป้าหมายสารอาหารที่ต้องการ ระบบจะค้นหาเมนูที่ใกล้เคียงที่สุด</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        cal = st.slider("Target Calories (kcal):", 50, 800, 200)
        prot = st.slider("Target Protein (g):", 0, 60, 25)
    with c2:
        carb = st.slider("Target Carbs (g):", 0, 100, 15)
        fat = st.slider("Target Fats (g):", 0, 50, 6)
    with c3:
        sug = st.slider("Target Sugar (g):", 0, 40, 2)
        sod = st.slider("Target Sodium (mg):", 10, 1500, 300)

    if st.button("Find Matching Dishes ➜", type="primary"):
        target_dict = {
            "Calories": cal,
            "Protein": prot,
            "Carbohydrates": carb,
            "Fats": fat,
            "Free Sugar": sug,
            "Sodium": sod
        }
        res = engine.recommend_target(target_dict, top_k=6)
        if res.get("success"):
            st.markdown("### ✨ Top Matches")
            recs_df = pd.DataFrame(res["recommendations"])
            display_cols = ["name", "category", "match_pct", "health_score", "grade", "calories", "protein", "carbs", "fats", "sugar", "sodium"]
            st.dataframe(recs_df[display_cols], use_container_width=True)


# ==========================================
# 3. NUTRI-GRADE AI CLASSIFIER
# ==========================================
elif nav_choice == "🧪 Nutri-Grade AI Classifier":
    st.markdown('<div class="main-header">🧪 Nutri-Grade AI Classification Simulator</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">จำลองปริมาณสารอาหารเพื่อตัดเกรด A/B/C ด้วย Random Forest และตรวจสอบ Atwater Calorie Consistency</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Input Macronutrients")
        sug = st.number_input("Free Sugar (g):", min_value=0.0, max_value=100.0, value=3.0, step=0.5)
        fat = st.number_input("Total Fats (g):", min_value=0.0, max_value=100.0, value=4.0, step=0.5)
        sod = st.number_input("Sodium (mg):", min_value=0.0, max_value=3000.0, value=150.0, step=10.0)
        prot = st.number_input("Protein (g) [Optional]:", min_value=0.0, max_value=100.0, value=15.0, step=0.5)
        carb = st.number_input("Carbohydrates (g) [Optional]:", min_value=0.0, max_value=200.0, value=10.0, step=0.5)

    with c2:
        st.markdown("#### AI Prediction Result")
        if st.button("Predict Nutri-Grade 🔬", type="primary"):
            pred = engine.predict_grade(sugar=sug, fat=fat, sodium=sod, protein=prot, carb=carb)
            if pred.get("success"):
                grade = pred["grade"]
                conf = pred["confidence"] * 100
                est_cal = pred["estimated_calories"]

                if grade.startswith("A"):
                    st.success(f"## 🏆 {grade}\n**Confidence:** {conf:.1f}%\n\n**Estimated Calories:** {est_cal} kcal")
                elif grade.startswith("B"):
                    st.warning(f"## ⚖️ {grade}\n**Confidence:** {conf:.1f}%\n\n**Estimated Calories:** {est_cal} kcal")
                else:
                    st.error(f"## ⚠️ {grade}\n**Confidence:** {conf:.1f}%\n\n**Estimated Calories:** {est_cal} kcal")

                st.markdown("##### Class Probabilities Breakdown:")
                st.json(pred["probabilities"])


# ==========================================
# 4. 2D PCA NUTRITION MAP
# ==========================================
elif nav_choice == "📊 2D PCA Nutrition Map":
    st.markdown('<div class="main-header">📊 2D PCA Nutrition Map & Clustering</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">แผนผังการกระจายตัวของอาหาร 1,014 เมนู บนระนาบ 2 มิติด้วย PCA จาก 11 มิติสารอาหาร</div>', unsafe_allow_html=True)

    clusters_data = engine.get_clusters_data()
    points = clusters_data.get("points", [])
    if points:
        pts_df = pd.DataFrame(points)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(
            data=pts_df,
            x="x",
            y="y",
            hue="category",
            palette="tab10",
            alpha=0.8,
            s=40,
            ax=ax
        )
        ax.set_title("2D PCA Projection of Indian Food Nutritional Profiles", fontsize=14, fontweight="bold")
        ax.set_xlabel("Principal Component 1 (Energy & Protein Density)")
        ax.set_ylabel("Principal Component 2 (Micronutrients & Sugar/Fat Ratio)")
        st.pyplot(fig)

        st.markdown("### 🏷️ Cluster Profiles Summary")
        cl_df = pd.DataFrame(clusters_data["clusters"])
        st.dataframe(cl_df[["id", "name", "count", "avg_nutrients"]], use_container_width=True)


# ==========================================
# 5. ML EVALUATION & INSIGHTS
# ==========================================
elif nav_choice == "📈 ML Evaluation & Insights":
    st.markdown('<div class="main-header">📈 ML Evaluation & Model Insights</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">รายงานผลการวัดประสิทธิภาพโมเดล Random Forest และ Confusion Matrix</div>', unsafe_allow_html=True)

    eval_data = engine.get_evaluation_metrics()
    if eval_data:
        m1, m2, m3 = st.columns(3)
        m1.metric("Overall Accuracy", f"{eval_data['accuracy'] * 100:.1f}%")
        m2.metric("Macro F1-Score", f"{eval_data['macro_f1']:.3f}")
        m3.metric("Test Samples", eval_data['test_sample_count'])

        col_cm, col_imp = st.columns(2)
        with col_cm:
            st.markdown("#### Confusion Matrix")
            cm = np.array(eval_data["confusion_matrix"]["matrix"])
            labels = eval_data["confusion_matrix"]["labels"]
            fig_cm, ax_cm = plt.subplots(figsize=(5, 4))
            sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels, ax=ax_cm)
            ax_cm.set_ylabel("Actual Grade")
            ax_cm.set_xlabel("Predicted Grade")
            st.pyplot(fig_cm)

        with col_imp:
            st.markdown("#### Feature Importance")
            imp_df = pd.DataFrame(eval_data["feature_importances"])
            fig_imp, ax_imp = plt.subplots(figsize=(6, 4))
            sns.barplot(data=imp_df, x="importance", y="feature", palette="viridis", ax=ax_imp)
            ax_imp.set_title("What drives the Nutri-Grade?")
            st.pyplot(fig_imp)


# ==========================================
# 6. DATASET EXPLORER
# ==========================================
elif nav_choice == "📖 Dataset Explorer":
    st.markdown('<div class="main-header">📖 Nutritional Dataset Explorer</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">สำรวจและคัดกรองข้อมูลสารอาหารทั้งหมดในระบบ</div>', unsafe_allow_html=True)

    if engine.df is not None:
        search_filter = st.text_input("Filter by dish name:", "")
        filtered = engine.df
        if search_filter:
            filtered = filtered[filtered["Dish Name"].str.lower().str.contains(search_filter.lower(), regex=False)]

        st.markdown(f"**Showing {len(filtered)} / {len(engine.df)} dishes**")
        st.dataframe(filtered, use_container_width=True)
