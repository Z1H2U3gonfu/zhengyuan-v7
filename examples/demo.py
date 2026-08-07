#!/usr/bin/env python3
"""证源 v7.0 快速演示"""

from core import EvidenceBuilder, PromptTree, ParamLocker, HashChain


def demo():
    print("🧠 证源 v7.0 演示")
    print("=" * 40)

    content = "写一首关于秋天的诗"

    # 1. 构建版本树
    tree = PromptTree(content)
    tree.add_version(content + "\n\n-- v2: 增加色彩描写")
    tree.add_version(content + "\n\n-- v3: 增加情感表达")

    # 2. 锁定参数
    locker = ParamLocker()
    signature = locker.lock({"temperature": 0.7, "top_p": 0.9})

    # 3. 构建证据包
    builder = EvidenceBuilder()
    evidence = builder.build(
        input_layer={"original": content, "source": "demo"},
        control_layer={"params": {"temperature": 0.7}, "signature": signature},
        process_layer={"versions": tree.get_history()},
        replay_layer={"command": "python main.py --input prompt.txt"}
    )

    # 4. 生成哈希链
    chain = HashChain()
    for layer_name, layer_data in evidence["layers"].items():
        chain.add_block({
            "layer": layer_name,
            "data": layer_data
        })

    print(f"证据包哈希: {evidence['hash'][:16]}...")
    print(f"哈希链长度: {len(chain.get_chain())}")
    print(f"哈希链状态: {'✅ 完整' if chain.verify() else '❌ 已损坏'}")

    print("\n✅ 演示完成")


if __name__ == "__main__":
    demo()
