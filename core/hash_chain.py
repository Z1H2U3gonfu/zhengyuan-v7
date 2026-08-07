import hashlib
import json
from datetime import datetime
from typing import List, Dict, Any, Optional


class HashChain:
    """SHA-256哈希链"""

    def __init__(self):
        self.blocks: List[Dict[str, Any]] = []
        self.last_hash: Optional[str] = None

    def add_block(self, data: Dict[str, Any]) -> str:
        block = {
            "index": len(self.blocks),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "data": data,
            "prev_hash": self.last_hash
        }
        serialized = json.dumps(block, sort_keys=True)
        block["hash"] = hashlib.sha256(serialized.encode()).hexdigest()
        self.blocks.append(block)
        self.last_hash = block["hash"]
        return block["hash"]

    def verify(self) -> bool:
        if not self.blocks:
            return True
        for i, block in enumerate(self.blocks):
            if i > 0 and block["prev_hash"] != self.blocks[i-1]["hash"]:
                return False
            block_copy = {k: v for k, v in block.items() if k != "hash"}
            serialized = json.dumps(block_copy, sort_keys=True)
            computed = hashlib.sha256(serialized.encode()).hexdigest()
            if computed != block["hash"]:
                return False
        return True

    def get_chain(self) -> List[Dict]:
        return self.blocks.copy()

    def get_last_hash(self) -> Optional[str]:
        return self.last_hash
