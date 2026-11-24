"""Central project paths and settings. Import from here instead of hardcoding paths."""
import os
from pathlib import Path

from dotenv import load_dotenv

# config.py lives in src/finsight/, so the project root is two folders up
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

load_dotenv(PROJECT_ROOT / ".env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # None until Phase 9 — that's fine