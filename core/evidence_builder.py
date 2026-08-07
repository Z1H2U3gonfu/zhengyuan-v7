import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, Any


class EvidenceBuilder:
    """四层证据包构建器"""

    def __init__(self, output_dir: str = "./output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def build(self, input_layer: Dict, control_layer: Dict,
              process_layer: Dict, replay_layer: Dict) -> Dict:
        """构建完整证据包"""
        package = {
            "version": "v7.0",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "layers": {
                "input": input_layer,
                "control": control_layer,
                "process": process_layer,
                "replay": replay_layer
            }
        }
        package["hash"] = self._compute_hash(package)
        return package

    def _compute_hash(self, package: Dict) -> str:
        package_copy = {k: v for k, v in package.items() if k != "hash"}
        serialized = json.dumps(package_copy, sort_keys=True)
        return hashlib.sha256(serialized.encode()).hexdigest()

    def save(self, package: Dict, filename: str = "evidence.json") -> str:
        filepath = self.output_dir / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(package, f, ensure_ascii=False, indent=2)
        return str(filepath)
