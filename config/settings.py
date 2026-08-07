import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = os.getenv("EVIDENCE_OUTPUT_DIR", "./output")
HASH_ALGORITHM = os.getenv("HASH_ALGORITHM", "sha256")
MAX_TREE_DEPTH = int(os.getenv("MAX_TREE_DEPTH", "50"))
