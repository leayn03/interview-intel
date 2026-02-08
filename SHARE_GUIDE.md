# Interview Intel - 分享与部署指南

**如何将 Interview Intel 分享给其他人使用**

版本：v6.2
更新日期：2026-02-06

---

## 📋 目录

1. [分享前的准备](#分享前的准备)
2. [清理个人数据](#清理个人数据)
3. [打包方式](#打包方式)
4. [部署方法](#部署方法)
5. [使用指导](#使用指导)

---

## 🔐 分享前的准备

### 重要提醒

在分享项目之前，**务必清理你的个人数据**，包括：

- ✅ 个人简历文件
- ✅ 生成的公司分析报告
- ✅ 个人配置文件
- ✅ 敏感信息

### 检查清单

```bash
# 1. 检查是否有个人数据
ls resumes/          # 查看简历文件
ls companies/        # 查看公司分析
cat ~/.interview_intel_config  # 查看配置文件

# 2. 备份你的数据（可选）
mkdir ~/interview_intel_backup
cp -r resumes companies ~/.interview_intel_config ~/interview_intel_backup/

# 3. 准备清理
```

---

## 🧹 清理个人数据

### 方式 1：完全清理（推荐分享时使用）

```bash
cd InterviewIntel

# 删除所有个人简历
rm -rf resumes/*.pdf
# 保留示例简历（可选）
git checkout resumes/master_resume_v1.0.pdf

# 删除所有公司分析
rm -rf companies/*

# 删除个人配置
rm ~/.interview_intel_config

# 重置简历注册表
cat > resumes/resume_registry.json << 'EOF'
{
  "versions": [],
  "tailored_versions": []
}
EOF

# 删除 Git 历史中的敏感信息（可选）
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch resumes/*.pdf" \
  --prune-empty --tag-name-filter cat -- --all
```

### 方式 2：选择性清理

```bash
# 只删除特定文件
rm resumes/你的简历.pdf
rm -rf companies/敏感公司/

# 保留其他示例
```

### 方式 3：使用清理脚本

```bash
# 创建清理脚本
cat > clean_personal_data.sh << 'EOF'
#!/bin/bash
echo "⚠️  这将删除所有个人数据"
read -p "确定继续? (yes/no) " confirm

if [ "$confirm" = "yes" ]; then
    echo "🧹 清理中..."
    rm -rf resumes/*.pdf
    rm -rf companies/*
    rm -f ~/.interview_intel_config
    echo "✅ 清理完成"
else
    echo "❌ 已取消"
fi
EOF

chmod +x clean_personal_data.sh
./clean_personal_data.sh
```

---

## 📦 打包方式

### 方式 1：Git 克隆（推荐）

**适用场景**: 分享给熟悉 Git 的用户

```bash
# 1. 清理个人数据
./clean_personal_data.sh

# 2. 提交到 Git
git add .
git commit -m "Clean personal data before sharing"

# 3. 推送到 GitHub（创建公开仓库）
git remote add origin https://github.com/your-username/InterviewIntel.git
git push -u origin main

# 4. 分享链接
# https://github.com/your-username/InterviewIntel
```

**接收者使用：**
```bash
git clone https://github.com/your-username/InterviewIntel.git
cd InterviewIntel
./setup.sh
```

### 方式 2：ZIP 压缩包（简单）

**适用场景**: 分享给不熟悉 Git 的用户

```bash
# 1. 清理个人数据
./clean_personal_data.sh

# 2. 创建 ZIP 包
cd ..
zip -r InterviewIntel_v6.2_$(date +%Y%m%d).zip InterviewIntel/ \
  -x "InterviewIntel/.git/*" \
  -x "InterviewIntel/__pycache__/*" \
  -x "InterviewIntel/*.pyc"

# 3. 分享文件
# - 网盘：百度网盘、Google Drive、Dropbox
# - 邮件：如果文件不大
# - 内网：公司共享文件夹
```

**接收者使用：**
```bash
# 解压
unzip InterviewIntel_v6.2_20260206.zip
cd InterviewIntel
./setup.sh
```

### 方式 3：Docker 镜像（高级）

**适用场景**: 企业级部署，确保环境一致

```dockerfile
# 创建 Dockerfile
cat > Dockerfile << 'EOF'
FROM python:3.9-slim

WORKDIR /app

# 安装依赖
RUN pip install pdfplumber --no-cache-dir

# 复制项目文件
COPY interview-intel/ ./interview-intel/
COPY resumes/ ./resumes/
COPY setup.sh ./

# 设置权限
RUN chmod +x setup.sh

# 创建目录
RUN mkdir -p companies .analytics/exports

CMD ["/bin/bash"]
EOF

# 构建镜像
docker build -t interview-intel:v6.2 .

# 保存镜像
docker save interview-intel:v6.2 | gzip > interview-intel-v6.2.tar.gz

# 分享文件
# 接收者加载: docker load < interview-intel-v6.2.tar.gz
```

---

## 🚀 部署方法

### 方法 1：个人电脑部署（最常见）

**步骤：**

1. **下载/克隆项目**
   ```bash
   # Git
   git clone https://github.com/your-username/InterviewIntel.git

   # 或解压 ZIP
   unzip InterviewIntel.zip
   ```

2. **运行安装脚本**
   ```bash
   cd InterviewIntel
   ./setup.sh
   ```

3. **添加简历**
   ```bash
   cp ~/my_resume.pdf resumes/张三-产品经理.pdf
   ```

4. **开始使用**
   ```bash
   python3 interview-intel/scripts/all_in_one_v6.1.py \
     --base-path . \
     --company "目标公司" \
     --role "目标职位" \
     --resume-version "张三-产品经理.pdf" \
     --years 3
   ```

### 方法 2：服务器部署（团队共享）

**适用场景**: 多人共享，中心化管理

```bash
# 1. 在服务器上克隆
ssh user@server
git clone https://github.com/your-username/InterviewIntel.git
cd InterviewIntel

# 2. 安装依赖
./setup.sh

# 3. 设置共享权限
chmod -R 755 .
chown -R shared-user:shared-group .

# 4. 每个用户创建自己的目录
mkdir -p resumes/张三 companies/张三
mkdir -p resumes/李四 companies/李四

# 5. 用户使用
python3 interview-intel/scripts/all_in_one_v6.1.py \
  --base-path /path/to/InterviewIntel \
  --company "公司" \
  --role "职位" \
  --resume-version "resumes/张三/简历.pdf"
```

### 方法 3：Docker 容器部署（隔离）

```bash
# 1. 运行容器
docker run -it --rm \
  -v ~/my_resumes:/app/resumes \
  -v ~/my_companies:/app/companies \
  interview-intel:v6.2

# 2. 容器内使用
python3 interview-intel/scripts/all_in_one_v6.1.py \
  --base-path /app \
  ...
```

### 方法 4：Claude Code 集成（推荐）

**步骤：**

1. **打开 Claude Code**
2. **打开项目**
   ```bash
   code /path/to/InterviewIntel
   ```
3. **直接对话使用**
   ```
   我想应聘 MiniMax 的产品经理职位
   JD: [粘贴内容]
   简历: resumes/张三-产品经理.pdf

   请帮我生成完整的面试准备包。
   ```

---

## 📚 使用指导

### 给接收者的快速指南

创建一个简单的 README 给用户：

```markdown
# 快速开始

## 1. 安装
\`\`\`bash
./setup.sh
\`\`\`

## 2. 添加你的简历
\`\`\`bash
cp ~/你的简历.pdf resumes/你的名字-职位.pdf
\`\`\`

## 3. 生成面试准备包
\`\`\`bash
python3 interview-intel/scripts/all_in_one_v6.1.py \\
  --base-path . \\
  --company "公司名" \\
  --role "职位名" \\
  --resume-version "你的简历.pdf" \\
  --years 工作年限
\`\`\`

## 4. 查看生成的文件
\`\`\`bash
ls companies/公司名/
\`\`\`

## 详细文档
- [用户配置指南](USER_SETUP_GUIDE.md)
- [常见问题](FAQ.md)
- [完整文档](interview-intel/SKILL_V6.md)
```

### 培训材料

**新用户培训大纲**：

1. **介绍（5分钟）**
   - 工具用途
   - 核心功能
   - 示例演示

2. **安装演示（5分钟）**
   - 克隆项目
   - 运行 setup.sh
   - 验证安装

3. **第一次使用（10分钟）**
   - 准备简历
   - 准备 JD
   - 运行脚本
   - 查看输出

4. **阅读报告（10分钟）**
   - 5个文件的作用
   - 阅读顺序
   - 如何使用

5. **答疑（5分钟）**

**总时长**: 35分钟

### 视频教程（可录制）

**建议录制 3 个短视频**：

1. **安装视频（2分钟）**
   - 下载项目 → 运行 setup.sh → 验证成功

2. **使用视频（3分钟）**
   - 添加简历 → 运行脚本 → 查看输出

3. **Claude Code 视频（2分钟）**
   - 打开项目 → 对话生成 → 查看结果

---

## 🎯 不同场景的分享方案

### 场景 1：分享给同事/朋友（1-2人）

**方案**: 直接发送 ZIP 包 + 简短说明

```bash
# 1. 打包
zip -r InterviewIntel.zip InterviewIntel/

# 2. 发送文件 + 说明
# 邮件内容：
#
# 这是一个面试准备工具，可以帮你：
# 1. 分析公司背景
# 2. 匹配简历和JD
# 3. 生成面试策略
#
# 使用方法：
# 1. 解压文件
# 2. 运行 ./setup.sh
# 3. 查看 USER_SETUP_GUIDE.md
#
# 有问题随时找我！
```

### 场景 2：分享给团队（5-10人）

**方案**: 内网部署 + 培训会

```bash
# 1. 部署到共享服务器
git clone https://github.com/your-username/InterviewIntel.git
cd InterviewIntel
./setup.sh

# 2. 组织培训会
# - 演示使用
# - 答疑解惑

# 3. 提供内部文档
# - 内网访问地址
# - 使用手册
# - 联系人信息
```

### 场景 3：开源给社区（公开）

**方案**: GitHub + 完整文档 + 社区支持

```bash
# 1. 准备开源
- 添加 LICENSE 文件（MIT 推荐）
- 完善 README.md
- 添加贡献指南 CONTRIBUTING.md

# 2. 推送到 GitHub
git remote add origin https://github.com/your-username/InterviewIntel.git
git push -u origin main

# 3. 宣传
- 发布到社区（Reddit, Hacker News）
- 写博客介绍
- 录制演示视频

# 4. 维护
- 回复 Issues
- 审核 Pull Requests
- 发布新版本
```

---

## 🔧 高级配置

### 企业定制版

如果要为企业定制：

```bash
# 1. Fork 项目
# 2. 创建企业分支
git checkout -b enterprise

# 3. 定制内容
- 添加公司 Logo
- 修改默认配置
- 集成内部系统（SSO、LDAP）

# 4. 维护企业版本
git merge main  # 定期合并主分支更新
```

### 白标版本

如果要创建白标版本（去除品牌）：

```bash
# 搜索并替换
find . -type f -name "*.md" -o -name "*.py" | xargs sed -i '' 's/Interview Intel/YourBrand/g'
```

---

## 📞 支持渠道

### 为接收者提供支持

**建议提供的支持方式**：

1. **文档**
   - [USER_SETUP_GUIDE.md](USER_SETUP_GUIDE.md)
   - [FAQ.md](FAQ.md)
   - [SKILL_V6.md](interview-intel/SKILL_V6.md)

2. **联系方式**
   - 你的邮箱
   - 微信/Slack 群
   - GitHub Issues

3. **培训**
   - 首次使用演示
   - 答疑时间
   - 录制视频教程

---

## ✅ 分享检查清单

在分享之前，确保：

- [ ] 已清理所有个人数据
- [ ] README.md 清晰易懂
- [ ] setup.sh 可以正常运行
- [ ] 示例文件可以正常生成
- [ ] 文档链接都有效
- [ ] LICENSE 文件已添加
- [ ] 联系方式已提供
- [ ] 已测试安装流程

---

## 📊 分享统计（可选）

如果你想了解分享效果：

```bash
# 添加简单的使用统计
cat >> interview-intel/scripts/all_in_one_v6.1.py << 'EOF'
# 使用统计（匿名）
import hashlib
import json
from datetime import datetime

def log_usage():
    # 记录使用（不包含敏感信息）
    usage = {
        'timestamp': datetime.now().isoformat(),
        'version': 'v6.2'
    }
    # 保存或发送...
EOF
```

---

## 🎉 开始分享吧！

```bash
# 1. 清理数据
./clean_personal_data.sh

# 2. 打包
zip -r InterviewIntel.zip InterviewIntel/

# 3. 分享
# 选择适合的方式分享给朋友、同事或社区

# 4. 提供支持
# 帮助他们顺利使用
```

**让更多人受益于这个工具！** 🚀

---

**文档版本**: v1.0
**最后更新**: 2026-02-06
**维护者**: Interview Intel Team
