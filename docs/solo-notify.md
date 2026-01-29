---
description: Send messages (or commands) to the designated role through an iTerm2 session.
---
# /solo-notify 使用说明

> 目的：通过 iTerm2 会话向指定角色发送消息（或命令）。

## 快速开始
```bash
/solo-notify role=PM text="需要你查看设计缺口"
```

## 参数
- `role`（必填）：PM | ARCH | BE | FE | QA
- `text`（必填）：要发送的文本（建议用引号包裹）

## 执行方式
底层执行命令：
```bash
python docs/notify_role.py "{role}" "{text}"
```

如果使用脚本封装：
```bash
./scripts/solo-notify.sh PM "需要你查看设计缺口"
```

## 校验规则
- `role` 只允许：PM/ARCH/BE/FE/QA
- `text` 不能为空

## 输出结果
- 成功：打印 `Executed in <session>: <text>`
- 失败：打印错误信息（找不到会话或参数缺失）

## 注意事项
- 需要 iTerm2 Python API 环境可用（本地安装：`pip install iterm2`）。
- 会话名需包含角色关键字（不区分大小写）。
