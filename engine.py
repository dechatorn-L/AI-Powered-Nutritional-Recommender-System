"""
Top-level entrypoint facade for NutritionAIEngine.
"""

import sys

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from src.engine import get_engine, NutritionAIEngine

__all__ = ["get_engine", "NutritionAIEngine"]

if __name__ == "__main__":
    print("[*] Initializing Nutrition AI Engine...")
    eng = get_engine()
    status = eng.get_system_status()
    print(f"[+] Ready! Loaded {status['dataset_count']} dishes across {status['clusters_count']} clusters.")
    print(f"[+] Nutri-Grade AI Accuracy: {status['model_accuracy'] * 100:.1f}%\n")

    # Quick CLI Demo
    test_dish = "Butter Chicken"
    print(f"--- Quick Test: Similar Dishes to '{test_dish}' ---")
    recs = eng.recommend_dish(test_dish, top_k=5)
    if recs.get('success'):
        target = recs['target_dish']
        print(f"Target: {target['name']} | Health Score: {target['health_score']} | Grade: {target['grade']}")
        for r in recs['recommendations']:
            print(f"  -> {r['name']:<30} | Match: {r['match_pct']:>5.1f}% | Cal: {r['calories']:>5.1f} | Prot: {r['protein']:>4.1f}g | Grade: {r['grade']}")
    else:
        print(f"Error: {recs.get('error')}")
