import hashlib
import json
from typing import Dict, Any, Optional


class ParamLocker:
    """参数锁定器"""

    def __init__(self):
        self.locked_params: Dict[str, Any] = {}
        self.lock_signature: Optional[str] = None

    def lock(self, params: Dict[str, Any]) -> str:
        self.locked_params = params.copy()
        serialized = json.dumps(params, sort_keys=True)
        self.lock_signature = hashlib.sha256(serialized.encode()).hexdigest()
        return self.lock_signature

    def verify(self, params: Dict[str, Any]) -> bool:
        if not self.lock_signature:
            return False
        serialized = json.dumps(params, sort_keys=True)
        computed = hashlib.sha256(serialized.encode()).hexdigest()
        return computed == self.lock_signature

    def get_locked_params(self) -> Dict[str, Any]:
        return self.locked_params.copy()

    def get_signature(self) -> Optional[str]:
        return self.lock_signature

    def to_dict(self) -> Dict[str, Any]:
        return {
            "locked_params": self.locked_params,
            "signature": self.lock_signature,
            "algorithm": "sha256"
        }
