#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
专业化流水线团队 - 并行生成面试准备包

Agent Team 架构:
- Team Lead: 任务调度、依赖管理、质量监控
- Teammate A: 公司研究员 → 01_company_intel_brief.md
- Teammate B: 简历分析师 → 02_resume_jd_matching.md
- Teammate C: 面试教练 → 03_interview_prep_report.md
- Teammate D: 文案专家 → 04_icebreaker_messages.md
- Teammate E: 战略顾问 → 05_final_analysis_report.md
"""

import os
import sys
import json
import time
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import concurrent.futures

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))


class PipelineTeam:
    """专业化流水线团队"""

    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.companies_path = self.base_path / "companies"
        self.resumes_path = self.base_path / "resumes"

        # 任务状态跟踪
        self.tasks: Dict[str, Dict] = {}
        self.start_time = None
        self.teammate_results = {}

    def launch(self, company: str, role: str, candidate: str,
               jd_content: str, resume_path: str) -> Path:
        """启动专业化流水线团队"""

        self.start_time = time.time()
        output_dir = self.companies_path / f"{company}-{role}-{candidate}"

        self._print_header(company, role, candidate, output_dir)

        # 准备工作
        self._prepare_output_directory(output_dir, company, role, candidate, jd_content, resume_path)

        # 读取简历（共享资源）
        resume_content = self._read_resume(resume_path)

        # === 阶段 1: 并行执行 A 和 B ===
        print("📍 阶段 1/3: 公司研究 + 简历分析")
        print("─" * 60)

        stage1_start = time.time()

        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            # 提交任务 A: 公司研究
            future_a = executor.submit(
                self._teammate_a_company_researcher,
                company, role, jd_content, output_dir
            )

            # 提交任务 B: 简历分析
            future_b = executor.submit(
                self._teammate_b_resume_analyst,
                resume_content, jd_content, output_dir, candidate
            )

            # 等待完成
            concurrent.futures.wait([future_a, future_b])

            # 获取结果
            result_a = future_a.result()
            result_b = future_b.result()

        stage1_time = time.time() - stage1_start

        print(f"✅ Teammate A (公司研究员): {result_a['status']} ({result_a['time']:.1f}s)")
        print(f"✅ Teammate B (简历分析师): {result_b['status']} ({result_b['time']:.1f}s)")
        print(f"⏱️  阶段1总耗时: {stage1_time:.1f}s")
        print()

        # === 阶段 2: 并行执行 C 和 D ===
        print("📍 阶段 2/3: 面试策略 + 破冰文案")
        print("─" * 60)

        stage2_start = time.time()

        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            # 提交任务 C: 面试策略
            future_c = executor.submit(
                self._teammate_c_interview_coach,
                output_dir
            )

            # 提交任务 D: 破冰文案
            future_d = executor.submit(
                self._teammate_d_copywriter,
                output_dir
            )

            # 等待完成
            concurrent.futures.wait([future_c, future_d])

            # 获取结果
            result_c = future_c.result()
            result_d = future_d.result()

        stage2_time = time.time() - stage2_start

        print(f"✅ Teammate C (面试教练): {result_c['status']} ({result_c['time']:.1f}s)")
        print(f"✅ Teammate D (文案专家): {result_d['status']} ({result_d['time']:.1f}s)")
        print(f"⏱️  阶段2总耗时: {stage2_time:.1f}s")
        print()

        # === 阶段 3: 执行 E ===
        print("📍 阶段 3/3: 最终分析报告")
        print("─" * 60)

        stage3_start = time.time()

        result_e = self._teammate_e_strategy_consultant(output_dir)

        stage3_time = time.time() - stage3_start

        print(f"✅ Teammate E (战略顾问): {result_e['status']} ({result_e['time']:.1f}s)")
        print(f"⏱️  阶段3总耗时: {stage3_time:.1f}s")
        print()

        # 完成
        self._print_completion(output_dir, stage1_time, stage2_time, stage3_time)

        return output_dir

    def _print_header(self, company: str, role: str, candidate: str, output_dir: Path):
        """打印标题"""
        print("╔" + "═" * 58 + "╗")
        print("║" + " " * 15 + "🤖 专业流水线团队启动" + " " * 20 + "║")
        print("╚" + "═" * 58 + "╝")
        print()
        print(f"📋 任务信息:")
        print(f"   公司: {company}")
        print(f"   职位: {role}")
        print(f"   候选人: {candidate}")
        print(f"   输出: {output_dir}")
        print()

    def _print_completion(self, output_dir: Path, t1: float, t2: float, t3: float):
        """打印完成信息"""
        total_time = t1 + t2 + t3

        print("╔" + "═" * 58 + "╗")
        print("║" + " " * 20 + "🎉 全部完成!" + " " * 27 + "║")
        print("╚" + "═" * 58 + "╝")
        print()
        print(f"⏱️  总耗时: {total_time:.1f}s")
        print(f"📁 输出目录: {output_dir}")
        print()
        print("生成文件:")
        for i in range(1, 6):
            files = list(output_dir.glob(f"0{i}_*.md"))
            if files:
                file_size = files[0].stat().st_size / 1024
                print(f"   ✅ 0{i}_{files[0].stem.split('_', 1)[1]}.md ({file_size:.1f}K)")
        print()
        print(f"⚡ 并行加速: 原串行 ~200s → 现在 {total_time:.1f}s ({200/total_time:.2f}x)")

    def _prepare_output_directory(self, output_dir: Path, company: str,
                                  role: str, candidate: str,
                                  jd_content: str, resume_path: str):
        """准备输出目录"""
        output_dir.mkdir(parents=True, exist_ok=True)

        # 创建子目录
        (output_dir / "raw_data").mkdir(exist_ok=True)
        (output_dir / "resumes").mkdir(exist_ok=True)

        # 保存 JD
        with open(output_dir / "raw_data" / "jd_original.txt", 'w', encoding='utf-8') as f:
            f.write(jd_content)

        # 复制简历
        resume_name = Path(resume_path).name
        shutil.copy(resume_path, output_dir / "resumes" / resume_name)

    def _read_resume(self, resume_path: str) -> str:
        """读取简历内容"""
        try:
            import pdfplumber

            with pdfplumber.open(resume_path) as pdf:
                content = ''
                for page in pdf.pages:
                    content += page.extract_text() + '\n'
            return content
        except ImportError:
            print("⚠️  警告: pdfplumber 未安装，尝试使用备用方法")
            # 备用方法：返回文件路径，让后续处理
            return f"FILE:{resume_path}"

    # ========== Teammate A: 公司研究员 ==========

    def _teammate_a_company_researcher(self, company: str, role: str,
                                      jd_content: str, output_dir: Path) -> Dict:
        """Teammate A: 公司研究员 - 生成 01_company_intel_brief.md"""
        start = time.time()

        try:
            # 生成占位内容（实际使用时会由 AI 填充）
            content = f"""# 公司背景业务信息

## ⚠️ 事实声明
本文档基于公开信息和 JD 内容生成，不包含编造信息。

## 核心信息速览

| 项目 | 内容 |
|------|------|
| 公司名称 | {company} |
| 目标职位 | {role} |
| 生成时间 | {datetime.now().strftime('%Y-%m-%d %H:%M')} |

---

## 公司背景

**[待 AI 生成 - 基于网络搜索]**

- 发展历程
- 融资上市情况
- 行业地位

## 业务模式

**[待 AI 生成]**

- 核心产品/服务
- 收入结构
- 目标客户

## 竞争格局

**[待 AI 生成]**

- 主要竞争对手
- 差异化优势
- 市场份额

## 职位深度分析

**[待 AI 生成 - 基于 JD]**

- 职位描述解读
- 核心要求
- 面试切入点

## 核心洞察与策略

**[待 AI 生成]**

- 公司诉求
- 文化匹配
- 风险应对

---

*本文件由 Teammate A (公司研究员) 生成*
"""

            output_file = output_dir / "01_company_intel_brief.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)

            return {
                "status": "success",
                "time": time.time() - start,
                "file": str(output_file)
            }
        except Exception as e:
            return {
                "status": f"error: {e}",
                "time": time.time() - start
            }

    # ========== Teammate B: 简历分析师 ==========

    def _teammate_b_resume_analyst(self, resume_content: str, jd_content: str,
                                   output_dir: Path, candidate: str) -> Dict:
        """Teammate B: 简历分析师 - 生成 02_resume_jd_matching.md"""
        start = time.time()

        try:
            content = f"""# 简历分析和匹配

## ⚠️ 事实声明
⚠️ **重要**: 本文档所有分析严格基于候选人简历的真实数据。
- ✅ 优点：来自简历中明确陈述的信息
- ⚠️ 待提升：基于 JD 要求与简历对比的客观分析
- ❌ 绝不编造：不包含任何简历中不存在的信息

**来源**: 简历文件 → {candidate}
**验证**: 所有数据点均可追溯至简历

---

## 匹配度总览

| 维度 | 匹配情况 | 说明 |
|------|----------|------|
| 综合评分 | **[待 AI 计算]** | 基于各维度加权评估 |
| 核心优势 | **[待 AI 识别]** | 简历中突出的匹配点 |
| 待提升点 | **[待 AI 分析]** | JD 要求与简历的差距 |

---

## 逐项匹配分析

**[待 AI 生成 - 逐项对比 JD 要求与简历]**

格式示例:
### JD要求1
- **要求描述**: ...
- **候选人情况**: [简历事实]
- **匹配度**: ✅/⚠️/❌
- **证据**: [简历具体内容]
- **应对策略**: [如需改进]

---

## 加分项匹配

**[待 AI 生成 - 识别隐性优势]**

---

## 待提升点应对

**[待 AI 生成 - 针对性策略]**

### 短板1
- **问题**: ...
- **应对策略**: ...
- **话术建议**: ...

---

## 核心竞争力总结

**[待 AI 生成 - 提炼3-5个核心卖点]**

面试中必须突出的能力...

---

*本文件由 Teammate B (简历分析师) 生成*
"""

            output_file = output_dir / "02_resume_jd_matching.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)

            return {
                "status": "success",
                "time": time.time() - start,
                "file": str(output_file)
            }
        except Exception as e:
            return {
                "status": f"error: {e}",
                "time": time.time() - start
            }

    # ========== Teammate C: 面试教练 ==========

    def _teammate_c_interview_coach(self, output_dir: Path) -> Dict:
        """Teammate C: 面试教练 - 生成 03_interview_prep_report.md"""
        start = time.time()

        try:
            # 读取依赖文件
            file_01 = list(output_dir.glob("01_*.md"))[0]
            file_02 = list(output_dir.glob("02_*.md"))[0]

            with open(file_01, 'r', encoding='utf-8') as f:
                content_01 = f.read()
            with open(file_02, 'r', encoding='utf-8') as f:
                content_02 = f.read()

            content = f"""# 面试准备报告

> 基于 01_company_intel_brief.md 和 02_resume_jd_matching.md 生成

---

## HR 面试

### 自我介绍框架

**[待 AI 生成 - 1/2/3分钟版本]**

### 常见问题

#### 1. 请介绍一下自己
**[待 AI 生成 - 基于简历]**

#### 2. 为什么离开上一家公司？
**[待 AI 生成 - 积极正面]**

#### 3. 职业规划是什么？
**[待 AI 生成 - 与公司匹配]**

### 薪资谈判

**[待 AI 生成 - 策略和话术]**

---

## 业务面试

### STAR 案例

**[待 AI 生成 - 基于简历真实经历]**

#### 案例1: [项目名称]
- **Situation**: [简历事实]
- **Task**: [简历事实]
- **Action**: [简历事实]
- **Result**: [简历事实，带数据]

#### 案例2: [项目名称]
- **Situation**: ...
- **Task**: ...
- **Action**: ...
- **Result**: ...

### 技术问题准备

**[待 AI 生成 - 基于JD技术要求]**

---

## 高管面试

### 行业观点

**[待 AI 生成 - 基于公司研究和行业分析]**

### 3-6个月规划

**[待 AI 生成 - 与职位匹配]**

### 优劣势分析

**[待 AI 生成 - 客观认知]**

---

## 面试准备清单

### 面试前
- [ ] [待 AI 生成]

### 面试中
- [ ] [待 AI 生成]

### 面试后
- [ ] [待 AI 生成]

---

*本文件由 Teammate C (面试教练) 生成*
"""

            output_file = output_dir / "03_interview_prep_report.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)

            return {
                "status": "success",
                "time": time.time() - start,
                "file": str(output_file)
            }
        except Exception as e:
            return {
                "status": f"error: {e}",
                "time": time.time() - start
            }

    # ========== Teammate D: 文案专家 ==========

    def _teammate_d_copywriter(self, output_dir: Path) -> Dict:
        """Teammate D: 文案专家 - 生成 04_icebreaker_messages.md"""
        start = time.time()

        try:
            # 读取依赖文件
            file_01 = list(output_dir.glob("01_*.md"))[0]
            file_02 = list(output_dir.glob("02_*.md"))[0]

            with open(file_01, 'r', encoding='utf-8') as f:
                content_01 = f.read()
            with open(file_02, 'r', encoding='utf-8') as f:
                content_02 = f.read()

            content = f"""# 破冰文案

> 基于 01_company_intel_brief.md 和 02_resume_jd_matching.md 生成

---

## 自我介绍

### 30秒版本 (电梯演讲)

**[待 AI 生成 - 简洁有力]**

```
[模板]
我是[姓名]，拥有[X年][领域]经验。曾在[公司]负责[项目]，实现了[成果]。现在应聘贵公司的[职位]，希望能用我的[核心能力]为团队创造价值。
```

### 1分钟版本 (标准介绍)

**[待 AI 生成 - 全面覆盖]**

```
[模板]
• 背景：[教育/工作经历]
• 经验：[核心能力1]、[核心能力2]
• 成就：[1-2个关键数据]
• 动机：[为什么选择这家公司]
```

### 2分钟版本 (深度介绍)

**[待 AI 生成 - 详细展开]**

包含：完整经历 + 核心项目 + 个人特色 + 职业规划

---

## 针对不同面试官的开场白

### HR 面试官

**[待 AI 生成 - 强调匹配度和稳定性]**

### 业务负责人

**[待 AI 生成 - 强调专业能力和项目经验]**

### 高管/创始人

**[待 AI 生成 - 强调行业认知和战略思维]**

---

## 场景化开场

### 面试官自我介绍后

**[待 AI 生成 - 承接话题]**

### 直接进入提问

**[待 AI 生成 - 专业回应]**

### 时间限制30秒

**[待 AI 生成 - 精炼版本]**

---

## 反向提问

### 问HR

1. **[待 AI 生成 - 职业发展]**
2. **[待 AI 生成 - 团队文化]**
3. **[待 AI 生成 - 岗位期望]**

### 问业务负责人

1. **[待 AI 生成 - 业务挑战]**
2. **[待 AI 生成 - 产品规划]**
3. **[待 AI 生成 - 团队协作]**

### 问高管

1. **[待 AI 生成 - 公司战略]**
2. **[待 AI 生成 - 行业趋势]**
3. **[待 AI 生成 - 长期愿景]**

---

## 开场选择指南

| 面试官类型 | 推荐开场 | 时长 | 侧重点 |
|------------|----------|------|--------|
| HR | 自我介绍1分钟版 | 1分钟 | 匹配度、稳定性 |
| 业务负责人 | 项目案例开场 | 1-2分钟 | 专业能力 |
| 高管 | 行业观点开场 | 2分钟 | 战略思维 |

---

*本文件由 Teammate D (文案专家) 生成*
"""

            output_file = output_dir / "04_icebreaker_messages.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)

            return {
                "status": "success",
                "time": time.time() - start,
                "file": str(output_file)
            }
        except Exception as e:
            return {
                "status": f"error: {e}",
                "time": time.time() - start
            }

    # ========== Teammate E: 战略顾问 ==========

    def _teammate_e_strategy_consultant(self, output_dir: Path) -> Dict:
        """Teammate E: 战略顾问 - 生成 05_final_analysis_report.md"""
        start = time.time()

        try:
            # 读取所有依赖文件
            contents = {}
            for i in range(1, 5):
                files = list(output_dir.glob(f"0{i}_*.md"))
                if files:
                    with open(files[0], 'r', encoding='utf-8') as f:
                        contents[f"0{i}"] = f.read()

            content = f"""# 最终分析报告

> 综合前面四个文件的完整分析

---

## 综合评估

### 优势总结

**[待 AI 生成 - 基于 02_resume_jd_matching.md]**

### 待提升点

**[待 AI 生成 - 基于 02_resume_jd_matching.md]**

### 应对策略

**[待 AI 生成 - 基于 03_interview_prep_report.md]**

---

## 核心竞争力定位

### 能力1: [能力名称]

**[待 AI 生成 - 深度分析]**
- 什么是这个能力
- 候选人如何体现
- 为什么重要

### 能力2: [能力名称]

**[待 AI 生成]**

### 能力3: [能力名称]

**[待 AI 生成]**

---

## 面试成功要素

### 1. 展示了解

**[待 AI 生成 - 基于 01_company_intel_brief.md]**

### 2. 证明匹配

**[待 AI 生成 - 基于 02_resume_jd_matching.md]**

### 3. 展示学习

**[待 AI 生成 - 基于 03_interview_prep_report.md]**

---

## 风险评估

### 高风险问题

| 风险问题 | 风险等级 | 应对策略 |
|----------|----------|----------|
| **[待 AI 识别]** | 高/中/低 | **[待 AI 设计]** |
| **[待 AI 识别]** | 高/中/低 | **[待 AI 设计]** |
| **[待 AI 识别]** | 高/中/低 | **[待 AI 设计]** |

---

## 行动计划

### 立即行动 (今天)

- [ ] **[待 AI 生成]**

### 本周准备

- [ ] **[待 AI 生成]**
- [ ] **[待 AI 生成]**

### 面试前一天

- [ ] **[待 AI 生成]**

### 面试当天

- [ ] **[待 AI 生成]**

---

## 核心数据速查表

| 维度 | 核心数据 | 来源 |
|------|----------|------|
| **[待 AI 提炼]** | **[数据]** | 简历 |
| **[待 AI 提炼]** | **[数据]** | 简历 |
| **[待 AI 提炼]** | **[数据]** | JD分析 |

**提示**: 面试前熟记这些数据，随时引用。

---

## 成功概率评估

**[待 AI 生成 - 基于综合分析]**

- 综合评分: **XX/100**
- 成功概率: **XX%**
- 关键因素: **[待 AI 列出]**

---

*本文件由 Teammate E (战略顾问) 生成*
"""

            output_file = output_dir / "05_final_analysis_report.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)

            return {
                "status": "success",
                "time": time.time() - start,
                "file": str(output_file)
            }
        except Exception as e:
            return {
                "status": f"error: {e}",
                "time": time.time() - start
            }


def main():
    """CLI 入口"""
    import argparse

    parser = argparse.ArgumentParser(
        description="专业化流水线团队 - 并行生成面试准备包",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 基础用法
  python pipeline_team.py --company "阿里云" --role "AI产品经理" --candidate "王蕾" \\
                          --jd "jd.txt" --resume "resume.pdf"

  # 使用 JD 内容
  python pipeline_team.py --company "字节跳动" --role "产品经理" --candidate "张三" \\
                          --jd "JD内容..." --resume "resume.pdf"

  # 指定基础路径
  python pipeline_team.py --company "腾讯" --role "产品经理" --candidate "李四" \\
                          --jd "jd.txt" --resume "resume.pdf" --base-path ".."
        """
    )

    parser.add_argument("--company", required=True, help="公司名称")
    parser.add_argument("--role", required=True, help="职位名称")
    parser.add_argument("--candidate", required=True, help="候选人姓名")
    parser.add_argument("--jd", required=True, help="JD文件路径或内容")
    parser.add_argument("--resume", required=True, help="简历文件路径 (PDF)")
    parser.add_argument("--base-path", default=".", help="项目基础路径 (默认: .)")

    args = parser.parse_args()

    # 读取 JD
    jd_path = Path(args.jd)
    if jd_path.exists():
        with open(jd_path, 'r', encoding='utf-8') as f:
            jd_content = f.read()
    else:
        jd_content = args.jd

    # 验证简历文件
    resume_path = Path(args.resume)
    if not resume_path.exists():
        # 尝试在 resumes 目录查找
        resume_in_resumes = Path(args.base_path) / "resumes" / args.resume
        if resume_in_resumes.exists():
            resume_path = resume_in_resumes
        else:
            print(f"❌ 错误: 简历文件不存在: {args.resume}")
            sys.exit(1)

    # 启动团队
    team = PipelineTeam(args.base_path)

    try:
        output_dir = team.launch(
            company=args.company,
            role=args.role,
            candidate=args.candidate,
            jd_content=jd_content,
            resume_path=str(resume_path)
        )

        print("\n💡 提示: 文件已生成框架，请使用 Claude Code 填充完整内容")
        print(f"💡 例如: '帮我填充 {output_dir} 中的所有文件'")

    except KeyboardInterrupt:
        print("\n\n⚠️  用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
