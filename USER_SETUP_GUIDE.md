# Interview Intel - 用户配置指南

**让任何人都能快速上手使用 Interview Intel 工具**

版本：v6.2
更新日期：2026-02-06

---

## 📋 目录

1. [快速开始（5分钟）](#快速开始5分钟)
2. [详细安装步骤](#详细安装步骤)
3. [配置你的简历](#配置你的简历)
4. [第一次使用](#第一次使用)
5. [进阶配置](#进阶配置)
6. [常见问题](#常见问题)

---

## 🚀 快速开始（5分钟）

### 前置要求

- Python 3.8 或更高版本
- 一份 PDF 格式的简历
- 互联网连接（用于搜索公司信息）

### 三步上手

```bash
# 第 1 步：克隆或下载项目
git clone https://github.com/your-repo/InterviewIntel.git
cd InterviewIntel

# 第 2 步：安装依赖
pip install pdfplumber

# 第 3 步：添加你的简历
cp ~/你的简历.pdf resumes/你的名字-职位.pdf

# 完成！现在可以使用了
```

---

## 📦 详细安装步骤

### 方式 1：从 GitHub 安装（推荐）

```bash
# 1. 克隆仓库
git clone https://github.com/your-repo/InterviewIntel.git
cd InterviewIntel

# 2. 安装 Python 依赖
pip3 install pdfplumber -q --user

# 3. 验证安装
python3 interview-intel/scripts/all_in_one_v6.1.py --help
```

### 方式 2：下载 ZIP 包安装

```bash
# 1. 下载 ZIP 包并解压
# 下载地址：https://github.com/your-repo/InterviewIntel/archive/main.zip

# 2. 进入目录
cd InterviewIntel-main

# 3. 安装依赖
pip3 install pdfplumber -q --user

# 4. 验证
python3 interview-intel/scripts/all_in_one_v6.1.py --help
```

### 验证安装成功

如果看到以下输出，说明安装成功：

```
usage: all_in_one_v6.1.py [-h] --base-path BASE_PATH --company COMPANY --role ROLE
                          [--jd-file JD_FILE] [--resume-version RESUME_VERSION]
                          ...
```

---

## 📄 配置你的简历

### 步骤 1：准备简历文件

**支持的格式**：
- ✅ PDF（推荐）
- ✅ Word（需转换为 PDF）

**命名建议**：
```
你的名字-职位类型-版本.pdf

示例：
- 张三-产品经理V1.0.pdf
- 李四-后端工程师V2.0.pdf
- 王五-数据分析师-通用版.pdf
```

### 步骤 2：放置简历文件

```bash
# 方式 1：直接复制
cp ~/Downloads/我的简历.pdf InterviewIntel/resumes/张三-产品经理V1.0.pdf

# 方式 2：使用 Finder/文件管理器
# 将简历拖拽到 InterviewIntel/resumes/ 目录
```

### 步骤 3：验证简历可读取

```bash
# 进入项目目录
cd InterviewIntel

# 测试简历读取
python3 -c "
import pdfplumber
with pdfplumber.open('resumes/张三-产品经理V1.0.pdf') as pdf:
    print(f'✅ 简历读取成功！共 {len(pdf.pages)} 页')
    print(f'前 100 字符：{pdf.pages[0].extract_text()[:100]}')
"
```

### 步骤 4：注册简历版本（可选）

```bash
# 使用简历管理工具注册版本
python3 interview-intel/scripts/resume_manager.py create \
  --file resumes/张三-产品经理V1.0.pdf \
  --version v1.0 \
  --desc "通用产品经理简历" \
  --target "Product Manager,PM" \
  --skills "产品规划,需求分析,项目管理"
```

---

## 🎯 第一次使用

### 场景：准备 MiniMax 的产品经理面试

#### 步骤 1：准备 JD 内容

```bash
# 创建 JD 文件
cat > /tmp/minimax_jd.txt << 'EOF'
职位描述
1、参与 AI开放平台的产品设计，为客户提供极致的AI产品体验和服务
2、与解决方案团队紧密合作，清晰理解客户需求，迭代产品功能
3、与研发团队密切合作，理解 AI相关技术和边界，推进研发迭代

职位要求
1、计算机、人工智能或相关领域的学士或硕士学位
2、优秀的产品sense和策划能力
3、了解AI大模型相关技术、应用场景和业界进展
4、3年以上开放平台类/AI类产品经验
EOF
```

#### 步骤 2：运行生成脚本

```bash
cd InterviewIntel

python3 interview-intel/scripts/all_in_one_v6.1.py \
  --base-path . \
  --company "MiniMax" \
  --role "AI产品经理" \
  --jd-file "/tmp/minimax_jd.txt" \
  --resume-version "张三-产品经理V1.0.pdf" \
  --industry "AI大模型" \
  --keywords "AI产品,开放平台,ToB" \
  --achievement "主导AI产品从0到1，用户增长300%" \
  --years 3
```

#### 步骤 3：查看生成的文件

```bash
# 查看生成的文件列表
ls -lh companies/MiniMax/

# 输出：
# 01_company_intel_brief.md       - 公司背景分析
# 02_resume_jd_matching.md        - 简历匹配度分析
# 03_interview_prep_report.md     - 面试准备报告
# 04_icebreaker_messages.md      - 破冰开场白
# 05_final_analysis_report.md    - 最终行动计划
```

#### 步骤 4：开始阅读准备

```bash
# 使用你喜欢的 Markdown 阅读器
# macOS
open companies/MiniMax/01_company_intel_brief.md

# Linux
xdg-open companies/MiniMax/01_company_intel_brief.md

# 或者用 VSCode
code companies/MiniMax/
```

---

## 🔧 进阶配置

### 1. 使用 Claude Code 一键生成（推荐）

如果你使用 Claude Code，可以直接对话：

```
我想应聘 MiniMax 的 AI产品经理职位

JD: [粘贴 JD 内容]

我的简历在 InterviewIntel/resumes/张三-产品经理V1.0.pdf

请帮我一键生成完整的面试准备包。
```

Claude Code 会自动：
1. 安装依赖
2. 读取简历
3. 搜索公司信息
4. 生成所有文件
5. 填充完整内容

### 2. 配置环境变量（可选）

```bash
# 在 ~/.bashrc 或 ~/.zshrc 中添加
export INTERVIEW_INTEL_HOME="/path/to/InterviewIntel"
export INTERVIEW_INTEL_RESUME="张三-产品经理V1.0.pdf"

# 然后可以简化命令
alias interview-prep='python3 $INTERVIEW_INTEL_HOME/interview-intel/scripts/all_in_one_v6.1.py \
  --base-path $INTERVIEW_INTEL_HOME \
  --resume-version $INTERVIEW_INTEL_RESUME'
```

### 3. 创建个人配置文件

```bash
# 创建配置文件
cat > ~/.interview_intel_config << 'EOF'
# 个人配置
RESUME_VERSION="张三-产品经理V1.0.pdf"
INDUSTRY="互联网"
YEARS=3
DEFAULT_KEYWORDS="产品设计,数据分析,项目管理"
DEFAULT_ACHIEVEMENT="主导产品从0到1，MAU达到10万+"
EOF

# 在脚本中使用
source ~/.interview_intel_config
```

### 4. 管理多个简历版本

```bash
# 创建不同版本的简历
resumes/
├── 张三-产品经理-ToB版.pdf         # B端产品职位
├── 张三-产品经理-ToC版.pdf         # C端产品职位
├── 张三-产品经理-AI版.pdf          # AI产品职位
└── 张三-数据产品经理.pdf           # 数据产品职位

# 针对不同职位使用不同简历
python3 interview-intel/scripts/all_in_one_v6.1.py \
  --resume-version "张三-产品经理-AI版.pdf" \  # 使用 AI 版本
  --company "智谱AI" \
  --role "AI产品经理"
```

---

## 📊 文件结构说明

### 安装后的目录结构

```
InterviewIntel/                      # 项目根目录
│
├── resumes/                         # 你的简历存放在这里
│   ├── 张三-产品经理V1.0.pdf
│   ├── 张三-产品经理V2.0.pdf
│   └── resume_registry.json        # 简历版本注册表
│
├── companies/                       # 生成的分析报告在这里
│   ├── MiniMax/
│   │   ├── 01_company_intel_brief.md
│   │   ├── 02_resume_jd_matching.md
│   │   ├── 03_interview_prep_report.md
│   │   ├── 04_icebreaker_messages.md
│   │   └── 05_final_analysis_report.md
│   └── [其他公司]/
│
├── interview-intel/                 # 核心工具代码
│   ├── SKILL_V6.md                 # 完整文档
│   └── scripts/
│       ├── all_in_one_v6.1.py      # 主脚本（你会用到）
│       ├── resume_manager.py        # 简历管理
│       └── interview_tracker.py     # 面试追踪
│
└── .claude/                         # Claude Code 配置
    └── commands/
        └── interview.md             # /interview 命令定义
```

---

## ❓ 常见问题

### Q1: 我不会编程，可以使用吗？

**A: 可以！** 有两种方式：

**方式 1：使用 Claude Code（最简单）**
1. 安装 Claude Code
2. 打开 InterviewIntel 项目
3. 直接对话："我想应聘 XXX 公司的 XXX 职位，JD 是..."
4. Claude Code 会自动完成所有操作

**方式 2：复制粘贴命令**
1. 复制下面的命令模板
2. 修改公司名、职位名、简历名
3. 在终端中运行

```bash
cd InterviewIntel
python3 interview-intel/scripts/all_in_one_v6.1.py \
  --base-path . \
  --company "公司名（改成你的）" \
  --role "职位名（改成你的）" \
  --resume-version "你的简历.pdf" \
  --years 你的工作年限
```

### Q2: 安装依赖失败怎么办？

**A: 尝试以下方法：**

```bash
# 方法 1：使用 pip3
pip3 install pdfplumber --user

# 方法 2：使用 python3 -m pip
python3 -m pip install pdfplumber --user

# 方法 3：使用国内镜像源
pip3 install pdfplumber -i https://pypi.tuna.tsinghua.edu.cn/simple

# 方法 4：检查 Python 版本
python3 --version  # 应该是 3.8 或更高
```

### Q3: 简历读取失败？

**A: 检查以下几点：**

1. **确认文件格式**
   ```bash
   file resumes/你的简历.pdf
   # 应该显示：PDF document
   ```

2. **确认文件权限**
   ```bash
   ls -lh resumes/你的简历.pdf
   # 应该有读权限（r）
   ```

3. **确认文件路径**
   ```bash
   # 使用绝对路径
   --resume-version "$(pwd)/resumes/你的简历.pdf"
   ```

4. **测试 pdfplumber**
   ```bash
   python3 -c "import pdfplumber; print('✅ pdfplumber 正常')"
   ```

### Q4: 如何更新我的信息？

**A: 重新运行脚本即可，会覆盖旧文件：**

```bash
# 更新后再次运行
python3 interview-intel/scripts/all_in_one_v6.1.py \
  --base-path . \
  --company "同一家公司" \
  --role "同一个职位" \
  --resume-version "新版本简历.pdf" \
  --years 更新后的年限
```

### Q5: 生成的内容不满意，可以编辑吗？

**A: 完全可以！生成的是 Markdown 文件，可以随意编辑：**

1. **使用任何文本编辑器**
   - VSCode（推荐）
   - Typora
   - Obsidian
   - 记事本

2. **编辑后保存**
   - 文件会保留，不会被覆盖（除非重新运行脚本）

3. **导出 PDF**
   - 大多数 Markdown 编辑器支持导出 PDF

### Q6: 可以分享给朋友使用吗？

**A: 可以！** 但要注意：

1. **清理你的个人数据**
   ```bash
   # 删除你的简历
   rm -rf resumes/*

   # 删除你的分析报告
   rm -rf companies/*

   # 保留示例文件
   git checkout resumes/master_resume_v1.0.pdf
   ```

2. **分享整个项目**
   ```bash
   # 打包项目
   cd ..
   zip -r InterviewIntel.zip InterviewIntel/

   # 或上传到 GitHub
   git push origin main
   ```

3. **提供这个配置指南**
   - 让朋友阅读 `USER_SETUP_GUIDE.md`

### Q7: 支持其他语言吗？

**A: 当前版本主要支持中文，但可以扩展：**

1. **JD 是英文**：可以正常使用，生成的分析会是中英混合
2. **简历是英文**：可以正常读取，但建议手动补充关键信息
3. **全英文版本**：可以通过修改模板实现（需要一定编程能力）

### Q8: 数据安全吗？

**A: 完全安全！**

1. **本地运行**：所有数据都在你的电脑上
2. **不上传**：不会将简历上传到任何服务器
3. **开源代码**：可以审查所有代码逻辑
4. **你可以：**
   - 断网使用（搜索公司信息需要网络）
   - 删除生成的文件
   - 完全控制你的数据

---

## 📚 学习资源

### 推荐阅读顺序

1. **本文档** - 快速上手
2. [QUICK_START_V6.1.md](QUICK_START_V6.1.md) - 快速开始指南
3. [interview-intel/SKILL_V6.md](interview-intel/SKILL_V6.md) - 完整功能文档
4. [.claude/commands/README.md](.claude/commands/README.md) - 斜杠命令说明

### 示例文件

查看这些示例了解输出效果：
- `companies/MiniMax/` - 完整示例
- `companies/SIF/` - 另一个示例
- `companies/言创万物/` - 第三个示例

### 视频教程（待添加）

- [ ] 5分钟快速安装
- [ ] 第一次使用演示
- [ ] Claude Code 一键生成
- [ ] 进阶技巧分享

---

## 🎯 下一步

现在你已经配置好了，可以：

1. ✅ **准备第一份面试** - 找一个 JD 试试看
2. ✅ **探索进阶功能** - 尝试简历版本管理
3. ✅ **分享给朋友** - 帮助更多人提高面试成功率
4. ✅ **提供反馈** - 告诉我们如何改进

---

## 📞 获取帮助

**遇到问题？**

1. **查看文档**：
   - [完整文档](interview-intel/SKILL_V6.md)
   - [常见问题](#常见问题)

2. **社区支持**：
   - GitHub Issues: [提交问题](https://github.com/your-repo/InterviewIntel/issues)
   - 讨论区: [参与讨论](https://github.com/your-repo/InterviewIntel/discussions)

3. **联系我们**：
   - Email: support@example.com
   - 微信群: [扫码加入]

---

## 🎉 开始你的求职之旅！

```bash
cd InterviewIntel
python3 interview-intel/scripts/all_in_one_v6.1.py --help
```

**祝你面试成功！** 🚀

---

**文档版本**: v1.0
**最后更新**: 2026-02-06
**维护者**: Interview Intel Team
