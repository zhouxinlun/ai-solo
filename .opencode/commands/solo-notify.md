---
description: Send messages (or commands) to the designated role through an iTerm2 session.
---
# /solo-notify

目标：调用本地脚本将消息发送到指定角色的 iTerm2 会话。

## 需要的参数（必填）
- role：PM | ARCH | BE | FE | QA
- text：要发送的文本（建议用引号包裹）

## 执行步骤（严格按顺序）
1. 校验参数合法性（role 必须在允许列表内，text 不能为空）。
2. 运行命令：
   - `./scripts/solo-notify.sh "<ROLE>" "<TEXT>"`
3. 输出脚本结果。

## 注意
- 需要本地 iTerm2 Python API 环境可用。
- 会话名需包含角色关键字（不区分大小写）。
