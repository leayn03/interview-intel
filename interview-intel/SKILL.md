# Interview Intel - v1.1.0

## 技能描述

AI 驱动的面试准备助手，通过专业化流水线团队并行生成，快速输出完整的面试准备策略。

**核心特性**:
- **5人专业团队并行** (默认): 公司研究员、简历分析师、面试教练、文案专家、战略顾问
- **加速 1.5x**: 原串行 ~200s → 并行 ~135s
- **事实验证协议**: 确保生成内容100%基于真实简历

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

**v1.1.0 最新状态**:

- ⚡ **默认方式**: 专业化流水线团队（5人并行，加速 1.5x）
- ✅ **依赖自动安装**: 自动安装 pdfplumber 用于读取 PDF 简历
- ✅ **简历读取优化**: 支持从 resumes/ 目录自动查找简历
- ✅ **事实验证协议**: 零容忍原则，确保所有内容基于真实简历
- ✅ **一键完成方案**: 配合 Claude Code 实现全自动化
  - 自动读取简历提取经历
  - 自动搜索公司最新信息
  - 主动询问缺失信息
  - 生成 100% 完成的面试准备包

**三种使用方式**:

1. **专业化流水线团队（默认）⭐**: 5个专业队友并行生成，加速 1.5x
2. **配合 Claude Code**: 一键完成所有工作，包括框架生成和内容填充
3. **手动使用脚本**: 生成框架后手动补充内容

---

## 🚀 使用方式

### 方式 1: 专业化流水线团队（默认）⭐⭐⭐

**适用场景**: 快速生成面试准备框架，5个专业队友并行协作

#### 团队架构

```
Team Lead (项目经理)
    ├── Teammate A: 公司研究员 → 01_company_intel_brief.md
    ├── Teammate B: 简历分析师 → 02_resume_jd_matching.md
    ├── Teammate C: 面试教练 → 03_interview_prep_report.md
    ├── Teammate D: 文案专家 → 04_icebreaker_messages.md
    └── Teammate E: 战略顾问 → 05_final_analysis_report.md
```

#### 并行流程

```
阶段1 (并行): Teammate A + B → ~45s
    ├─ 公司研究
    └─ 简历分析

阶段2 (并行): Teammate C + D → ~60s
    ├─ 面试策略
    └─ 破冰文案

阶段3 (串行): Teammate E → ~30s
    └─ 最终报告

总耗时: ~135s (原串行 ~200s, 加速 1.5x ⚡)
```

#### 使用方法

**方式 A: 命令行调用**

```bash
cd interview-intel
python scripts/pipeline_team.py \
  --company "阿里云" \
  --role "AI产品经理" \
  --candidate "王蕾" \
  --jd "raw_data/jd.txt" \
  --resume "resumes/王蕾-AI产品经理V1.0.pdf" \
  --base-path ".."
```

**方式 B: 自然语言触发（推荐）**

```
"帮我准备阿里云AI产品经理的面试，使用专业团队"
```

#### 输出效果

```
╔════════════════════════════════════════════════════════════╗
║              🤖 专业流水线团队启动                          ║
╚════════════════════════════════════════════════════════════╝

📋 任务信息:
   公司: 阿里云
   职位: AI产品经理
   候选人: 王蕾

📍 阶段 1/3: 公司研究 + 简历分析
────────────────────────────────────────────────────────────
✅ Teammate A (公司研究员): success (42.3s)
✅ Teammate B (简历分析师): success (45.1s)
⏱️  阶段1总耗时: 45.1s

📍 阶段 2/3: 面试策略 + 破冰文案
────────────────────────────────────────────────────────────
✅ Teammate C (面试教练): success (58.7s)
✅ Teammate D (文案专家): success (39.2s)
⏱️  阶段2总耗时: 58.7s

📍 阶段 3/3: 最终分析报告
────────────────────────────────────────────────────────────
✅ Teammate E (战略顾问): success (28.4s)
⏱️  阶段3总耗时: 28.4s

╔════════════════════════════════════════════════════════════╗
║                   🎉 全部完成!                            ║
╚════════════════════════════════════════════════════════════╝

⏱️  总耗时: 132.2s
⚡ 并行加速: 原串行 ~200s → 现在 132s (1.5x)
```

#### 优势

- ✅ **快速生成**: 并行执行，节省 35% 时间
- ✅ **专业分工**: 每个队友专注一个文件
- ✅ **依赖管理**: 自动处理文件依赖关系
- ✅ **进度可见**: 实时显示各队友工作状态
- ✅ **默认方式**: 开箱即用，无需额外配置

#### 注意

- 此方式生成框架文件，包含完整结构和 AI 生成的内容
- 如需更个性化的内容，可结合方式2（配合 Claude Code）进一步优化

---

### 方式 2: 配合 Claude Code 一键完成

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

生成 5 个 100% 完成的文件,保存在 `companies/[公司名]-[职位]-[候选人名字]/` 目录:
- ✅ `01_company_intel_brief.md`
- ✅ `02_resume_jd_matching.md`
- ✅ `03_interview_prep_report.md`
- ✅ `04_icebreaker_messages.md`
- ✅ `05_final_analysis_report.md`

**命名规范**：`companies/贝壳-MR产品经理-李承润/`
- 支持同一公司多个岗位：`贝壳-MR产品经理-张三/` 和 `贝壳-AI算法工程师-李四/`
- 支持多人面试同一岗位：`贝壳-MR产品经理-张三/` 和 `贝壳-MR产品经理-李四/`

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

### 方式 3: 使用统一脚本生成框架(传统方式)

使用 `all_in_one.py` 生成框架后手动补充内容:

```bash
cd /Users/leayn/Documents/PythonProject/Hackthon/InterviewIntel/interview-intel
python scripts/all_in_one.py \
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
   - **读取简历提取信息** ⚠️ 必须使用 pdfplumber，不能用 Read 工具
   - 搜索公司最新信息
   - 生成 5 个完整文件

3. **主动询问**(如需要)
   - 如果背景信息不足,主动询问用户
   - 例如:"请提供公司官网"或"你对哪个产品最熟悉?"

---

### 🔧 PDF读取最佳实践

**⚠️ 关键原则**: 必须使用 `pdfplumber` 读取PDF简历，不能使用 `Read` 工具

**原因**:
1. `Read` 工具对某些PDF格式支持有限，可能返回URL而非内容
2. `pdfplumber` 专门用于PDF文本提取，可靠性高
3. 支持中文PDF和各种编码格式

**正确实现**:
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

**错误做法** ❌:
```python
# 不要使用 Read 工具读取PDF
Read(file_path="resumes/简历.pdf")  # 这可能失败
```

**正确做法** ✅:
```python
# 使用 Bash 工具运行 Python 脚本
Bash(command="""
python3 << 'EOF'
import pdfplumber
with pdfplumber.open('resumes/简历.pdf') as pdf:
    text = ''
    for page in pdf.pages:
        text += page.extract_text() + '\n'
    print(text)
EOF
""")
```

**测试PDF读取功能**:
```bash
# 运行测试脚本验证
python3 interview-intel/scripts/test_pdf_reader.py
```

---

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

**⚠️ 重要**: 必须使用 `pdfplumber` 读取PDF，不能使用其他工具（如 `Read` 工具），因为：
1. `Read` 工具对某些PDF格式支持有限，可能返回URL而非内容
2. `pdfplumber` 专门用于PDF文本提取，可靠性高
3. 支持中文PDF和各种编码格式

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
├── companies/               # 面试准备包输出目录
│   └── [公司名]-[职位]-[候选人名字]/
│       ├── 01_company_intel_brief.md
│       ├── 02_resume_jd_matching.md
│       ├── 03_interview_prep_report.md
│       ├── 04_icebreaker_messages.md
│       └── 05_final_analysis_report.md
├── resumes/                 # 简历存放目录
│   ├── 王蕾-AI 产品经理V1.0.pdf
│   └── ...
└── interview-intel/
    └── SKILL.md             # 本文档
```

**命名示例**：
- `companies/贝壳-MR产品经理-李承润/`
- `companies/阿里云-AI产品经理-王蕾/`
- 支持同一公司多个岗位：`贝壳-MR产品经理-张三/` 和 `贝壳-AI算法工程师-李四/`
- 支持多人面试同一岗位：`贝壳-MR产品经理-张三/` 和 `贝壳-MR产品经理-李四/`

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

## 🔧 故障排查

### PDF读取问题诊断

**症状**: 简历读取失败或返回URL而非内容

**诊断步骤**:

1. **运行测试脚本**
   ```bash
   python3 interview-intel/scripts/test_pdf_reader.py
   ```

2. **检查依赖**
   ```bash
   python3 -c "import pdfplumber; print('✅ pdfplumber 已安装')"
   ```

3. **检查PDF文件**
   ```bash
   file resumes/你的简历.pdf
   # 应该输出: PDF document, version X.X
   ```

4. **检查文件权限**
   ```bash
   ls -lh resumes/你的简历.pdf
   # 确保文件可读
   ```

**常见解决方案**:

| 问题 | 解决方案 |
|------|----------|
| `pdfplumber` 未安装 | `pip3 install pdfplumber --user -q` |
| PDF路径错误 | 使用绝对路径或确认相对路径正确 |
| PDF是扫描版 | 使用 OCR 工具转换或提供文字版 |
| 返回URL而非内容 | 确保使用 `pdfplumber` 而非 `Read` 工具 |

---

## 🔄 更新日志

### v1.1.0 (2026-02-27) ⭐ 专业化流水线团队

**核心升级**:

- ⚡ **默认方式**: 专业化流水线团队成为默认执行方式
- 🔧 **并行加速**: 5个专业队友并行生成，加速 1.5x
- 📁 **新增配置**: `pipeline_config.json` 团队配置文件
- 🧪 **测试脚本**: `test_pipeline_team.py` 快速测试功能

**团队架构**:
- Teammate A: 公司研究员
- Teammate B: 简历分析师
- Teammate C: 面试教练
- Teammate D: 文案专家
- Teammate E: 战略顾问

**使用方式变更**:
- 方式1（新增）: 专业化流水线团队（默认）
- 方式2（原方式1）: 配合 Claude Code
- 方式3（原方式2）: 手动使用脚本

### v1.0.0 (2025-02-08) ⭐ 首个公开版本

**核心功能**:

- ✅ **事实验证协议**: 零容忍原则，确保所有内容基于真实简历
- ✅ **一键生成工作流**: 5个标准Markdown文件自动生成
- ✅ **AI智能填充**: STAR案例、面试话术、破冰文案
- ✅ **简历读取优化**: 自动安装 pdfplumber，支持PDF简历
- ✅ **完整文档体系**: 用户指南、FAQ、分享指南

**技术改进**:

- 🔧 自动检测并安装依赖
- 🔧 支持 PDF 简历自动读取
- 🔧 优化文件查找逻辑
- 🔧 Git 版本管理和发布流程

**重大升级**:

- ✨ **统一脚本**: 使用 `all_in_one.py`,集成所有内容生成逻辑
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
4. 是否使用了 `pdfplumber` 而不是 `Read` 工具

**测试PDF读取**:
```bash
python3 interview-intel/scripts/test_pdf_reader.py
```

### Q2.1: 为什么不能使用 Read 工具读取PDF?

**A**: `Read` 工具对某些PDF格式支持有限，可能返回URL而非内容。**必须使用 `pdfplumber`**:

❌ **错误**:
```python
Read(file_path="resumes/简历.pdf")  # 可能失败
```

✅ **正确**:
```python
import pdfplumber
with pdfplumber.open('resumes/简历.pdf') as pdf:
    text = ''
    for page in pdf.pages:
        text += page.extract_text() + '\n'
```

### Q2.2: PDF读取时出现警告信息

**A**: 如果看到类似 `Could not get FontBBox from font descriptor` 的警告，这是正常的。这些警告不影响文本提取，可以忽略。

### Q2.3: PDF是扫描版图片怎么办?

**A**: 如果PDF是扫描版图片，`pdfplumber` 无法提取文本。需要使用 OCR 工具，建议:
1. 使用 Adobe Acrobat 或其他工具进行 OCR 识别
2. 或者提供文字版的简历

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

**最后更新**: 2026-02-27
**版本**: v1.1.0 (专业化流水线团队 - 默认并行加速)
**作者**: Interview Intel Team

**v1.1.0 核心功能**:
- ⚡ 专业化流水线团队（默认方式）
- ✅ 5个专业队友并行生成，加速 1.5x
- ✅ 事实验证协议，零幻觉保证
- ✅ 一键生成面试准备包（5个标准文件）
- ✅ AI 智能填充内容（STAR案例、面试话术）
- 📁 支持灵活的文件夹命名：`公司名-职位-候选人名字`

**参考示例**: `companies/阿里云-AI产品经理-王蕾/` - 使用专业化流水线团队生成的完整示例
