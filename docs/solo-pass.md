---
description: After the user passes the self-check, the PM review is skipped and the current task is automatically archived and transferred to the next role.
---
# /solo-pass 使用说明

> 目的：在用户自检通过后，跳过 PM 审核，自动完成当前任务归档并流转到下一角色。

## 快速开始
```bash
/solo-pass
```

## 参数
- `role`（可选）：PM | ARCH | BE | FE | QA。默认当前主代理角色。
- `feature_id`（必填）：当前 FeatureId。
- `task_path`（必填）：当前任务文件路径（需在 `completed/` 且带 `-done.md`）。
- `project`（可选）：项目代号，用于 QA 归档到 `docs/project/{project}/docs/bugs.md`。
- `next`（可选）：指定下一角色，默认按标准流水线（ARCH -> BE/FE -> QA -> 归档）。

## 自检清单（必须通过）
- Deliverables 完整（任务内清单已填写）。
- 角色分账已更新（`role-LEDGER.md` / `role-DELIVERY.md`）。
- 证据路径存在（设计/代码/测试/缺陷路径可访问）。
- 依赖条件满足（`DependsOn` 对应步骤已完成）。

## 执行流程
1. 读取规则索引与核心规则：
   - `docs/SPACE_INDEX.md`
   - `docs/framework/core_rules.md`
2. 加载当前角色规则与任务流转规则：
   - `docs/framework/<ROLE>.md`
   - `docs/tasks/README.md`
3. 校验当前任务：
   - `task_path` 必须位于 `docs/tasks/{FeatureId}/completed/` 且为 `-done.md`。
   - TaskId 必须等于文件基础名（无 `-done.md` 后缀）。
4. 自检通过后，执行“自审归档”：
   - 将任务移动到 `docs/tasks/{FeatureId}/archived/` 并去掉 `-done.md` 后缀。
   - 在任务内记录状态变更（日期 + `solo-pass`）。
5. 更新账单与执行计划：
   - 在 `role-LEDGER.md` 与 `role-DELIVERY.md` 标记完成。
   - 在 `LEDGER.md` 勾销对应步骤并附证据路径（允许角色在完成分账后勾销）。
   - 在 `DELIVERY.md` 将对应 StepId 标记为 DONE。
6. 自动流转到下一角色（默认流水线）：
   - ARCH：创建 BE/FE Task 到 `assigned/`，并在 `DELIVERY.md` 填写 TaskId。
   - BE/FE：若 BE 与 FE 均已完成，创建 QA Task 到 `assigned/`。
   - QA：归档完成，若提供 `project`，更新 `docs/project/{project}/docs/bugs.md`。

## 自动流转细则
- **ARCH -> BE/FE**
  - 前提：`docs/design/{FeatureId}/design-spec.md` 已存在。
  - 动作：从模板创建 BE/FE Task（可多个实例），放入 `docs/tasks/{FeatureId}/assigned/`。
- **BE/FE -> QA**
  - 前提：所有 BE 与 FE 任务已完成（`completed/` 或 `archived/`）。
  - 动作：从模板创建 QA Task 到 `assigned/`，更新 `DELIVERY.md`。
- **QA -> 归档**
  - 前提：缺陷已写入 `docs/bugs/{FeatureId}/`。
  - 动作：如提供 `project`，在 `docs/project/{project}/docs/bugs.md` 追加摘要索引。

## 输出要求
- 列出本次归档的任务路径与变更记录。
- 明确是否已触发下一角色任务，若未触发说明原因。
- 给出下一步建议（1-3 条）。

## 注意事项
- 未经用户明确确认不得执行 `solo-pass`。
- 不修改 `docs/_templates/`。
- 不跨项目写入任何路径。
