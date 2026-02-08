# Interview Intel - v6.2

## 技能描述

综合求职策略系统,为候选人提供从公司调研到面试准备的完整解决方案。**v6.2 核心升级**:修复简历读取问题,完善一键完成方案,自动安装依赖,优化用户体验。

**适用场景**:
- 分析公司背景和业务信息
- 匹配简历与 JD 要求
- 生成面试准备策略和话术
- 创建破冰开场白
- 输出完整分析报告和行动计划

---

## 🎯 核心能力

### 1. 标准化输出结构

每个公司/职位自动生成 **5 个标准文件**:

#### 文件 1: 公司背景业务信息 (`01_company_intel_brief.md`)
- **核心信息速览**: 关键数据一页纸
- **公司背景**: 发展历程、融资上市、行业地位
- **业务模式**: B+C双轮驱动、收入结构、核心产品
- **竞争格局**: 主要竞争对手、差异化优势
- **职位深度分析**: 职位描述解读、要求匹配、面试切入点
- **核心洞察与策略**: 公司诉求、风险应对

#### 文件 2: 简历分析和匹配 (`02_resume_jd_matching.md`)
- **匹配度总览**: 综合评分、核心优势、待提升点
- **逐项匹配分析**: 每个JD要求的详细匹配分析
- **加分项匹配**: 所有加分项的匹配情况
- **待提升点应对**: 针对每个短板的应对策略和话术
- **核心竞争力总结**: 面试中需要突出的核心能力

#### 文件 3: 面试准备报告 (`03_interview_prep_report.md`)
- **HR面试**: 自我介绍、离职原因、职业规划、薪资策略
- **业务面试**: CodeLink项目详解、RAG技术理解、优化经验
- **高管面试**: 行业洞察、优劣势分析、3-6个月规划
- **技术面试**(可选): 模型评估、RAG vs Fine-tuning
- **面试准备清单**: 完整的准备时间表

#### 文件 4: 破冰文案 (`04_icebreaker_messages.md`)
- **通用开场白**: 30秒/1分钟/2分钟版本
- **针对不同面试官**: HR/产品负责人/高管
- **针对不同场景**: 面试官自我介绍后、直接提问、为什么选择MiniMax
- **针对不同风格**: 专业正式型、亲和自然型、数据驱动型
- **针对特殊情况**: 时间紧张、技术背景、业务背景
- **破冰技巧**: 注意事项和使用建议

#### 文件 5: 最终分析报告 (`05_final_analysis_report.md`)
- **综合评估**: 优势总结、待提升点、应对策略
- **核心竞争力定位**: 三大能力深度分析
- **面试成功要素**: 展示了解、证明匹配、展示学习
- **风险评估**: 高风险问题及应对策略
- **面试准备清单**: 详细的行动计划
- **薪资谈判策略**: 原则和话术

---

## ⚠️ 重要说明

**v6.2 最新状态**:

- ✅ **依赖自动安装**: 自动安装 pdfplumber 用于读取 PDF 简历
- ✅ **简历读取优化**: 支持从 resumes/ 目录自动查找简历
- ✅ **一键完成方案**: 配合 Claude Code 实现全自动化
  - 自动读取简历提取经历
  - 自动搜索公司最新信息
  - 主动询问缺失信息
  - 生成 100% 完成的面试准备包
- ✅ **统一脚本**: `all_in_one_v1.0.0.py` 集成所有内容生成逻辑

**两种使用方式**:

1. **配合 Claude Code（最推荐）**: 一键完成所有工作，包括框架生成和内容填充
2. **手动使用脚本**: 生成框架后手动补充内容

---

## 🚀 使用方式

### 方式 1: 配合 Claude Code 一键完成(最推荐)⭐⭐⭐

**适用场景**: 使用 Claude Code，希望**一键完成所有工作**

#### 完整工作流程:

**第1步: 向 Claude Code 提供信息**

```
我想应聘 MiniMax 的 B端大模型产品经理职位

JD: [粘贴 JD 内容]

我的简历在 InterviewIntel/resumes/王蕾-AI 产品经理V1.0.pdf

请帮我一键生成完整的面试准备包。
```

**第2步: Claude Code 自动执行**

Claude Code 会自动完成以下工作:

1. **安装依赖**(如需要)
   - 自动安装 pdfplumber 用于读取 PDF 简历

2. **读取简历提取信息**
   - 从 resumes/ 目录读取你的 PDF 简历
   - 提取核心工作经历和成就

3. **补充公司和行业信息**
   - 自动搜索公司最新信息(上市、融资、产品)
   - 获取竞争对手和行业趋势

4. **生成 5 个完整的 Markdown 文件**
   - 填充所有内容,生成完整的 STAR 案例
   - 生成针对性的面试话术
   - 生成匹配度分析

**第3步: 输出完整文件**

生成 5 个 100% 完成的文件,保存在 `companies/[公司名]/` 目录:
- ✅ `01_company_intel_brief.md`
- ✅ `02_resume_jd_matching.md`
- ✅ `03_interview_prep_report.md`
- ✅ `04_icebreaker_messages.md`
- ✅ `05_final_analysis_report.md`

#### 提示词模板:

**模板 1: 基础使用**

```
我想应聘 [公司名] 的 [职位名称]

JD: [粘贴 JD 内容]

我的简历在 InterviewIntel/resumes/王蕾-AI 产品经理V1.0.pdf

请帮我一键生成完整的面试准备包。
```

**模板 2: 提供更多信息**

```
我想应聘 MiniMax 的 B端大模型产品经理职位

公司: MiniMax
职位: B端大模型产品经理
JD: [粘贴 JD 内容]
简历: InterviewIntel/resumes/王蕾-AI 产品经理V1.0.pdf
行业: AI大模型
关键词: AI产品,大模型,ToB,开放平台
工作年限: 6年
核心成就: 主导AI产品从0到1,用户增长300%

请帮我生成完整的面试准备包。
```

**模板 3: 使用外部简历**

```
我想应聘某公司的产品经理职位

公司: [公司名]
职位: [职位名称]
JD: [粘贴 JD 内容]
简历: /path/to/my/resume.pdf
项目路径: /Users/leayn/Documents/PythonProject/Hackthon/InterviewIntel

请帮我生成完整的面试准备包。
```

#### 优势:

- ✅ **真正的一键完成**: 从框架到内容填充,全部自动化
- ✅ **自动安装依赖**: 首次使用自动安装 pdfplumber
- ✅ **主动询问**: 遇到信息不足会主动询问
- ✅ **真实数据**: 基于你的简历和最新公司信息
- ✅ **个性化定制**: 每个内容都是针对你定制的

---

### 方式 2: 使用统一脚本生成框架(传统方式)

使用 `all_in_one_v1.0.0.py` 生成框架后手动补充内容:

```bash
cd /Users/leayn/Documents/PythonProject/Hackthon/InterviewIntel/interview-intel
python scripts/all_in_one_v1.0.0.py \
  --base-path "/Users/leayn/Documents/PythonProject/Hackthon/InterviewIntel" \
  --company "MiniMax" \
  --role "B端大模型产品经理" \
  --industry "AI大模型" \
  --keywords "AI大模型,开放平台,ToB" \
  --years 6
```

**注意**: 此方式只生成框架,需要手动补充 `[待补充]` 内容

---

## 📚 斜杠命令说明

### /interview 命令

**触发条件**: 用户说 "我想应聘..." 或直接调用 /interview

**自动执行流程**:

1. **收集信息**
   - 询问公司名称(使用 AskUserQuestion)
   - 询问目标职位
   - 询问 JD 来源(有内容/有文件/暂时没有)
   - 询问简历位置(默认/其他)

2. **自动执行**
   - 安装依赖(pdfplumber)
   - 读取简历提取信息
   - 搜索公司最新信息
   - 生成 5 个完整文件

3. **主动询问**(如需要)
   - 如果背景信息不足,主动询问用户
   - 例如:"请提供公司官网"或"你对哪个产品最熟悉?"

### 快速开始示例

**示例 1: 最简方式**

```
我想应聘 MiniMax 的 AI产品经理职位

JD: [粘贴 JD 内容]

请帮我一键生成完整的面试准备包。
```

**示例 2: 提供完整信息**

```
我想应聘智谱AI的AI产品经理职位

公司: 智谱AI
职位: AI产品经理
JD: [粘贴 JD 内容]
简历: InterviewIntel/resumes/王蕾-AI 产品经理V1.0.pdf
行业: AI大模型
关键词: AI产品,大模型,ToB
工作年限: 6年
核心成就: 主导AI产品从0到1,用户增长300%

请帮我生成完整的面试准备包。
```

**示例 3: 使用外部简历**

```
我想应聘月之暗面的产品经理职位

公司: 月之暗面
职位: 产品经理
JD: [粘贴 JD 内容]
简历: /path/to/my/resume.pdf
项目路径: /Users/leayn/Documents/PythonProject/Hackthon/InterviewIntel

请帮我生成完整的面试准备包。
```

---

## 🔧 技术实现

### 依赖管理

**首次使用自动安装**:

```python
# 自动安装 pdfplumber
import subprocess
import sys

try:
    import pdfplumber
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pdfplumber', '-q', '--user'])
    import pdfplumber
```

### 简历读取实现

```python
import pdfplumber

def read_resume(pdf_path):
    """读取 PDF 简历并提取文本"""
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() + '\n'
        return text
```

### 文件结构

```
InterviewIntel/
├── interviews/              # 面试准备包输出目录
│   └── [公司名]/
│       ├── 01_company_intel_brief.md
│       ├── 02_resume_jd_matching.md
│       ├── 03_interview_prep_report.md
│       ├── 04_icebreaker_messages.md
│       └── 05_final_analysis_report.md
├── resumes/                 # 简历存放目录
│   ├── 王蕾-AI 产品经理V1.0.pdf
│   └── ...
└── interview-intel/
    └── SKILL_V6.md          # 本文档
```

---

## 📖 使用流程

### 标准流程(推荐)

```
1. 准备信息
   ├── JD 文本
   ├── 公司名称
   └── 职位名称

2. 调用 /interview 命令
   └── 一键生成 5 个完整文件

3. 阅读准备
   ├── 01_company_intel_brief.md (了解公司)
   ├── 02_resume_jd_matching.md (了解匹配度)
   ├── 03_interview_prep_report.md (准备面试话术)
   ├── 04_icebreaker_messages.md (准备开场白)
   └── 05_final_analysis_report.md (制定行动计划)

4. 面试实战
   ├── 准备核心案例
   ├── 模拟面试练习
   └── 参加面试
```

---

## 🎯 最佳实践

### 面试准备时间规划

**第1天**: 生成并阅读所有文件
**第2-3天**: 深度理解公司和职位
**第4-5天**: 准备核心案例和话术
**第6天**: 模拟面试练习
**第7天**: 面试前最后复习

### 核心文件阅读顺序

1. **05_final_analysis_report.md** - 先看行动计划,了解全局
2. **01_company_intel_brief.md** - 了解公司和职位
3. **02_resume_jd_matching.md** - 了解自己的匹配度
4. **03_interview_prep_report.md** - 准备面试话术
5. **04_icebreaker_messages.md** - 准备开场白

### 面试前快速复习

- 只读各文件的"核心信息速览"部分
- 重点标记关键数据和话术
- 准备好问面试官的问题

---

## 🔄 更新日志

### v6.2 (2026-01-21) ⭐ 最新版本

**重大修复**:

- 🐛 **修复简历读取问题**: 自动安装 pdfplumber 依赖
- 🐛 **优化简历查找逻辑**: 支持从 resumes/ 目录自动查找
- 🐛 **完善错误处理**: 依赖安装失败时给出明确提示
- 🐛 **优化用户体验**: 更清晰的进度提示和错误信息

**改进**:

- 📝 更新命令文档,提供更多示例
- 📝 优化一键完成方案的工作流程
- 📝 完善斜杠命令说明
- 📝 增加快速开始模板

**技术改进**:

- 🔧 自动检测并安装依赖
- 🔧 支持 PDF 简历自动读取
- 🔧 优化文件查找逻辑

### v1.0.0 (2026-01-21)

**重大升级**:

- ✨ **统一脚本**: 创建 `all_in_one_v1.0.0.py`,集成所有内容生成逻辑
- ✨ **智能 JD 解析**: 自动提取职责描述和任职要求
- ✨ **自动生成破冰文案**: 两种策略(专业匹配型 + 业务洞察型)
- ✨ **智能匹配分析**: 基于工作年限和成就自动生成匹配度框架
- ✨ **面试策略框架**: 自动生成 HR/业务/高管三轮策略
- 🎉 **一键完成方案**: 配合 Claude Code 实现全自动化
  - 自动读取简历提取真实经历
  - 自动搜索公司最新信息
  - 主动询问缺失信息
  - AI 智能填充所有 `[待补充]` 内容
  - 生成 100% 完成的面试准备包

### v1.0.0 (2026-01-21)

**重大升级**:

- ✨ 标准化 5 个输出文件结构
- ✨ 新增详细版+精简版双模式
- ✨ 新增 `company_researcher.py` 脚本
- ✨ 新增 `final_report_generator.py` 脚本
- ✨ 统一文件命名规范(数字前缀)

---

## 🛠️ 技术栈

- **语言**: Python 3.8+
- **依赖**:
  - `pdfplumber`: PDF 简历读取(自动安装)
- **输出**: Markdown 格式
- **存储**: 本地文件系统

---

## 📞 常见问题

### Q1: 首次使用报错 "ModuleNotFoundError: No module named 'pdfplumber'"

**A**: 这是正常的,系统会自动安装 pdfplumber。如果自动安装失败,请手动执行:

```bash
pip3 install pdfplumber --user -q
```

### Q2: 简历读取失败

**A**: 请检查:
1. 简历文件是否在 `InterviewIntel/resumes/` 目录
2. 简历文件是否是 PDF 格式
3. 文件路径是否正确

### Q3: 没有提供简历路径怎么办

**A**: 系统会自动在 `InterviewIntel/resumes/` 目录查找简历。如果找不到,会询问你具体的简历路径。

### Q4: 想使用其他位置的简历

**A**: 在调用 /interview 时明确指定简历路径:

```
我的简历在 /path/to/my/resume.pdf
```

---

## 📄 许可

MIT License

---

**最后更新**: 2026-01-21
**版本**: v6.2 (修复简历读取,完善一键完成方案)
**作者**: Interview Intel Team

**v6.2 新增功能**:
- 🐛 修复简历读取问题,自动安装 pdfplumber
- 🎉 完善一键完成方案,更流畅的用户体验
- 📝 更新命令文档,提供更多使用示例
- ✅ 优化错误处理和提示信息

**参考示例**: `companies/MiniMax/` - 使用一键完成方案生成的完整示例
