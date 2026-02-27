# Changelog

All notable changes to Interview Intel will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-08

### ⭐ 首个公开版本 (Initial Release)

**核心特性**：
- 一键生成面试准备包（5个标准Markdown文件）
- 事实验证协议（Fact Verification Protocol v1.0）
- 严格基于真实简历，零幻觉保证
- AI智能填充内容（STAR案例、面试话术）

### 🆕 主要功能

#### 1. 一键生成工作流
- **all_in_one.py**: 主工作流脚本
  - 输入：公司名 + 职位 + JD + 简历
  - 输出：5个完整Markdown文件
  - 自动执行：文件创建、简历读取、网络搜索、内容填充

#### 2. 事实验证协议 (Fact Verification Protocol)
- 零容忍原则：绝不编造用户信息
- 三阶段验证：简历读取 → 信息确认 → 事实核查
- 自动触发：通过settings.local.json hooks自动启用
- PDF读取失败时明确提示，不继续使用编造数据

#### 3. 生成的文件（5个标准文件）
- `01_company_intel_brief.md` - 公司情报简报
- `02_resume_jd_matching.md` - 简历-JD匹配分析
- `03_interview_prep_report.md` - 面试准备报告
- `04_icebreaker_messages.md` - 破冰开场白
- `05_final_analysis_report.md` - 最终分析报告

#### 4. 辅助脚本
- `setup_company_folder.py` - 文件夹结构创建
- `extract_jd_keywords.py` - JD关键词提取
- `resume_manager.py` - 简历版本管理
- `interview_tracker.py` - 面试进度追踪
- `analytics_generator.py` - 统计分析

### 🎯 成功案例

- **词元无限**（AI Coding产品经理）- 95%匹配度
- **阿里云**（AI Coding产品专家）- 95%匹配度

### 📚 技术栈

- Python 3.x
- Claude Code / Claude.ai
- pdfplumber（PDF文本提取）
- Markdown
- JSON（面试追踪）

### 📄 许可证

MIT License

### 🙏 致谢

感谢所有早期用户和测试者的反馈！

---

## [0.x] - 开发版本（未公开发布）

### 内部测试版本
- v6.1 - 事实验证协议测试
- v6.0 - 基础面试准备包生成
- v5.0 - 一键执行工作流
- v4.0 - 智能匹配和面试博弈
- v3.0 - 基础架构和追踪系统

---

## 版本说明

从v1.0.0开始，采用语义化版本（Semantic Versioning）：
- **主版本（Major）**：重大变更，可能不兼容
- **次版本（Minor）**：新增功能，向后兼容
- **补丁版本（Patch）**：Bug修复

---

**相关链接**:
- [GitHub Releases](https://github.com/your-username/InterviewIntel/releases)
- [GitHub Issues](https://github.com/your-username/InterviewIntel/issues)
