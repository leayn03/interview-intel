# Changelog

All notable changes to Interview Intel will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-02-27

### ⭐ 专业化流水线团队 (默认方式)

**核心升级**：
- 5个专业队友并行生成，加速 1.5x
- 成为默认执行方式，开箱即用

### 🆕 团队架构

- **Teammate A** (公司研究员) → 01_company_intel_brief.md
- **Teammate B** (简历分析师) → 02_resume_jd_matching.md
- **Teammate C** (面试教练) → 03_interview_prep_report.md
- **Teammate D** (文案专家) → 04_icebreaker_messages.md
- **Teammate E** (战略顾问) → 05_final_analysis_report.md

### ⚡ 性能提升

- **并行执行**: 阶段1(A+B) → 阶段2(C+D) → 阶段3(E)
- **加速效果**: 原串行 ~200s → 并行 ~135s (1.5x)

### 🔧 新增文件

- `pipeline_config.json` - 团队配置文件
- `scripts/pipeline_team.py` - 并行生成器
- `scripts/test_pipeline_team.py` - 测试脚本

### 📝 使用方式

**自然语言（推荐）**：
```
"帮我准备XX公司XX职位的面试"
```

**命令行**：
```bash
python scripts/pipeline_team.py \
  --company "XX公司" \
  --role "XX职位" \
  --candidate "你的名字" \
  --jd "jd.txt" \
  --resume "resume.pdf"
```

---

## [1.0.0] - 2026-02-08

### ⭐ 首个公开版本

**核心特性**：
- 一键生成面试准备包（5个标准Markdown文件）
- 事实验证协议，严格基于真实简历
- AI智能填充内容（STAR案例、面试话术）
