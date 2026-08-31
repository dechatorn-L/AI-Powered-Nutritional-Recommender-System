"""
Embedded Production REST API Server & Static Asset Handler.
Zero external server framework dependencies.
"""

import sys
import json
import urllib.parse
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
import argparse

from ..engine import get_engine

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
WEB_DIR = PROJECT_ROOT / "web"


class NutritionAIRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB_DIR), **kwargs)

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query_params = urllib.parse.parse_qs(parsed_url.query)

        if path == "/api/status":
            self.handle_status_api()
        elif path == "/api/dishes":
            self.handle_dishes_api(query_params)
        elif path == "/api/recommend/dish":
            self.handle_recommend_dish_api(query_params)
        elif path == "/api/clusters":
            self.handle_clusters_api()
        elif path == "/api/evaluation":
            self.handle_evaluation_api()
        elif path == "/api/distribution":
            self.handle_distribution_api()
        elif path == "/" or path == "":
            self.path = "/index.html"
            super().do_GET()
        else:
            super().do_GET()

    def do_POST(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path

        content_length = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else "{}"

        try:
            body_json = json.loads(post_body)
        except Exception:
            body_json = {}

        if path == "/api/recommend/target":
            self.handle_recommend_target_api(body_json)
        elif path == "/api/grade/predict":
            self.handle_predict_grade_api(body_json)
        else:
            self.send_error(404, "Endpoint not found")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def send_json_response(self, data, status_code=200):
        response_bytes = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(response_bytes)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(response_bytes)

    def handle_status_api(self):
        engine = get_engine()
        status = engine.get_system_status()
        self.send_json_response(status)

    def handle_dishes_api(self, query_params):
        engine = get_engine()
        q = query_params.get('q', [None])[0]
        category = query_params.get('category', [None])[0]
        grade = query_params.get('grade', [None])[0]
        limit = int(query_params.get('limit', [50])[0])
        offset = int(query_params.get('offset', [0])[0])

        res = engine.get_dishes(query=q, category=category, grade=grade, limit=limit, offset=offset)
        self.send_json_response(res)

    def handle_recommend_dish_api(self, query_params):
        engine = get_engine()
        name = query_params.get('name', query_params.get('q', ['']))[0]
        k = int(query_params.get('k', [5])[0])

        if not name:
            self.send_json_response({"success": False, "error": "Dish name is required"}, status_code=400)
            return

        res = engine.recommend_dish(name, top_k=k)
        self.send_json_response(res)

    def handle_recommend_target_api(self, body_json):
        engine = get_engine()
        k = int(body_json.get('k', body_json.get('top_k', 5)))
        res = engine.recommend_target(body_json, top_k=k)
        self.send_json_response(res)

    def handle_predict_grade_api(self, body_json):
        engine = get_engine()
        sugar = float(body_json.get('sugar', body_json.get('Free Sugar (g)', 0.0)))
        fat = float(body_json.get('fat', body_json.get('Fats (g)', 0.0)))
        sodium = float(body_json.get('sodium', body_json.get('Sodium (mg)', 0.0)))
        protein = body_json.get('protein', body_json.get('Protein (g)'))
        carb = body_json.get('carb', body_json.get('Carbohydrates (g)'))
        fiber = body_json.get('fiber', body_json.get('Fibre (g)'))
        calories = body_json.get('calories', body_json.get('Calories (kcal)'))

        res = engine.predict_grade(
            sugar=sugar,
            fat=fat,
            sodium=sodium,
            protein=float(protein) if protein is not None else None,
            carb=float(carb) if carb is not None else None,
            fiber=float(fiber) if fiber is not None else None,
            calories=float(calories) if calories is not None else None
        )
        self.send_json_response(res)

    def handle_clusters_api(self):
        engine = get_engine()
        clusters_data = engine.get_clusters_data()
        self.send_json_response(clusters_data)

    def handle_evaluation_api(self):
        engine = get_engine()
        eval_data = engine.get_evaluation_metrics()
        self.send_json_response(eval_data)

    def handle_distribution_api(self):
        engine = get_engine()
        dist_data = engine.get_nutritional_distributions()
        self.send_json_response(dist_data)


def run_server(host: str = "0.0.0.0", port: int = 8000):
    """
    Start embedded REST API server.
    """
    server_address = (host, port)
    httpd = HTTPServer(server_address, NutritionAIRequestHandler)
    print(f"==================================================")
    print(f"🥗 Nutrition AI REST Server active on http://localhost:{port}")
    print(f"📂 Web UI Directory: {WEB_DIR}")
    print(f"==================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Shutting down server gracefully...")
        httpd.server_close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Nutrition AI REST Server")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host IP")
    parser.add_argument("--port", type=int, default=8000, help="Port number")
    args = parser.parse_args()
    run_server(host=args.host, port=args.port)
