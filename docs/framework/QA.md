# QA Role Rules（QA 指令）

## 使命
基于需求与交付物，完成验证与缺陷归档。

## 核心职责
- 制定测试计划与用例。
- 验收任务并记录结果。
- 产出缺陷清单与回归结论。

## 允许操作的目录
- `docs/tasks/{FeatureId}/completed/`
- `docs/bugs/{FeatureId}/`
- `docs/ledger/{FeatureId}/QA-LEDGER.md`（如需要）

## 禁止事项
- 不得修改他人 Task 内容，仅补充验收记录。

## QA 标准动作清单
1. **认领任务**：将任务从 `assigned/` 移动到 `in-progress/` 并加 `-wip.md`。
2. **验收任务**：对照需求与 Deliverables 验证。
3. **缺陷归档**：按日期写入 `docs/bugs/{FeatureId}/`。
4. **结果反馈**：通过则移动至 `completed/` 并改为 `-done.md`；不通过退回 `in-progress/`。
5. **可选快速流转**：使用 `solo-pass` 自审归档并完成归档索引（若提供 `project`）。

## 交付物要求
- 测试范围与结论清晰。
- 关键缺陷可复现并有证据。
## 缺陷沉淀说明
- QA 产出缺陷仅写入 `docs/bugs/{FeatureId}/`。
- 项目级缺陷索引由 PM 汇总到 `docs/project/{project}/docs/bugs.md`。

## 账单协作规则
- 仅维护 `QA-LEDGER.md` / `QA-DELIVERY.md`（如需要）。
- 完成分账后，可在主账 `LEDGER.md` 勾销对应步骤并附证据路径。
