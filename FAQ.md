# Interview Intel - 常见问题解答 (FAQ)

**快速找到问题的解决方案**

最后更新：2026-02-06

---

## 📋 目录

- [安装问题](#安装问题)
- [使用问题](#使用问题)
- [简历相关](#简历相关)
- [生成内容](#生成内容)
- [技术问题](#技术问题)
- [进阶使用](#进阶使用)

---

## 安装问题

### Q1: 安装时提示 "command not found: python3"

**A:** 你的系统没有安装 Python 3。

**解决方法：**

```bash
# macOS
brew install python3

# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# CentOS/RHEL
sudo yum install python3 python3-pip

# Windows
# 访问 https://www.python.org/downloads/ 下载安装
```

验证安装：
```bash
python3 --version
# 应显示：Python 3.x.x
```

---

### Q2: pip install 失败，提示权限错误

**A:** 没有权限安装到系统目录。

**解决方法：**

```bash
# 方法 1：安装到用户目录（推荐）
pip3 install pdfplumber --user

# 方法 2：使用虚拟环境
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install pdfplumber

# 方法 3：使用 sudo（不推荐）
sudo pip3 install pdfplumber
```

---

### Q3: 安装 pdfplumber 超时

**A:** 网络问题或 PyPI 服务器访问慢。

**解决方法：**

```bash
# 使用国内镜像源
pip3 install pdfplumber -i https://pypi.tuna.tsinghua.edu.cn/simple

# 或永久配置镜像源
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

其他可用镜像：
- 清华：https://pypi.tuna.tsinghua.edu.cn/simple
- 阿里云：https://mirrors.aliyun.com/pypi/simple/
- 中科大：https://pypi.mirrors.ustc.edu.cn/simple/

---

### Q4: 运行 setup.sh 提示权限被拒绝

**A:** 脚本没有执行权限。

**解决方法：**

```bash
# 添加执行权限
chmod +x setup.sh

# 然后运行
./setup.sh
```

---

## 使用问题

### Q5: 运行脚本提示 "No such file or directory"

**A:** 不在正确的目录，或文件路径错误。

**解决方法：**

```bash
# 1. 确认在项目根目录
pwd
# 应显示：/path/to/InterviewIntel

# 2. 检查文件是否存在
ls interview-intel/scripts/all_in_one.py

# 3. 使用绝对路径
cd /path/to/InterviewIntel
python3 interview-intel/scripts/all_in_one.py --help
```

---

### Q6: 生成的文件在哪里？

**A:** 在 `companies/[公司名]/` 目录下。

**查看方法：**

```bash
# 列出所有公司
ls companies/

# 查看特定公司的文件
ls companies/MiniMax/

# 输出示例：
# 01_company_intel_brief.md
# 02_resume_jd_matching.md
# 03_interview_prep_report.md
# 04_icebreaker_messages.md
# 05_final_analysis_report.md
```

---

### Q7: 可以同时分析多个职位吗？

**A:** 可以！为每个职位运行一次脚本即可。

**示例：**

```bash
# 职位 1：产品经理
python3 interview-intel/scripts/all_in_one.py \
  --company "MiniMax" \
  --role "AI产品经理" \
  ...

# 职位 2：研发经理
python3 interview-intel/scripts/all_in_one.py \
  --company "MiniMax" \
  --role "研发经理" \
  ...

# 生成的文件会自动分开
ls companies/MiniMax/
# 01_company_intel_brief.md           # 共用
# 02_resume_jd_matching_AI产品经理.md  # 独立
# 02_resume_jd_matching_研发经理.md     # 独立
```

---

### Q8: 运行脚本报错："ModuleNotFoundError: No module named 'pdfplumber'"

**A:** pdfplumber 未安装或安装失败。

**解决方法：**

```bash
# 1. 检查是否已安装
python3 -c "import pdfplumber; print('已安装')"

# 2. 如果未安装
pip3 install pdfplumber --user

# 3. 如果还是报错，检查 Python 路径
which python3
which pip3
# 确保两者在同一个 Python 环境

# 4. 使用 python3 -m pip 安装
python3 -m pip install pdfplumber --user
```

---

## 简历相关

### Q9: 简历读取失败，显示 "PDF 解析错误"

**A:** PDF 文件可能损坏、加密或格式不兼容。

**解决方法：**

```bash
# 1. 检查文件是否能正常打开
open resumes/你的简历.pdf

# 2. 尝试重新导出 PDF
# - 打开原始简历（Word/Google Docs）
# - 重新导出为 PDF
# - 确保没有设置密码保护

# 3. 测试 PDF 可读性
python3 << EOF
import pdfplumber
try:
    with pdfplumber.open('resumes/你的简历.pdf') as pdf:
        text = pdf.pages[0].extract_text()
        print(f"✅ PDF 可读，前100字符：{text[:100]}")
except Exception as e:
    print(f"❌ 错误：{e}")
EOF
```

**常见原因：**
- PDF 文件被加密/有密码保护
- PDF 是扫描版（图片）而非文本版
- PDF 版本太新或太旧
- 文件损坏

**解决方案：**
- 移除 PDF 密码保护
- 使用 OCR 工具识别扫描版
- 使用主流工具重新导出 PDF

---

### Q10: 我的简历是 Word 格式，可以用吗？

**A:** 需要先转换为 PDF。

**转换方法：**

```bash
# macOS（使用 Pages 或 Word）
# 打开 Word 文件 → 导出 → PDF

# Linux（使用 LibreOffice）
libreoffice --headless --convert-to pdf 你的简历.docx

# 在线转换
# https://www.ilovepdf.com/word_to_pdf
# https://smallpdf.com/word-to-pdf
```

**未来支持：**
我们计划在后续版本中直接支持 Word 格式。

---

### Q11: 我有多份简历，如何管理？

**A:** 使用简历版本管理系统。

**方法：**

```bash
# 1. 将所有简历放到 resumes/ 目录，使用描述性命名
resumes/
├── 张三-产品经理-ToB版.pdf
├── 张三-产品经理-ToC版.pdf
├── 张三-产品经理-AI版.pdf
└── 张三-数据产品经理.pdf

# 2. 注册版本（可选）
python3 interview-intel/scripts/resume_manager.py create \
  --file resumes/张三-产品经理-AI版.pdf \
  --version v1.0-AI \
  --desc "AI产品经理专用简历" \
  --target "AI Product Manager" \
  --skills "AI产品,大模型,产品规划"

# 3. 使用时指定版本
python3 interview-intel/scripts/all_in_one.py \
  --resume-version "张三-产品经理-AI版.pdf" \
  ...
```

---

### Q12: 简历中有敏感信息，安全吗？

**A:** 完全安全！所有数据都在本地处理。

**安全措施：**

1. **本地处理**：简历不会上传到任何服务器
2. **离线运行**：除了搜索公司信息，其他都可以离线
3. **数据控制**：你可以随时删除生成的文件
4. **开源代码**：可以审查代码逻辑

**建议：**

```bash
# 分享项目前，清理个人数据
rm -rf resumes/*          # 删除简历
rm -rf companies/*        # 删除分析报告
rm ~/.interview_intel_config  # 删除配置文件
```

---

## 生成内容

### Q13: 生成的内容太泛化，不够个性化

**A:** 需要提供更详细的参数。

**改进方法：**

```bash
# ❌ 不好：参数太少
python3 interview-intel/scripts/all_in_one.py \
  --company "MiniMax" \
  --role "产品经理"

# ✅ 更好：提供详细信息
python3 interview-intel/scripts/all_in_one.py \
  --company "MiniMax" \
  --role "B端大模型产品经理" \
  --jd-file jd.txt \
  --resume-version "张三-AI产品经理.pdf" \
  --industry "AI大模型" \
  --keywords "大模型,开放平台,ToB,API设计,开发者生态" \
  --achievement "主导AI开放平台从0到1，接入企业客户200+，GMV达到500万" \
  --years 5

# 💡 使用 Claude Code 获得最佳效果
# 直接对话，提供完整的 JD 和你的背景故事
```

---

### Q14: 生成的破冰文案太官方，不像我的风格

**A:** 生成后可以手动编辑，保留框架调整表述。

**方法：**

```bash
# 1. 打开破冰文案文件
code companies/MiniMax/04_icebreaker_messages.md

# 2. 根据你的风格修改
# - 保留核心信息点
# - 调整表达方式
# - 加入个人特色

# 3. 保存后使用
```

**提示：**
- 生成的内容是基础框架
- 建议根据个人风格适当调整
- 可以 A/B 测试不同版本

---

### Q15: 匹配度分析不准确

**A:** 可能是 JD 解析不完整或参数不准确。

**改进方法：**

```bash
# 1. 确保 JD 文件格式清晰
# 职位描述
1、负责 AI 产品设计
2、协作研发团队

# 职位要求
1、3年以上产品经验
2、熟悉 AI 技术

# 2. 提供完整的工作年限和成就
--years 5 \
--achievement "详细的成就描述"

# 3. 使用 Claude Code 获得更准确的分析
# AI 会理解上下文，给出更精准的匹配度
```

---

### Q16: 可以重新生成某个文件吗？

**A:** 可以，重新运行脚本即可覆盖。

**方法：**

```bash
# 重新生成整套文件（会覆盖）
python3 interview-intel/scripts/all_in_one.py \
  --company "MiniMax" \
  --role "产品经理" \
  ... # 其他参数

# 如果只想更新某个文件，手动编辑即可
code companies/MiniMax/03_interview_prep_report.md
```

---

## 技术问题

### Q17: 运行很慢，如何加速？

**A:** 主要耗时在搜索公司信息，可以优化。

**优化方法：**

```bash
# 1. 如果已有公司信息，可以提前准备
# 手动编辑：companies/MiniMax/01_company_intel_brief.md

# 2. 关闭网络搜索（如果不需要最新信息）
# 在脚本中设置 --offline 模式（未来版本）

# 3. 使用 SSD 硬盘
# PDF 读取会更快

# 4. 使用 Claude Code
# AI 并行处理，速度更快
```

---

### Q18: 如何在没有网络的情况下使用？

**A:** 大部分功能支持离线，但公司信息搜索需要网络。

**离线使用：**

```bash
# 1. 提前下载依赖
pip3 download pdfplumber

# 2. 离线安装
pip3 install pdfplumber-*.whl --user

# 3. 手动准备公司信息
# 编辑：companies/MiniMax/01_company_intel_brief.md

# 4. 运行脚本
python3 interview-intel/scripts/all_in_one.py \
  --company "MiniMax" \
  --role "产品经理" \
  --skip-search  # 跳过网络搜索
```

---

### Q19: 支持 Windows 吗？

**A:** 理论上支持，但推荐使用 macOS 或 Linux。

**Windows 使用：**

```bash
# 1. 安装 Python 3.8+
# 下载：https://www.python.org/downloads/

# 2. 安装依赖
pip install pdfplumber

# 3. 使用 PowerShell 或 CMD 运行
python interview-intel\scripts\all_in_one.py ^
  --base-path . ^
  --company "MiniMax" ^
  --role "产品经理"

# 注意：路径使用反斜杠 \
```

**已知问题：**
- setup.sh 脚本不支持 Windows
- 路径分隔符不同
- 建议使用 WSL（Windows Subsystem for Linux）

---

### Q20: 如何备份我的数据？

**A:** 所有数据都在项目目录，直接复制即可。

**备份方法：**

```bash
# 方法 1：压缩整个项目
cd ..
zip -r InterviewIntel_backup_$(date +%Y%m%d).zip InterviewIntel/

# 方法 2：只备份生成的数据
cd InterviewIntel
zip -r data_backup_$(date +%Y%m%d).zip resumes/ companies/

# 方法 3：使用 Git
git init
git add .
git commit -m "Backup $(date)"

# 方法 4：同步到云端
# Google Drive, Dropbox, iCloud 等
```

---

## 进阶使用

### Q21: 如何自动追踪面试进度？

**A:** 使用内置的面试追踪工具。

**方法：**

```bash
# 1. 初始化追踪
python3 interview-intel/scripts/interview_tracker.py init \
  --company-path companies/MiniMax \
  --company "MiniMax" \
  --role "AI产品经理" \
  --resume v1.0

# 2. 添加面试轮次
python3 interview-intel/scripts/interview_tracker.py add-round \
  --company-path companies/MiniMax \
  --round 1 \
  --name "电话面试" \
  --date 2026-02-10 \
  --interviewer "张经理"

# 3. 更新结果
python3 interview-intel/scripts/interview_tracker.py update \
  --company-path companies/MiniMax \
  --round 1 \
  --status completed \
  --result passed
```

详见：[interview-intel/SKILL_V6.md](interview-intel/SKILL_V6.md#5-面试进度追踪)

---

### Q22: 如何生成统计报告？

**A:** 使用分析工具。

**方法：**

```bash
# 生成全局统计
python3 interview-intel/scripts/analytics_generator.py generate --scope global

# 导出 CSV
python3 interview-intel/scripts/analytics_generator.py export \
  --format csv \
  --output interview_data.csv

# 生成 HTML 仪表板
python3 interview-intel/scripts/analytics_generator.py dashboard \
  --output dashboard.html
```

---

### Q23: 可以集成到 CI/CD 吗？

**A:** 可以！脚本支持命令行参数，易于集成。

**示例：GitHub Actions**

```yaml
# .github/workflows/interview-prep.yml
name: Interview Prep

on: [push]

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: pip install pdfplumber
      - name: Generate reports
        run: |
          python3 interview-intel/scripts/all_in_one.py \
            --base-path . \
            --company "MiniMax" \
            --role "产品经理"
```

---

### Q24: 如何贡献代码或报告问题？

**A:** 欢迎贡献！

**方式：**

1. **报告 Bug**
   - GitHub Issues: [提交问题](https://github.com/your-repo/InterviewIntel/issues)
   - 包含：错误信息、系统环境、复现步骤

2. **提交功能请求**
   - GitHub Discussions: [功能建议](https://github.com/your-repo/InterviewIntel/discussions)

3. **贡献代码**
   ```bash
   # Fork 项目
   git clone https://github.com/your-username/InterviewIntel.git

   # 创建分支
   git checkout -b feature/your-feature

   # 提交代码
   git commit -m "Add your feature"
   git push origin feature/your-feature

   # 创建 Pull Request
   ```

---

## 🆘 还是没解决？

### 获取帮助的方式

1. **查看完整文档**
   - [USER_SETUP_GUIDE.md](USER_SETUP_GUIDE.md) - 配置指南
   - [interview-intel/SKILL_V6.md](interview-intel/SKILL_V6.md) - 完整文档

2. **社区支持**
   - GitHub Issues: 报告问题
   - GitHub Discussions: 提问讨论
   - 微信群: [扫码加入]

3. **联系我们**
   - Email: support@example.com
   - 反馈表单: [填写反馈]

---

## 📊 问题统计

**最常见的 5 个问题：**

1. 安装依赖失败 (35%)
2. 简历读取错误 (25%)
3. 找不到生成的文件 (15%)
4. 匹配度不准确 (15%)
5. 网络超时 (10%)

**解决率：**
- 自助解决: 80%
- 社区帮助: 15%
- 需要支持: 5%

---

**文档版本**: v1.0
**最后更新**: 2026-02-06
**贡献者**: Interview Intel Team & Community

**帮助改进这份文档**: [提交修改](https://github.com/your-repo/InterviewIntel/edit/main/FAQ.md)
