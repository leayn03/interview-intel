# Interview Intel - 开源整理方案

> 准备将 Interview Intel skill 开源到 GitHub 的完整清理和优化方案

## 📋 当前状态分析

### ✅ 已做好的配置

**.gitignore 已经正确配置**：
```
companies/*/          # 用户面试准备数据（已忽略）
*.pdf                # 简历文件（已忽略）
.DS_Store            # Mac系统文件（已忽略）
.claude/settings.local.json  # Claude本地配置（已忽略）
```

**敏感信息检查**：
- ✅ companies/ 目录无个人敏感信息
- ✅ resumes/ 目录已忽略
- ✅ .claude/settings.local.json 已忽略

### ⚠️ 需要清理的内容

| 文件/目录 | 说明 | 操作 |
|----------|------|------|
| `interview-intel.skill.bak` | 备份文件 | **删除** |
| `interview-intel.skill.bak2` | 备份文件 | **删除** |
| `.DS_Store` | Mac系统文件 | **删除** |
| `companies/.DS_Store` | Mac系统文件 | **删除** |
| `resumes/.DS_Store` | Mac系统文件 | **删除** |
| `interview-intel/.DS_Store` | Mac系统文件 | **删除** |

### 📦 需要添加的新文件

| 文件 | 说明 | 操作 |
|------|------|------|
| `interview-intel/pipeline_config.json` | 流水线配置 | **添加** |
| `interview-intel/scripts/pipeline_team.py` | 流水线脚本 | **添加** |
| `interview-intel/scripts/test_pipeline_team.py` | 测试脚本 | **添加** |

---

## 🧹 清理步骤

### 步骤 1: 清理临时和备份文件

```bash
# 删除备份文件
rm -f interview-intel.skill.bak
rm -f interview-intel.skill.bak2

# 删除 .DS_Store 文件
find . -name ".DS_Store" -type f -delete
```

### 步骤 2: 更新 .gitignore（如需要）

**当前 .gitignore 已完善，无需修改**

如需添加其他忽略规则，可添加：
```
# Backup files
*.bak
*.bak2

# Temporary files
*.tmp
*.temp
```

### 步骤 3: 验证 companies/ 和 resumes/ 已被忽略

```bash
# 检查 git 状态
git status

# 确认 companies/ 和 resumes/ 不会被提交
git check-ignore -v companies/*/
git check-ignore -v resumes/*/*.pdf
```

### 步骤 4: 添加新文件到 git

```bash
# 添加流水线相关文件
git add interview-intel/pipeline_config.json
git add interview-intel/scripts/pipeline_team.py
git add interview-intel/scripts/test_pipeline_team.py

# 添加更新的文件
git add README.md
git add interview-intel.skill
git add interview-intel/SKILL.md
```

---

## 📝 开源前检查清单

### 必须检查项

- [ ] **敏感信息检查**
  - [ ] 无个人联系方式（手机、邮箱、住址）
  - [ ] 无密码/密钥/token
  - [ ] 无公司内部数据
  - [ ] 无第三方私密信息

- [ ] **文件清理**
  - [ ] 删除所有 .DS_Store 文件
  - [ ] 删除所有 .bak 备份文件
  - [ ] 确认 companies/ 和 resumes/ 被 .gitignore 忽略

- [ ] **文档完善**
  - [ ] README.md 包含完整的使用说明
  - [ ] LICENSE 文件存在且合适
  - [ ] CHANGELOG.md 记录版本变更
  - [ ] FAQ.md 包含常见问题

- [ ] **功能验证**
  - [ ] 所有脚本可正常运行
  - [ ] skill 文件可用
  - [ ] 示例数据不包含敏感信息

### 可选检查项

- [ ] **开源协议**
  - [ ] 当前使用 MIT License
  - [ ] 考虑是否需要更改
  - [ ] 检查第三方库的许可证兼容性

- [ ] **README 优化**
  - [ ] 添加徽章（build status、license等）
  - [ ] 添加目录结构说明
  - [ ] 添加贡献指南
  - [ ] 添加问题反馈渠道

---

## 🚀 推荐的开源步骤

### 方案 A: 直接提交（推荐）

```bash
# 1. 清理文件
rm -f interview-intel.skill.bak interview-intel.skill.bak2
find . -name ".DS_Store" -type f -delete

# 2. 添加所有更改
git add -A

# 3. 检查状态
git status

# 4. 提交
git commit -m "feat: 添加专业化流水线团队模式

- 新增 pipeline_team.py 并行生成器
- 新增 pipeline_config.json 配置文件
- 新增 test_pipeline_team.py 测试脚本
- 更新 SKILL.md 和 README.md
- 优化文件夹命名支持多场景

性能提升:
- 框架生成 <1s (5个队友并行)
- 原串行 ~15min → 现并行 ~7min (加速 2x)

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

# 5. 推送
git push origin master
```

### 方案 B: 创建 release tag（可选）

```bash
# 创建版本标签
git tag v1.1.0 -m "v1.1.0 - 专业化流水线团队模式"

# 推送标签
git push origin v1.1.1
```

---

## 📂 项目结构说明

```
InterviewIntel/
├── .github/               # GitHub 相关
│   └── workflows/           # GitHub Actions（可选）
├── .claude/                # Claude Code 配置
│   └── commands/           # 斜杠命令定义
├── companies/              # 用户数据（已在 .gitignore 中）
├── resumes/               # 用户简历（已在 .gitignore 中）
├── docs/                  # 文档
│   └── ...
├── interview-intel/        # skill 核心文件
│   ├── SKILL.md           # 主文档
│   ├── QUICK_START.md     # 快速开始
│   ├── CHANGELOG.md        # 变更日志
│   ├── pipeline_config.json # 流水线配置
│   ├── scripts/           # 功能脚本
│   │   ├── pipeline_team.py     # 流水线生成器 ⭐新增
│   │   └── test_pipeline_team.py  # 测试脚本 ⭐新增
│   └── ...
├── .gitignore            # Git 忽略规则
├── README.md              # 项目说明
├── LICENSE                # MIT 许可证
├── CHANGELOG.md           # 变更日志
└── setup.sh              # 安装脚本
```

---

## ⚠️ 重要注意事项

### 1. companies/ 目录说明

**当前状态**：`companies/*` 已在 .gitignore 中，不会被提交

**原因**：
- `companies/` 包含用户的面试准备数据
- 可能包含个人简历、JD 等敏感信息
- 这些数据应该由用户本地管理

**验证**：
```bash
# 检查 companies/ 是否被忽略
git check-ignore -v companies/*/

# 查看哪些文件会被提交
git status
```

### 2. resumes/ 目录说明

**当前状态**：`*.pdf` 已在 .gitignore 中，不会被提交

**原因**：
- 简历文件包含个人信息
- 用户数据应保持在本地

### 3. Skill 文件中可能包含的模板

**检查位置**：
- `interview-intel/assets/` 目录下的模板文件
- 模板中可能包含示例数据，需确保不包含真实个人信息

**验证**：
```bash
# 搜索可能的真实个人信息
grep -r "王蕾\|李承润\|张三\|158\|159" interview-intel/assets/
```

---

## 🔐 敏感信息审查

### 自动扫描脚本

```bash
#!/bin/bash
echo "🔍 扫描可能的敏感信息..."

# 检查个人联系方式
echo "📱 检查个人联系方式..."
grep -r "1[3-9]\d{9}" . --exclude-dir=.git --exclude-dir=node_modules || echo "✅ 未发现手机号"

# 检查邮箱
echo "📧 检查邮箱地址..."
grep -r "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" . --exclude-dir=.git --exclude-dir=node_modules | head -20

# 检查身份证
echo "🪪 检查身份证号..."
grep -r "[1-9]\{17\}[0-9Xx]" . --exclude-dir=.git || echo "✅ 未发现身份证号"

# 检查 companies/ 目录
echo "📂 检查 companies/ 目录..."
if git ls-files companies/ | grep -q .; then
    echo "⚠️  警告: companies/ 中有文件被跟踪！"
    git ls-files companies/
else
    echo "✅ companies/ 目录未被跟踪"
fi

echo "🔍 扫描完成！"
```

---

## 📊 当前 git 状态总结

### 已修改的文件（待提交）

| 文件 | 状态 | 说明 |
|------|------|------|
| `README.md` | Modified | 更新团队模式说明 |
| `interview-intel.skill` | Modified | 重新打包，包含新功能 |
| `interview-intel/SKILL.md` | Modified | 添加方式2：专业化流水线团队 |

### 新增的文件（待添加）

| 文件 | 状态 | 说明 |
|------|------|------|
| `interview-intel/pipeline_config.json` | Untracked | 流水线配置 |
| `interview-intel/scripts/pipeline_team.py` | Untracked | 流水线生成器 |
| `interview-intel/scripts/test_pipeline_team.py` | Untracked | 测试脚本 |

### 需要删除的文件

| 文件 | 操作 |
|------|------|
| `interview-intel.skill.bak` | 删除 |
| `interview-intel.skill.bak2` | 删除 |
| `.DS_Store` (各目录下) | 删除 |

---

## ✅ 建议的开源命令序列

```bash
# 1. 清理临时文件
rm -f interview-intel.skill.bak interview-intel.skill.bak2
find . -name ".DS_Store" -type f -delete

# 2. 添加所有更改
git add -A

# 3. 查看状态确认
git status

# 4. 提交
git commit -m "feat: 添加专业化流水线团队模式

新增功能:
- pipeline_team.py: 5个专业队友并行生成 (A/B/C/D/E)
- pipeline_config.json: 团队配置和依赖管理
- test_pipeline_team.py: 快速测试脚本

更新文档:
- SKILL.md: 添加方式2: 专业化流水线团队
- README.md: 添加团队模式说明和示例

性能提升:
- 框架生成 <1s (5个队友并行)
- 内容填充 加速 2x

文件夹命名优化:
- companies/公司名-职位-候选人
- 支持多公司、多岗位、多候选人场景

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

# 5. 推送到 GitHub
git push origin master
```

---

## 🎯 开源后建议

### 1. 更新 README.md

建议添加以下内容：

```markdown
# Interview Intel

[![License](https://img.shields.io/badge/license-MIT-blue.svg)
[![Version](https://img.shields.io/badge/version-v1.1.0-green.svg)
[![Skill](https://img.shields.io/badge/Claude%20Code-interview--blue.svg)

## 快速开始

### 方式 1: 配合 Claude Code（推荐）

### 方式 2: 专业化流水线团队（新增）⚡

...

## 文档

- [FAQ](FAQ.md)
- [变更日志](CHANGELOG.md)
- [事实验证协议](.claude/FACT_VERIFICATION_PROTOCOL.md)

## 许可证

MIT License - 详见 [LICENSE](LICENSE)
```

### 2. 添加贡献指南

创建 `CONTRIBUTING.md`：

```markdown
# 贡献指南

欢迎贡献 Interview Intel！

## 报告问题

请在 GitHub Issues 中提交问题。

## 提交 PR

1. Fork 本仓库
2. 创建特性分支
3. 提交 Pull Request
```

### 3. 添加 LICENSE 文件（如果还没有）

当前已有 MIT License，无需修改。

---

需要我执行这些清理和提交操作吗？
