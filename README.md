# Interview Intel

> AI 驱动的面试准备助手 - 系统化分析公司、职位和简历，生成针对性的面试准备策略

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.0-green.svg)](https://github.com/leayn03/interview-intel)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-interview--intel-blue.svg)](https://github.com/leayn03/interview-intel)

## 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/leayn03/interview-intel.git
cd interview-intel

# 在 Claude Code 中加载技能
# 方式 1: 拖拽 interview-intel.skill 到 Claude Code
# 方式 2: 使用斜杠命令
/interview 面试公司 职位名称
```

### 使用示例

```
你: /interview 阿里云 AI产品经理

AI 将会:
1. 为你创建 companies/阿里云-AI产品经理-你的名字/ 文件夹
2. 询问 JD 和简历信息
3. 生成 5 个完整的面试准备文件:
   - 01 公司情报简报
   - 02 简历-JD 匹配分析
   - 03 面试准备策略
   - 04 破冰文案库
   - 05 最终综合报告
```

## 核心特性

### 🤖 AI 驱动的分析生成

基于你的简历和目标职位 JD，AI 自动生成：

| 生成文件 | 内容说明 |
|---------|----------|
| `01_company_intel_brief.md` | 公司背景、产品分析、竞争格局、技术栈 |
| `02_resume_jd_matching.md` | 简历与 JD 的逐项匹配、差距分析、应对策略 |
| `03_interview_prep_report.md` | HR/业务/高管面试准备、STAR 案例库、技术问答 |
| `04_icebreaker_messages.md` | 自我介绍模板、反向提问、场景化开场 |
| `05_final_analysis_report.md` | 综合评估、成功概率、行动计划 |

### ⚡ 专业化流水线团队 (并行加速)

**两种使用方式**:

**方式 1: 自然语言（推荐）**
```
你: "帮我准备阿里云AI产品经理的面试，使用专业团队模式"
```

**方式 2: 命令行**
```bash
cd interview-intel
python scripts/pipeline_team.py \
  --company "目标公司" \
  --role "目标职位" \
  --candidate "你的名字" \
  --jd "path/to/jd.txt" \
  --resume "path/to/resume.pdf"
```

**5人专业团队并行工作**:
```
阶段1 (并行): Teammate A + B → ~45s
    ├─ 公司研究员 → 01 公司情报简报
    └─ 简历分析师 → 02 简历-JD 匹配

阶段2 (并行): Teammate C + D → ~60s
    ├─ 面试教练 → 03 面试准备策略
    └─ 文案专家 → 04 破冰文案库

阶段3 (串行): Teammate E → ~30s
    └─ 战略顾问 → 05 最终综合报告

总耗时: ~135s (加速 1.5x)
```

### 🗂️ 智能文件组织

```
InterviewIntel/
├── companies/
│   └── 阿里云-AI产品经理-张三/       # 自动创建
│       ├── 01_company_intel_brief.md
│       ├── 02_resume_jd_matching.md
│       ├── 03_interview_prep_report.md
│       ├── 04_icebreaker_messages.md
│       └── 05_final_analysis_report.md
├── resumes/                           # 你的简历库
│   └── 你的简历.pdf
└── interview-intel.skill              # Claude 技能包
```

## 工作原理

### AI 如何为你准备面试

1. **理解 JD**: AI 分析职位描述，提取关键要求
2. **研究公司**: 基于公开信息生成公司情报简报
3. **简历匹配**: 逐项对比你的简历与 JD 要求
4. **生成策略**: 针对性准备面试话术和案例
5. **文案优化**: 提供自我介绍和反向提问模板

### 事实验证协议 ⭐

- ✅ 所有分析严格基于你的简历真实数据
- ✅ 不编造不存在的工作经验或技能
- ✅ 差距分析诚实指出需要补充的领域
- ✅ 案例准备基于真实项目经历

## 技能结构

```
interview-intel/
├── SKILL.md                    # 主技能文件（Prompt 定义）
├── pipeline_config.json        # 流水线团队配置
├── scripts/
│   ├── pipeline_team.py        # 并行生成器（5人团队）
│   └── test_pipeline_team.py   # 测试脚本
└── references/
    ├── company_research_guide.md    # 公司研究框架
    ├── jd_analysis_framework.md     # JD 分析框架
    └── resume_jd_mapping.md         # 简历匹配方法
```

## 常见问题

### Q: 需要提供什么信息？

A: 需要准备：
- 目标公司和职位名称
- 职位描述 (JD) 文本
- 你的个人简历（PDF 或文本）

### Q: 生成的文件准确吗？

A: AI 基于你提供的真实信息生成，遵循事实验证协议：
- 优点：来自简历明确陈述的信息
- 差距：基于 JD 与简历对比的客观分析
- 不编造任何简历中不存在的内容

### Q: 支持哪些类型的面试？

A: 适用于技术类职位面试，包括：
- 软件工程师（前后端、全栈、移动端）
- 产品经理（AI 产品、技术产品）
- 技术负责人/架构师
- 数据科学家/分析师

### Q: 多久能生成完整准备材料？

A: 使用专业化流水线团队模式：
- 框架生成：<1 秒
- 完整内容：约 5-10 分钟（取决于复杂度）

## 文档

- [完整功能说明](interview-intel/SKILL.md) - 详细的技能定义
- [事实验证协议](.claude/FACT_VERIFICATION_PROTOCOL.md) - 数据真实性保证

## 开源协议

MIT License - 详见 [LICENSE](LICENSE)

---

**版本**: v1.1.0 - 专业化流水线团队模式
**仓库**: https://github.com/leayn03/interview-intel
