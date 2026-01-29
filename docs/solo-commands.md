# Solo Commands 快速说明

面向协作者的上手说明，覆盖 `/solo-start`、`/solo-pick`、`/solo-pass`、`/solo-notify`。

## /solo-start
用途：初始化角色上下文与项目资料加载。

参数：
- `role`（可选）：PM | ARCH | BE | FE | QA（默认当前主代理角色）
- `feature_id`（可选）：已有需求时填写；否则自动扫描或由 PM 生成
- `prd_path`（可选）：PRD 路径（本地路径或文档链接）
- `design_assets`（可选）：原型/HTML 设计图路径，或 HTML 列表文件路径（建议存放到 `docs/requirements/{FeatureId}/assets/`）
- `project`（可选）：项目代号，对应 `docs/project/{project}/docs`
- `project_path`（可选）：存量项目根目录（仅生成索引，不复制源码）

示例：
```
/solo-start
/solo-start role=ARCH feature_id=2026-01-28-obs-download-test-b4e52f9a
/solo-start project=ai-solo project_path=docs/project/ai-solo
```

## /solo-pick
用途：未提供 FeatureId 时自动定位可执行任务或需求入口。

参数：
- `role`（可选）：PM | ARCH | BE | FE | QA
- `project`（可选）：项目代号（优先过滤）
- `auto_claim`（可选）：true/false，是否自动认领

示例：
```
/solo-pick
/solo-pick role=BE auto_claim=true
```

## /solo-pass
用途：角色自检通过后，跳过 PM 审核，自审归档并自动流转到下一角色。

参数：
- `feature_id`（必填）：当前 FeatureId
- `task_path`（必填）：当前任务文件路径（需在 `completed/` 且为 `-done.md`）
- `role`（可选）：PM | ARCH | BE | FE | QA
- `project`（可选）：项目代号（QA 归档索引用）
- `next`（可选）：指定下一角色

示例：
```
/solo-pass feature_id=2026-01-28-obs-download-test-b4e52f9a \
task_path=docs/tasks/2026-01-28-obs-download-test-b4e52f9a/completed/2026-01-29-ARCH-1a2b3c4d-done.md
```

## /solo-notify
用途：通过 iTerm2 会话向指定角色发送消息（或命令）。

参数：
- `role`（必填）：PM | ARCH | BE | FE | QA
- `text`（必填）：要发送的文本（建议用引号包裹）

前置依赖：
- 需要本地安装 iTerm2 Python API：
  - `pip install iterm2`

示例：
```
/solo-notify role=PM text="需要你查看设计缺口"
```

## 进一步阅读
- 详细流程：`docs/solo-start.md`、`docs/solo-pick.md`、`docs/solo-pass.md`、`docs/solo-notify.md`
