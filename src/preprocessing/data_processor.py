"""
Data Preprocessing, Cleaning, Imputation, and Feature Engineering
for AI-Powered Nutritional Recommender System.
"""

from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

NUMERICAL_FEATURES: List[str] = [
    'Calories (kcal)',
    'Carbohydrates (g)',
    'Protein (g)',
    'Fats (g)',
    'Free Sugar (g)',
    'Fibre (g)',
    'Sodium (mg)',
    'Calcium (mg)',
    'Iron (mg)',
    'Vitamin C (mg)',
    'Folate (µg)'
]

CLASSIFICATION_FEATURES: List[str] = [
    'Calories (kcal)',
    'Carbohydrates (g)',
    'Protein (g)',
    'Fats (g)',
    'Free Sugar (g)',
    'Fibre (g)',
    'Sodium (mg)'
]

DV_POSITIVE: Dict[str, float] = {
    'Protein (g)': 50.0,
    'Fibre (g)': 28.0,
    'Vitamin C (mg)': 90.0,
    'Calcium (mg)': 1300.0,
    'Iron (mg)': 18.0
}

DV_NEGATIVE: Dict[str, float] = {
    'Free Sugar (g)': 50.0,
    'Fats (g)': 78.0,
    'Sodium (mg)': 2300.0
}

NAME_MAP: Dict[str, str] = {
    'Calories': 'Calories (kcal)',
    'calories': 'Calories (kcal)',
    'kcal': 'Calories (kcal)',
    'Energy': 'Calories (kcal)',
    'Carbs': 'Carbohydrates (g)',
    'carb': 'Carbohydrates (g)',
    'Carb': 'Carbohydrates (g)',
    'carbohydrates': 'Carbohydrates (g)',
    'Carbohydrates': 'Carbohydrates (g)',
    'Protein': 'Protein (g)',
    'protein': 'Protein (g)',
    'Fat': 'Fats (g)',
    'fat': 'Fats (g)',
    'Fats': 'Fats (g)',
    'fats': 'Fats (g)',
    'Sugar': 'Free Sugar (g)',
    'sugar': 'Free Sugar (g)',
    'Free Sugar': 'Free Sugar (g)',
    'Fiber': 'Fibre (g)',
    'fiber': 'Fibre (g)',
    'Fibre': 'Fibre (g)',
    'Sodium': 'Sodium (mg)',
    'sodium': 'Sodium (mg)',
    'Calcium': 'Calcium (mg)',
    'calcium': 'Calcium (mg)',
    'Iron': 'Iron (mg)',
    'iron': 'Iron (mg)',
    'Vitamin C': 'Vitamin C (mg)',
    'vitc': 'Vitamin C (mg)',
    'Folate': 'Folate (µg)',
    'folate': 'Folate (µg)'
}


def compute_nrf_score(row_or_df: Union[pd.Series, pd.DataFrame, Dict[str, float]]) -> Union[float, pd.Series]:
    """
    Calculate Nutrient Rich Foods (NRF 5.3) Index.
    NRF 5.3 = Sum(%DV 5 beneficial nutrients) - Sum(%DV 3 limiting nutrients)
    """
    if isinstance(row_or_df, dict):
        p_sum = (
            (row_or_df.get('Protein (g)', 0.0) / DV_POSITIVE['Protein (g)']) * 100.0 +
            (row_or_df.get('Fibre (g)', 0.0) / DV_POSITIVE['Fibre (g)']) * 100.0 +
            (row_or_df.get('Vitamin C (mg)', 0.0) / DV_POSITIVE['Vitamin C (mg)']) * 100.0 +
            (row_or_df.get('Calcium (mg)', 0.0) / DV_POSITIVE['Calcium (mg)']) * 100.0 +
            (row_or_df.get('Iron (mg)', 0.0) / DV_POSITIVE['Iron (mg)']) * 100.0
        )
        n_sum = (
            (row_or_df.get('Free Sugar (g)', 0.0) / DV_NEGATIVE['Free Sugar (g)']) * 100.0 +
            (row_or_df.get('Fats (g)', 0.0) / DV_NEGATIVE['Fats (g)']) * 100.0 +
            (row_or_df.get('Sodium (mg)', 0.0) / DV_NEGATIVE['Sodium (mg)']) * 100.0
        )
        return float(p_sum - n_sum)

    # DataFrame / Series computation
    p_protein = (row_or_df['Protein (g)'] / DV_POSITIVE['Protein (g)']) * 100.0
    p_fiber = (row_or_df['Fibre (g)'] / DV_POSITIVE['Fibre (g)']) * 100.0
    p_vitc = (row_or_df['Vitamin C (mg)'] / DV_POSITIVE['Vitamin C (mg)']) * 100.0
    p_calcium = (row_or_df['Calcium (mg)'] / DV_POSITIVE['Calcium (mg)']) * 100.0
    p_iron = (row_or_df['Iron (mg)'] / DV_POSITIVE['Iron (mg)']) * 100.0

    n_sugar = (row_or_df['Free Sugar (g)'] / DV_NEGATIVE['Free Sugar (g)']) * 100.0
    n_fat = (row_or_df['Fats (g)'] / DV_NEGATIVE['Fats (g)']) * 100.0
    n_sodium = (row_or_df['Sodium (mg)'] / DV_NEGATIVE['Sodium (mg)']) * 100.0

    positives = p_protein + p_fiber + p_vitc + p_calcium + p_iron
    negatives = n_sugar + n_fat + n_sodium

    return positives - negatives


def assign_nutri_grade(row: Union[pd.Series, Dict[str, float]]) -> str:
    """
    Ground-truth rule-based Nutri-Grade classification:
    - Grade C (Limit): Sugar > 15g OR Fats > 20g OR Sodium > 600mg
    - Grade A (Healthy): Sugar < 5g AND Fats < 5g AND Sodium < 200mg
    - Grade B (Moderate): Remaining
    """
    sugar = row['Free Sugar (g)'] if isinstance(row, pd.Series) else row.get('Free Sugar (g)', 0.0)
    fats = row['Fats (g)'] if isinstance(row, pd.Series) else row.get('Fats (g)', 0.0)
    sodium = row['Sodium (mg)'] if isinstance(row, pd.Series) else row.get('Sodium (mg)', 0.0)

    if sugar > 15.0 or fats > 20.0 or sodium > 600.0:
        return 'C (Limit)'
    elif sugar < 5.0 and fats < 5.0 and sodium < 200.0:
        return 'A (Healthy)'
    else:
        return 'B (Moderate)'


def load_and_preprocess_data(file_path: Union[str, Path]) -> pd.DataFrame:
    """
    Load raw or processed CSV dataset, apply median imputation for missing values,
    and compute all derived feature engineering columns.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found at {path}")

    df = pd.read_csv(path)

    # Impute missing values with median
    if 'Vitamin C (mg)' in df.columns:
        df['Vitamin C (mg)'] = df['Vitamin C (mg)'].fillna(df['Vitamin C (mg)'].median())
    if 'Folate (µg)' in df.columns:
        df['Folate (µg)'] = df['Folate (µg)'].fillna(df['Folate (µg)'].median())

    # Ensure all numerical columns are float
    for col in NUMERICAL_FEATURES:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0.0)

    # Binary Tags
    df['High_Protein'] = (df['Protein (g)'] > 10.0).astype(int)
    df['Low_Carb'] = (df['Carbohydrates (g)'] < 15.0).astype(int)
    df['Low_Calorie'] = (df['Calories (kcal)'] < 150.0).astype(int)

    # NRF 5.3 Health Score
    df['Health_Score'] = compute_nrf_score(df)

    # Nutri-Grade Ground Truth
    df['Grade'] = df.apply(assign_nutri_grade, axis=1)

    return df
