# Interview Intel Skill

这是一个用于技术面试准备的 Claude 技能，帮助系统性地分析公司、职位描述和简历，生成针对性的面试准备策略。

## 功能特性

### 🗂️ 自动文件组织
- **按公司组织**: 为每个目标公司创建独立文件夹
- **结构化存储**: 自动分类原始数据、分析报告、面试笔记
- **多角色支持**: 同一公司的不同职位分别追踪
- **一致性命名**: 智能文件命名，避免冲突

### 1. 公司情报收集
- 产品和商业模式理解
- 近期发展和战略方向
- 技术栈和工程文化
- 团队结构和关键领导者

### 2. 职位描述分析
- 技术技能分类（必需 vs 加分项）
- 经验要求和级别
- 软技能和文化匹配指标
- 职责范围和影响力预期
- **自动关键词提取**: Python 脚本自动化 JD 分析

### 3. 简历-JD 匹配映射
- 直接匹配（强证据）
- 相邻匹配（可迁移经验）
- 差距分析（需要补充或学习的领域）
- 关键故事准备

### 4. 简历版本管理 ⭐ 新增
- **完整文件管理**: 存储和追踪完整的 PDF/Word 简历文件
- **版本控制**: 管理多个简历版本，每个针对不同职位类型
- **智能推荐**: 根据 JD 要求推荐最佳简历版本
- **公司定制**: 为特定公司和职位定制简历
- **版本比较**: 对比不同版本的差异
- **使用追踪**: 追踪哪个版本用于哪些申请

### 5. 面试进度追踪 ⭐ 新增
- **结构化追踪**: JSON 格式记录申请和面试全流程
- **轮次管理**: 详细记录每一轮面试信息
- **反馈收集**: 记录面试官、问题、反馈、难度、信心
- **时间线可视化**: 生成申请到 offer 的完整时间线
- **简历关联**: 追踪每次申请使用的简历版本
- **决策记录**: 记录最终结果和 offer 详情

### 6. 统计分析与可视化 ⭐ 新增
- **全局统计**: 总申请数、响应率、面试通过率、offer 率
- **简历效果分析**: 不同简历版本的表现对比
- **职位类型分析**: 不同职位的成功率统计
- **面试表现追踪**: 难度、信心、通过率等指标
- **CSV 导出**: 导出数据用于 Excel 分析
- **HTML 仪表板**: 交互式图表和可视化（基于 Chart.js）

### 7. 综合面试准备报告
- 公司情报摘要
- JD 要求细分
- 简历匹配度和差距
- 准备优先级
- 故事库（STAR 格式）
- 需要提问的问题
- 核心谈话要点

## 安装方法

### 在 Claude Code 中安装

```bash
# 方法 1: 从本地目录安装
claude plugin install interview-intel.skill

# 方法 2: 如果你将此技能添加到了插件市场
/plugin install interview-intel@your-marketplace
```

### 在 Claude.ai 中使用

1. 访问 Claude.ai
2. 上传 `interview-intel.skill` 文件
3. 开始使用技能

## 使用示例

### 完整的面试准备流程

```
用户: "帮我准备 DataCorp 的高级后端工程师面试。这是 JD: [JD 文本]。这是我的简历: [简历]。"

技能将会:
1. 提取并分析 JD
2. 研究 DataCorp 公司情报
3. 将你的简历映射到 JD 要求
4. 生成综合面试准备报告
5. 突出前 3 个优势和前 2 个差距
6. 提供 5 个关键故事准备
7. 建议优先学习主题
```

### 快速 JD 分析

```
用户: "你能分析这个职位描述并告诉我应该重点关注什么吗？[JD 文本]"

技能将会:
1. 在 JD 上运行 extract_jd_keywords.py
2. 使用框架进行详细分析
3. 按优先级分类要求
4. 输出结构化 JD 分析
5. 建议准备优先级
```

### 公司研究

```
用户: "下周我要去 TechStartup 面试。我应该了解他们什么？"

技能将会:
1. 使用研究指南研究公司
2. 收集产品、业务、文化信息
3. 查找近期发展
4. 确定面试相关性
5. 输出公司情报简报
```

## 技能结构

### 技能源代码
```
interview-intel/
├── SKILL.md                               # 主技能文件
├── scripts/
│   ├── setup_company_folder.py           # 文件夹结构创建脚本
│   ├── extract_jd_keywords.py            # JD 关键词提取脚本
│   ├── resume_manager.py                  # 简历版本管理 ⭐ 新增
│   ├── interview_tracker.py               # 面试追踪 ⭐ 新增
│   └── analytics_generator.py             # 统计分析 ⭐ 新增
├── references/
│   ├── company_research_guide.md         # 公司研究框架
│   ├── jd_analysis_framework.md          # JD 分析框架
│   └── resume_jd_mapping.md              # 简历映射方法
└── assets/
    ├── company_intel_brief_template.md   # 公司情报模板
    ├── interview_prep_report_template.md # 面试准备报告模板
    ├── resume_changelog_template.md       # 简历变更日志 ⭐ 新增
    └── interview_round_notes_template.md  # 面试笔记模板 ⭐ 新增
```

### 生成的文件组织结构 ⭐ 增强版
```
InterviewIntel/                           # 你的工作目录
├── resumes/                              # 全局简历版本库 ⭐ 新增
│   ├── master_resume_v1.0.pdf
│   ├── master_resume_v2.0.pdf
│   ├── resume_registry.json             # 版本注册表
│   └── CHANGELOG.md                     # 变更记录
├── SIF/                                  # 公司文件夹（自动创建）
│   ├── company_intel_brief.md           # 公司情报报告
│   ├── jd_analysis_Backend_Engineer.md  # JD 分析
│   ├── resume_mapping_Backend_Engineer.md # 简历匹配
│   ├── interview_prep_Backend_Engineer.md # 综合准备报告
│   ├── raw_data/                        # 原始数据
│   │   ├── jd_original_Backend_Engineer.txt
│   │   └── jd_keywords_Backend_Engineer.txt
│   ├── resumes/                         # 公司定制简历 ⭐ 新增
│   │   └── resume_Backend_Engineer_v1.pdf
│   ├── interviews/                      # 面试记录 ⭐ 新增
│   │   ├── tracking.json               # 结构化追踪数据
│   │   ├── round_1_notes.md            # 每轮详细笔记
│   │   └── round_2_notes.md
│   ├── notes.md                         # 面试笔记
│   └── README.md                        # 文件夹说明
├── Google/                              # 另一家公司
│   └── ...
├── .analytics/                          # 全局统计 ⭐ 新增
│   ├── global_stats.json               # 汇总统计
│   └── exports/
│       ├── interview_data.csv          # CSV 导出
│       └── dashboard.html              # HTML 仪表板
└── interview-intel.skill                # 技能包文件
```

## 工具使用

### 1. 文件夹结构创建脚本 ⭐ 新增

**在开始任何分析前，先创建文件夹结构：**

```bash
# 创建公司文件夹（不指定职位）
python scripts/setup_company_folder.py ~/InterviewIntel "SIF"

# 创建公司+职位文件夹（推荐）
python scripts/setup_company_folder.py ~/InterviewIntel "SIF" "Backend Engineer"

# 示例输出
✅ Created company folder structure for: SIF
📁 Company Folder: ~/InterviewIntel/SIF
📁 Raw Data Folder: ~/InterviewIntel/SIF/raw_data
📄 Suggested file paths:
  - Company Intel: ~/InterviewIntel/SIF/company_intel_brief.md
  - JD Analysis: ~/InterviewIntel/SIF/jd_analysis_Backend_Engineer.md
  ...
```

**脚本功能：**
- 自动创建结构化文件夹
- 生成 README.md 和 notes.md 模板
- 输出 JSON 格式的文件路径（方便编程使用）
- 智能文件命名（处理特殊字符和空格）

### 2. JD 关键词提取脚本

```bash
# 从文件读取
python scripts/extract_jd_keywords.py jd_file.txt

# 从标准输入读取
cat jd.txt | python scripts/extract_jd_keywords.py

# 或直接粘贴
python scripts/extract_jd_keywords.py
# (粘贴 JD 文本，然后按 Ctrl+D)
```

**脚本会自动提取：**
- 技术关键词（按类别分类）
- 经验要求
- 软技能
- 要求强度（必需 vs 优先）
- 关键短语

### 3. 简历版本管理 ⭐ 新增

```bash
# 创建新的主版本
python scripts/resume_manager.py create --file ~/Documents/resume.pdf --version v1.0 --desc "通用后端简历" --target "Backend,Full-stack" --skills "Python,Docker,AWS"

# 列出所有版本
python scripts/resume_manager.py list

# 按目标职位筛选
python scripts/resume_manager.py list --filter Backend

# 为特定公司定制简历
python scripts/resume_manager.py tailor --base v1.0 --company SIF --role "Backend Engineer" --output ~/InterviewIntel/SIF/resumes/

# 比较两个版本
python scripts/resume_manager.py compare --v1 v1.0 --v2 v2.0

# 根据 JD 推荐版本
python scripts/resume_manager.py recommend --target "Backend Engineer" --requirements "Python,Docker,Kubernetes,AWS"

# 查看使用报告
python scripts/resume_manager.py report --version v1.0
```

**功能说明：**
- 存储完整的 PDF/Word 简历文件
- 自动计算文件哈希确保完整性
- 追踪版本元数据：目标职位、关键技能、创建日期
- 为公司定制时自动复制文件到公司文件夹
- 支持版本比较和智能推荐
- 生成简历使用统计报告

### 4. 面试追踪 ⭐ 新增

```bash
# 初始化追踪（提交申请时）
python scripts/interview_tracker.py init --company-path ~/InterviewIntel/SIF --company SIF --role "Backend Engineer" --resume v2.0

# 添加面试轮次
python scripts/interview_tracker.py add-round --company-path ~/InterviewIntel/SIF --round 1 --name "Phone Screen" --date 2026-01-25 --time "10:00" --interviewer "John Doe" --title "Senior Engineer"

# 更新面试结果
python scripts/interview_tracker.py update --company-path ~/InterviewIntel/SIF --round 1 --status completed --result passed --difficulty 3 --confidence 4

# 查看当前状态
python scripts/interview_tracker.py status --company-path ~/InterviewIntel/SIF

# 生成时间线
python scripts/interview_tracker.py timeline --company-path ~/InterviewIntel/SIF
```

**功能说明：**
- JSON 格式存储结构化面试数据
- 追踪每轮面试的详细信息
- 记录面试官、时间、平台、焦点领域
- 记录难度、信心、反馈
- 追踪简历版本关联
- 生成可视化时间线

### 5. 统计分析 ⭐ 新增

```bash
# 生成全局统计
python scripts/analytics_generator.py generate --scope global

# 生成特定公司统计
python scripts/analytics_generator.py generate --scope company --company SIF

# 导出 CSV 数据
python scripts/analytics_generator.py export --format csv --output interview_data.csv

# 生成 HTML 仪表板
python scripts/analytics_generator.py dashboard --output dashboard.html
```

**功能说明：**
- 跨所有公司聚合统计数据
- 计算响应率、面试通过率、offer 率
- 分析不同简历版本的表现
- 按职位类型分析成功率
- 导出 CSV 用于 Excel 分析
- 生成交互式 HTML 仪表板（Chart.js）
- 自动扫描所有公司文件夹

## 最佳实践

### 文件组织 ⭐ 新的工作流程
1. **总是先创建文件夹**: 使用 `setup_company_folder.py` 创建结构
2. **保存所有输出**: 将所有分析报告保存到对应的公司文件夹
3. **原始数据存档**: JD 原文和提取结果保存到 `raw_data/`
4. **追踪多职位**: 同一公司不同职位使用不同文件名后缀
5. **更新笔记**: 面试后及时更新 `notes.md`

### 分析技巧
1. **公司情报收集**: 从公司网站、博客和 LinkedIn 开始
2. **JD 分析**: 注意重复提到的内容（真正的优先级）
3. **简历映射**: 诚实评估匹配强度
4. **故事准备**: 使用 STAR 格式（情境、任务、行动、结果）
5. **持续更新**: 随着了解的深入更新分析

## 📚 文档

- [用户配置指南](USER_SETUP_GUIDE.md) - 新手快速上手
- [常见问题](FAQ.md) - 24个问题详细解答
- [分享指南](SHARE_GUIDE.md) - 如何分享给他人
- [完整文档](interview-intel/SKILL_V6.md) - 全面功能说明

## 🆘 支持

如有问题或改进建议：

- 📖 查看 [FAQ.md](FAQ.md)
- 💬 提交 [GitHub Issue](https://github.com/your-repo/InterviewIntel/issues)
- 📧 联系邮箱: <support@example.com>

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源协议。

**简而言之**：你可以自由使用、修改、分发本项目，包括商业用途，只需保留原始许可证声明。

---

**创建日期**: 2026-01-21
**版本**: v1.0.0 - 首个公开版本，完整功能集 + 事实验证协议 ⭐⭐⭐
**最后更新**: 2026-02-06 - 添加用户配置体系和 MIT License
