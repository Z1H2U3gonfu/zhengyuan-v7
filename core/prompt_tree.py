import hashlib
from datetime import datetime
from typing import List, Dict, Any, Optional


class TreeNode:
    """版本树节点"""

    def __init__(self, content: str, parent: Optional["TreeNode"] = None,
                 metadata: Optional[Dict] = None):
        self.content = content
        self.parent = parent
        self.children: List["TreeNode"] = []
        self.metadata = metadata or {}
        self.timestamp = datetime.utcnow().isoformat() + "Z"
        self.node_id = self._compute_node_id()

    def _compute_node_id(self) -> str:
        data = f"{self.content}{self.timestamp}"
        return hashlib.sha256(data.encode()).hexdigest()[:16]

    def add_child(self, child: "TreeNode") -> None:
        child.parent = self
        self.children.append(child)

    def to_dict(self) -> Dict:
        return {
            "node_id": self.node_id,
            "content": self.content[:200] + "..." if len(self.content) > 200 else self.content,
            "timestamp": self.timestamp,
            "metadata": self.metadata,
            "children": [c.to_dict() for c in self.children]
        }


class PromptTree:
    """提示词版本树"""

    def __init__(self, root_content: str, root_metadata: Optional[Dict] = None):
        self.root = TreeNode(root_content, metadata=root_metadata)
        self.current = self.root
        self.all_nodes: List[TreeNode] = [self.root]

    def add_version(self, content: str, metadata: Optional[Dict] = None) -> TreeNode:
        new_node = TreeNode(content, parent=self.current, metadata=metadata)
        self.current.add_child(new_node)
        self.current = new_node
        self.all_nodes.append(new_node)
        return new_node

    def switch_to(self, node_id: str) -> bool:
        for node in self.all_nodes:
            if node.node_id == node_id:
                self.current = node
                return True
        return False

    def get_history(self) -> List[Dict]:
        history = []
        node = self.current
        while node:
            history.append(node.to_dict())
            node = node.parent
        return list(reversed(history))

    def to_dict(self) -> Dict:
        return {
            "root": self.root.to_dict(),
            "current_node": self.current.node_id,
            "total_versions": len(self.all_nodes)
  }
