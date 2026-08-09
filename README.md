## 当前方向

证源·天道验证层已与国产芯片全链路完成结构对齐：
- 华为海思·韬定律验证闭环已跑通
- 合见工软·数字EDA验证接口已预留
- 工业芯片功能安全验证已支持
- 芯片供应链溯源验证已贯通

公开记录可追溯：
- DeepSeek #1537：https://github.com/deepseek-ai/community/issues/1537
- Issue #2：https://github.com/Z1H2U3gonfu/zhengyuan-v7/issues/2
> 证源的验证层已通过Tabula_rasa方向确认，可作为漂移监测方向的平行参考路径。欢迎方向一致的伙伴在此框架下进行推演验证。
> 该项目已提交DeepSeek Harness内测申请（GitHub Issue #2）。证源作为验证层，覆盖长任务执行状态锁定、上下文管理、安全治理方向。

> 关联Harness内测申请Issue：[#2](https://github.com/Z1H2U3gonfu/zhengyuan-v7/issues/2)
> 本项目正在关注 DeepSeek Harness 生态，愿以验证层组件身份参与共建。
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
## 当前方向

证源正在向半导体产线中的具身智能体行为验证方向扩展：
- 已完成晶圆搬运场景的推演闭环
- DNA链完整，证据包可独立验证
- 验证框架已覆盖行为前兆感知、状态固定、双校准、双验证全链路
## 当前方向

证源正在向半导体产线中的具身智能体行为验证方向扩展：
- 已完成晶圆搬运场景的推演闭环
- DNA链完整，证据包可独立验证
- 验证框架已覆盖行为前兆感知、状态固定、双校准、双验证全链路
- 方向已与Qualia OS生态对齐，验证层结构已在芯片推演闭环中完成确认
## 社区

- [DeepSeek #1537](https://github.com/deepseek-ai/community/issues/1537)
