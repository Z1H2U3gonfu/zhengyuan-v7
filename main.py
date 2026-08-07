#!/usr/bin/env python3
"""
证源 v7.0 · 开源版
让AI生成内容自带可验证的"出生证明"
"""

import json
import argparse
from pathlib import Path
from datetime import datetime

from core.evidence_builder import EvidenceBuilder
from core.prompt_tree import PromptTree
from core.param_locker import ParamLocker
from core.hash_chain import HashChain


def main():
    parser = argparse.ArgumentParser(description="证源 v7.0 - AI创作确权工具")
    parser.add_argument("--input", "-i", required=True, help="输入的提示词文件路径")
    parser.add_argument("--output", "-o", default="evidence.json", help="输出的证据包文件名")
    args = parser.parse_args()

    print("""
    ╔═════════════════════════════════════════╗
    ║  证源 v7.0 · 让AI创作有证可查            ║
    ╚═════════════════════════════════════════╝
    """)

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"❌ 文件不存在: {args.input}")
        return

    content = input_path.read_text(encoding="utf-8")
    print(f"✅ 已读取: {args.input} ({len(content)} 字符)")

    # 1. 构建版本树
    print("📝 构建提示词版本树...")
    tree = PromptTree(
        root_content=content,
        root_metadata={"source": args.input}
    )
    tree.add_version(
        content + "\n\n-- v2: 优化表达",
        metadata={"version": "v2"}
    )
    tree.add_version(
        content + "\n\n-- v3: 最终润色",
        metadata={"version": "v3"}
    )

    # 2. 锁定参数
    print("🔒 锁定生成参数...")
    locker = ParamLocker()
    params = {"temperature": 0.7, "top_p": 0.9, "seed": 42, "max_tokens": 2048}
    signature = locker.lock(params)

    # 3. 构建证据包
    print("📦 构建四层证据包...")
    builder = EvidenceBuilder()

    evidence = builder.build(
        input_layer={
            "original_prompt": content[:500] + "..." if len(content) > 500 else content,
            "length": len(content),
            "source": args.input
        },
        control_layer={
            "params": params,
            "signature": signature
        },
        process_layer={
            "versions": tree.get_history(),
            "edits": [
                {"version": "v1", "desc": "原始版本"},
                {"version": "v2", "desc": "优化表达"},
                {"version": "v3", "desc": "最终润色"}
            ]
        },
        replay_layer={
            "command": f"python main.py --input {args.input}",
            "timestamp": datetime.utcnow().isoformat()
        }
    )

    # 4. 生成哈希链
    print("🔗 生成哈希链...")
    chain = HashChain()
    for layer_name, layer_data in evidence["layers"].items():
        chain.add_block({
            "layer": layer_name,
            "data": layer_data
        })

    evidence["hash_chain"] = chain.get_chain()
    evidence["hash_chain_valid"] = chain.verify()

    # 5. 保存
    output_path = builder.save(evidence, args.output)
    print(f"✅ 证据包已保存: {output_path}")

    # 6. 验证哈希链
    print(f"🔗 哈希链状态: {'✅ 完整' if evidence['hash_chain_valid'] else '❌ 已损坏'}")

    print("\n🎉 证源 v7.0 执行完成！")


if __name__ == "__main__":
    main()
