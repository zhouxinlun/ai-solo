# AI Solo Template

本项目是一个“提示词驱动的单人多角色协作模板”，把传统团队（PM/ARCH/BE/FE/QA）虚拟化为一组 AI 角色。开发者作为 Orchestrator，通过标准化 SOP 文件与命令，把需求、设计、实现、验收串成可追踪的闭环。

核心理念：
- 角色分工明确：每个角色只维护自己的分账与交付记录。
- 事实可追溯：所有结论必须有文件证据与路径。
- 目录即状态：任务流转只通过目录与文件名后缀体现。
- 单一权威：主账 LEDGER 为事实中心，DELIVERY 为执行计划。

## 目录概览
- 需求：`docs/requirements/{FeatureId}/`
- 设计：`docs/design/{FeatureId}/`
- 任务流转：`docs/tasks/{FeatureId}/{assigned|in-progress|completed|archived}/`
- 账单：`docs/ledger/{FeatureId}/`
- 缺陷：`docs/bugs/{FeatureId}/`（QA 证据）
- 项目沉淀：`docs/project/{project}/docs/`（PM 归档索引）

## 自定义命令（OpenCode）
OpenCode 的自定义命令放在：
```
.opencode/commands/
```
已提供命令：
- `/solo-start` 初始化规则与项目上下文
- `/solo-pick` 自动定位可执行任务
- `/solo-pass` 角色自审归档 + 自动流转
- `/solo-notify` 发送消息到指定角色会话

## iTerm2 多窗口协作与通知
本项目通过 iTerm2 多窗口模拟多角色运行，并用脚本发送消息：
```
python docs/notify_role.py "{role}" "{text}"
```
本地依赖（仅需一次）：
```
pip install iterm2
```
封装命令：
```
./scripts/solo-notify.sh PM "需要你查看设计缺口"
```

## 从需求到交付的标准流程
1. **PM 创建需求**
   - 生成 FeatureId，创建 `PM_REQUIREMENTS.md`。
   - 需求与原型 HTML 放入：
     - `docs/requirements/{FeatureId}/`
     - `docs/requirements/{FeatureId}/assets/`
   - 初始化 `LEDGER.md` 与 `DELIVERY.md`。

2. **ARCH 设计**
   - 领取任务后，将原型与素材复制到：
     - `docs/design/{FeatureId}/assets/`
   - 输出设计文档：
     - `docs/design/{FeatureId}/design-spec.md`
     - `docs/design/{FeatureId}/design-gap.md`

3. **BE/FE 实现**
   - 依据 `design-spec.md` 与设计 assets 实施。
   - 更新各自 `role-LEDGER.md` 与 `role-DELIVERY.md`。

4. **QA 验收**
   - 缺陷写入 `docs/bugs/{FeatureId}/`。
   - PM 在项目沉淀里记录缺陷索引。

5. **归档**
   - 任务进入 `archived/`，LEDGER/DELIVERY 标记完成。

## 快速使用步骤
1. 打开 OpenCode，执行 `/solo-start`。
2. PM 创建需求与输入材料（需求文档、HTML 原型）。
3. ARCH 领取设计任务，完成设计归档。
4. PM 分发 FE/BE 任务，完成实现。
5. QA 归档缺陷与验收。
6. 可选：使用 `/solo-pass` 跳过 PM 审核自审流转。
7. 多角色协作时，用 `/solo-notify` 发送消息给目标角色。

## 规则索引
规则入口：`docs/SPACE_INDEX.md`  
角色规则：`docs/framework/*.md`  
任务流转：`docs/tasks/README.md`
