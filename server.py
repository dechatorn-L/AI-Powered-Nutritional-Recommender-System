"""
Root CLI Server Launcher for AI-Powered Nutritional Recommender System.
"""

import sys
import argparse
from pathlib import Path

# Ensure UTF-8 output
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from src.web.server import run_server

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Launch Nutrition AI Web Application")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host IP (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8000, help="Port (default: 8000)")
    args = parser.parse_args()

    print(f"[*] Starting Nutrition AI Server on port {args.port}...")
    run_server(host=args.host, port=args.port)
