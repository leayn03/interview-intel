# Changelog

All notable changes to Interview Intel will be documented in this file.

## [v5.0] - 2026-01-21

### ⭐ 新增：一键执行工作流

- **all_in_one.py**: 新增主工作流脚本，一条命令生成所有面试准备材料
  - 输入：JD + 简历版本
  - 输出：公司背景、JD 分析、简历匹配、面试策略、破冰文案
  - 自动化执行 6 个步骤，无需手动运行多个脚本

### 🎯 使用方式

```bash
python scripts/all_in_one.py execute \
  --base-path ~/InterviewIntel \
  --company "公司名称" \
  --role "职位名称" \
  --jd-file jd.txt \
  --resume-version v1.0
```

### 📝 文档更新

- SKILL.md：添加"⚡ Quick Start: One-Click Execution"章节
- QUICK_START.md：新增快速开始指南，包含使用示例和场景
- 更新所有脚本说明，突出 all_in_one.py 为推荐方式

### 🔧 技术细节

- all_in_one.py 编排所有子脚本按顺序执行
- 自动处理文件夹创建、JD 保存、关键词提取
- 生成 workflow_metadata.json 记录执行元数据
- 支持可选参数：resume-file, achievement, years, insight

---

## [v4.0] - 2026-01-21

### 🆕 核心功能

三大新增脚本，全面提升求职博弈能力：

#### 1. resume_optimizer.py - 简历-JD 智能匹配

- **JD 深度分析**：提取硬性要求、核心能力、隐藏洞察（"他们真正想要什么"）
- **STAR 改写建议**：提供结构化改写建议（Situation-Task-Action-Result）
- **关键词高亮**：识别简历和 JD 之间的匹配关键词
- **匹配度评分**：量化简历-JD 对齐程度

#### 2. interview_strategy.py - 面试攻防策略生成

- **第一轮（HR筛选）**：风险识别 + 防御脚本
  - 常见风险：频繁跳槽、职业空窗期、跨行业转型
  - 提供好答案 vs 坏答案对比
- **第二轮（业务负责人）**：预测问题 + 杀手案例模板
  - 高频问题预测（技术深度、项目复杂度、团队协作）
  - 杀手案例准备（STAR 框架 + 量化成果）
- **第三轮（高管面试）**：战略问题 + 商业思维
  - 战略性问题准备
  - 宏观话题（行业趋势、产品方向、团队建设）

#### 3. icebreaker_generator.py - 破冰文案生成

- **策略 A（专业匹配）**：适合 HR 和正规流程
  - 风格：专业、简洁、结果导向
  - 结构：挂钩（JD关键词）+ 证明（成就）+ 行动（查看简历）
- **策略 B（业务洞察）**：适合业务负责人和创业团队
  - 风格：温暖、有洞察、平等交流
  - 结构：挂钩（行业洞察）+ 证明（类似场景）+ 行动（探讨挑战）
- **使用指南**：发送时机、禁忌词汇、加分技巧

### 📁 文件组织优化

- **统一目录结构**：所有公司材料迁移到 `companies/` 目录
- **更新 setup_company_folder.py**：自动在 companies/ 下创建公司文件夹
- **向后兼容**：已有公司文件夹（MiniMax, SIF）已迁移

### 📄 新增模板

- **star_rewrite_template.md**：STAR 框架改写指南
  - 模板 1：产品/项目经历
  - 模板 2：技术优化经历
  - 模板 3：跨团队协作经历
  - 改写检查清单

### 🎯 核心理念

- **精准匹配**：基于 JD 关键词对齐，不虚构
- **STAR 框架**：所有经历改写遵循 Situation-Task-Action-Result 结构
- **透明洞察**：揭示 JD 背后的真实需求
- **招聘博弈**：理解 HR、业务、高管的不同考察点

### 📊 实际案例

- **京东物流运输产品经理**：完整分析示例
  - 匹配度：60%（中等）
  - 最大硬伤：缺乏物流行业经验
  - 提供详细补课策略和 STAR 改写示例
  - 评估成功概率：简历通过率 30-40%

---

## [v3.0] - 之前版本

- Resume version management
- Interview tracking
- Analytics generation
- Company folder structure
- JD keyword extraction

---

## 版本说明

- **v1.0.0**：首个公开版本，完整功能集 + 事实验证协议
- 这是 Interview Intel 的第一个正式发布版本

**推荐版本**：v1.0.0（当前版本）
