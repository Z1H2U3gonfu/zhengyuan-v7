# 证源 v7.0

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 让AI生成内容自带可验证的"出生证明"

## 什么是证源？

证源是一个记录AI创作全过程的框架。从输入提示词、参数调整、版本迭代到最终输出，每一步都被记录为可独立验证的证据包。

## v7.0 核心能力

- **四层证据包结构**：输入层 / 控制层 / 加工层 / 复现层
- **提示词版本树**：记录每一次修改的演变路径
- **参数锁定**：锁定 temperature、top_p 等关键参数
- **SHA-256 哈希链**：确保记录不可篡改

## 快速开始

```bash
git clone https://github.com/Z1H2U3gonfu/zhengyuan-v7
cd zhengyuan-v7
pip install -r requirements.txt
echo "写一首关于秋天的诗" > prompt.txt
python main.py --input prompt.txt --output evidence.json
## 许可证

MIT License © 2026 Zhu Junlin

## 版本演进

- **v7.0**（开源版）：四层证据包 + 版本树 + 参数锁定 + 哈希链
- **v11**：内容平台溯源方向
- **v16**：国家AI安全合规方向
- **v25**：具身体验证方向（DNA刻入已接入）

## 社区

- [DeepSeek #1537](https://github.com/deepseek-ai/community/issues/1537)
