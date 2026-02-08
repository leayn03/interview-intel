#!/usr/bin/env python3
"""
Interview Strategy Generator

Generates interview attack-defense strategies based on resume and JD analysis.
Simulates HR, Business Lead, and Executive rounds.
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any


class InterviewStrategy:
    """Generates comprehensive interview preparation strategies."""

    def __init__(self, company_path: str):
        """
        Initialize the strategy generator.

        Args:
            company_path: Path to company folder
        """
        self.company_path = Path(company_path)

    def generate_full_strategy(
        self,
        resume_version: str,
        jd_analysis: Dict[str, Any],
        resume_gaps: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Generate complete interview strategy for all rounds.

        Args:
            resume_version: Resume version used
            jd_analysis: JD analysis data
            resume_gaps: List of identified gaps in resume

        Returns:
            Dictionary with strategy for each round
        """
        strategy = {
            "generated_at": datetime.now().isoformat(),
            "resume_version": resume_version,
            "role": jd_analysis.get('role', 'Unknown'),
            "round_1_hr": self._generate_hr_strategy(resume_gaps or []),
            "round_2_business": self._generate_business_strategy(jd_analysis),
            "round_3_executive": self._generate_executive_strategy(jd_analysis),
            "killer_cases": self._generate_killer_cases(jd_analysis),
            "risk_mitigation": self._generate_risk_mitigation(resume_gaps or [])
        }

        return strategy

    def _generate_hr_strategy(self, resume_gaps: List[str]) -> Dict[str, Any]:
        """
        Generate HR round (screening) strategy.

        Focus: Stability, salary, culture fit, risk points
        """
        strategy = {
            "focus_areas": [
                "职业稳定性",
                "薪资期望合理性",
                "离职原因",
                "文化契合度"
            ],
            "risk_points": self._identify_hr_risks(resume_gaps),
            "defense_scripts": [],
            "preparation_tips": [
                "准备 3 个离职原因（真实但积极）",
                "准备薪资区间（参考市场价 + 20%）",
                "准备对公司的了解（产品、文化、价值观）",
                "准备职业规划（3-5 年清晰目标）"
            ]
        }

        # Generate defense scripts for each risk
        for risk in strategy["risk_points"]:
            script = self._generate_defense_script(risk)
            strategy["defense_scripts"].append(script)

        return strategy

    def _identify_hr_risks(self, resume_gaps: List[str]) -> List[Dict[str, str]]:
        """Identify HR-level risks from resume."""
        risks = []

        # Common HR concerns
        risk_templates = [
            {
                "risk_type": "频繁跳槽",
                "concern": "候选人稳定性",
                "trigger": "2年内超过2次跳槽"
            },
            {
                "risk_type": "空窗期",
                "concern": "空窗期间在做什么",
                "trigger": "简历中出现3个月以上空白"
            },
            {
                "risk_type": "专业不对口",
                "concern": "为什么转行",
                "trigger": "专业与岗位不匹配"
            },
            {
                "risk_type": "薪资跳跃",
                "concern": "期望是否过高",
                "trigger": "期望涨幅超过40%"
            }
        ]

        # Check gaps against templates
        for gap in resume_gaps:
            for template in risk_templates:
                if gap.lower() in template["risk_type"].lower():
                    risks.append(template)

        return risks

    def _generate_defense_script(self, risk: Dict[str, str]) -> Dict[str, str]:
        """Generate defense script for a specific risk."""
        scripts = {
            "频繁跳槽": {
                "bad_answer": "因为公司不好 / 老板不行 / 钱少事多",
                "good_answer": "每一次变动都是为了更大的成长空间。[具体公司] 让我掌握了 [技能A]，[具体公司] 让我承担了更大的责任。现在我希望在一个长期平台深耕，贵司的 [具体优势] 正是我看重的。",
                "key_points": [
                    "正向表达：每次跳槽都有明确收获",
                    "表达稳定意愿：这次想长期发展",
                    "锚定对方优势：展示你做过功课"
                ]
            },
            "空窗期": {
                "bad_answer": "在家休息 / 找工作 / 没什么特别的",
                "good_answer": "这段时间我专注于 [具体学习/项目]。比如完成了 [课程/认证/开源项目]，提升了 [技能]。这让我对 [领域] 有了更深理解，也更清楚自己的职业方向。",
                "key_points": [
                    "主动学习：展示自驱力",
                    "成果证明：有具体产出",
                    "目标清晰：知道自己要什么"
                ]
            },
            "专业不对口": {
                "bad_answer": "原来专业不喜欢 / 找不到工作",
                "good_answer": "在 [原专业] 的学习让我具备了 [可迁移能力]。后来发现自己更擅长且热爱 [目标领域]，通过 [具体行动：项目/实习/自学] 系统性转型。过去 [X] 年的实战证明了我的选择和能力。",
                "key_points": [
                    "能力迁移：原专业不是废的",
                    "主动转型：有清晰规划",
                    "结果证明：用业绩说话"
                ]
            },
            "薪资跳跃": {
                "bad_answer": "市场价就是这样 / 我值这个价",
                "good_answer": "我的期望基于 [市场调研数据]，同时考虑了 [自身能力提升/责任增加/市场稀缺性]。更重要的是，我看重这个机会的 [成长空间/平台价值]，薪资在合理范围内可以谈。",
                "key_points": [
                    "数据支撑：不是拍脑袋",
                    "价值证明：我能带来什么",
                    "灵活态度：不是只看钱"
                ]
            }
        }

        risk_type = risk["risk_type"]
        return scripts.get(risk_type, {
            "bad_answer": "避免消极、推诿责任的回答",
            "good_answer": "真诚、具体、结果导向的回答",
            "key_points": ["真诚", "具体", "积极"]
        })

    def _generate_business_strategy(self, jd_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate business lead round strategy.

        Focus: Practical skills, problem-solving, case depth
        """
        strategy = {
            "focus_areas": [
                "实战能力验证",
                "问题解决思路",
                "技术深度",
                "业务理解"
            ],
            "likely_questions": self._predict_business_questions(jd_analysis),
            "killer_cases": [],  # To be filled
            "deep_dive_topics": self._identify_deep_dive_topics(jd_analysis),
            "preparation_tips": [
                "准备 2-3 个完整的 STAR 案例",
                "每个案例都要有数据支撑",
                "准备应对追问：为什么这样做？有没有更好的方案？",
                "准备技术细节：不能只讲表面"
            ]
        }

        return strategy

    def _predict_business_questions(self, jd_analysis: Dict[str, Any]) -> List[Dict[str, str]]:
        """Predict likely business round questions."""
        questions = []

        # Based on JD core competencies
        core_skills = jd_analysis.get('core_competencies', [])
        for skill in core_skills[:5]:  # Top 5
            questions.append({
                "question": f"请分享一个你在{skill.get('skill', 'N/A')}方面的实战案例？",
                "why_asked": f"验证你的 {skill.get('skill', 'N/A')} 能力是否扎实",
                "answer_framework": "STAR: 背景-任务-行动-结果，重点讲数据和难点"
            })

        # Common questions
        questions.extend([
            {
                "question": "遇到过最大的挑战是什么？如何解决的？",
                "why_asked": "考察问题解决能力和抗压能力",
                "answer_framework": "选择与JD相关的挑战，强调解决思路和结果"
            },
            {
                "question": "为什么想加入我们公司？",
                "why_asked": "考察动机和对公司的了解程度",
                "answer_framework": "产品/技术/团队/市场，选2-3个点深入讲"
            }
        ])

        return questions

    def _identify_deep_dive_topics(self, jd_analysis: Dict[str, Any]) -> List[str]:
        """Identify topics that interviewer might deep dive into."""
        topics = []

        # From JD keywords
        keywords = jd_analysis.get('keyword_frequency', {})
        top_keywords = list(keywords.keys())[:10]
        topics.extend(top_keywords)

        return topics

    def _generate_executive_strategy(self, jd_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate executive round strategy.

        Focus: Potential, business thinking, values, strategic vision
        """
        strategy = {
            "focus_areas": [
                "发展潜力",
                "商业思维",
                "价值观匹配",
                "战略眼光"
            ],
            "likely_questions": [
                {
                    "question": "你如何看待 [行业/技术] 的未来发展？",
                    "answer_direction": "展示行业洞察，结合趋势和数据，提出自己的判断"
                },
                {
                    "question": "你的 3-5 年职业规划是什么？",
                    "answer_direction": "清晰的成长路径，与公司发展方向一致"
                },
                {
                    "question": "你认为优秀的 [岗位] 需要具备哪些素质？",
                    "answer_direction": "结合JD要求+自身优势，展示自我认知"
                },
                {
                    "question": "你在选择工作时最看重什么？",
                    "answer_direction": "成长>平台>团队>薪资，展示长期主义"
                }
            ],
            "macro_topics": self._generate_macro_topics(jd_analysis),
            "preparation_tips": [
                "研究行业趋势和公司战略",
                "准备对行业的独到见解",
                "展示长期思考和规划",
                "保持真诚，不要过度包装"
            ]
        }

        return strategy

    def _generate_macro_topics(self, jd_analysis: Dict[str, Any]) -> List[Dict[str, str]]:
        """Generate macro/strategic topics for discussion."""
        topics = []

        role = jd_analysis.get('role', '')

        # Generic topics based on role
        if '产品' in role or 'Product' in role:
            topics.append({
                "topic": "AI 产品的商业化路径",
                "angle": "从技术到商业价值的转化"
            })
            topics.append({
                "topic": "toB 和 toC 产品的差异",
                "angle": "客户需求、交付方式、商业模式"
            })

        if '技术' in role or 'Engineer' in role:
            topics.append({
                "topic": "技术选型的trade-off",
                "angle": "新技术 vs 稳定性，创新 vs 成本"
            })

        return topics

    def _generate_killer_cases(self, jd_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate template for killer cases."""
        cases = [
            {
                "case_name": "核心成就案例",
                "requirement": "必须与JD高度相关，体现核心能力",
                "structure": {
                    "Situation": "3-5句话描述背景和挑战",
                    "Task": "明确目标和你的职责",
                    "Action": "5-8个关键行动步骤，突出难点和亮点",
                    "Result": "量化数据：X提升了Y%，Z节省了N小时"
                },
                "prep_checklist": [
                    "[ ] 数据准备好了吗？（前后对比）",
                    "[ ] 难点讲清楚了吗？（体现能力）",
                    "[ ] 能应对追问吗？（为什么这样做？）",
                    "[ ] 与JD匹配吗？（关键词对齐）"
                ]
            },
            {
                "case_name": "问题解决案例",
                "requirement": "展示分析能力和执行力",
                "structure": {
                    "Problem": "遇到什么问题，影响多大",
                    "Analysis": "如何分析根因",
                    "Solution": "提出什么方案，为什么选这个",
                    "Result": "问题解决效果"
                },
                "prep_checklist": [
                    "[ ] 问题是否足够有挑战性？",
                    "[ ] 分析过程是否体现思维深度？",
                    "[ ] 方案是否有创新性？",
                    "[ ] 结果是否可量化？"
                ]
            }
        ]

        return cases

    def _generate_risk_mitigation(self, resume_gaps: List[str]) -> Dict[str, Any]:
        """Generate risk mitigation strategies."""
        mitigation = {
            "identified_risks": resume_gaps,
            "mitigation_strategies": [],
            "proactive_disclosure": []
        }

        for gap in resume_gaps:
            strategy = {
                "risk": gap,
                "approach": "转劣势为优势",
                "tactics": self._get_mitigation_tactics(gap)
            }
            mitigation["mitigation_strategies"].append(strategy)

        return mitigation

    def _get_mitigation_tactics(self, risk: str) -> List[str]:
        """Get specific tactics for mitigating a risk."""
        tactics_map = {
            "经验不足": [
                "强调学习能力和快速上手案例",
                "突出相关项目的深度而非广度",
                "展示对行业/技术的深入理解"
            ],
            "跨行转型": [
                "强调可迁移技能",
                "展示转型的主动性和规划",
                "用实际成果证明转型成功"
            ],
            "技术栈不匹配": [
                "强调技术学习能力",
                "展示快速掌握新技术的案例",
                "突出底层思维和方法论"
            ]
        }

        for key, tactics in tactics_map.items():
            if key in risk:
                return tactics

        return ["主动说明，展示改进意愿和学习能力"]

    def export_strategy_report(
        self,
        strategy: Dict[str, Any],
        output_file: Optional[str] = None
    ) -> str:
        """
        Export strategy to markdown report.

        Args:
            strategy: Strategy data
            output_file: Output file path

        Returns:
            Path to generated report
        """
        if not output_file:
            role = strategy['role'].replace(' ', '_')
            output_file = self.company_path / f"interview_strategy_{role}.md"

        content = self._format_strategy_report(strategy)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

        return str(output_file)

    def _format_strategy_report(self, strategy: Dict[str, Any]) -> str:
        """Format strategy as markdown report."""
        report = f"""# 面试攻防策略

**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**目标职位**: {strategy['role']}
**简历版本**: {strategy['resume_version']}

---

## 一、Round 1: HR 筛选面试

### 关注重点
{self._format_list(strategy['round_1_hr']['focus_areas'])}

### 识别到的风险点
{self._format_risk_points(strategy['round_1_hr']['risk_points'])}

### 防坑话术
{self._format_defense_scripts(strategy['round_1_hr']['defense_scripts'])}

### 准备建议
{self._format_list(strategy['round_1_hr']['preparation_tips'])}

---

## 二、Round 2: 业务负责人面试

### 关注重点
{self._format_list(strategy['round_2_business']['focus_areas'])}

### 高概率问题
{self._format_questions(strategy['round_2_business']['likely_questions'])}

### 可能深挖的话题
{self._format_list(strategy['round_2_business']['deep_dive_topics'])}

### 准备建议
{self._format_list(strategy['round_2_business']['preparation_tips'])}

---

## 三、Round 3: 高管/终面

### 关注重点
{self._format_list(strategy['round_3_executive']['focus_areas'])}

### 高概率问题
{self._format_executive_questions(strategy['round_3_executive']['likely_questions'])}

### 宏观话题
{self._format_macro_topics(strategy['round_3_executive'].get('macro_topics', []))}

### 准备建议
{self._format_list(strategy['round_3_executive']['preparation_tips'])}

---

## 四、必杀技案例准备

{self._format_killer_cases(strategy['killer_cases'])}

---

## 五、风险缓解策略

{self._format_risk_mitigation(strategy['risk_mitigation'])}

---

**生成工具**: Interview Intel - Interview Strategy
"""
        return report

    def _format_list(self, items: List[str]) -> str:
        """Format list items."""
        return '\n'.join([f"- {item}" for item in items])

    def _format_risk_points(self, risks: List[Dict[str, str]]) -> str:
        """Format risk points."""
        if not risks:
            return "- 未识别到明显风险"

        output = []
        for risk in risks:
            output.append(f"**{risk['risk_type']}**: {risk['concern']}")
        return '\n\n'.join(output)

    def _format_defense_scripts(self, scripts: List[Dict[str, str]]) -> str:
        """Format defense scripts."""
        output = []
        for i, script in enumerate(scripts, 1):
            output.append(f"""
#### 话术 {i}

**❌ 错误示范**: {script.get('bad_answer', 'N/A')}

**✅ 正确示范**: {script.get('good_answer', 'N/A')}

**关键要点**:
{self._format_list(script.get('key_points', []))}
""")
        return '\n'.join(output)

    def _format_questions(self, questions: List[Dict[str, str]]) -> str:
        """Format predicted questions."""
        output = []
        for i, q in enumerate(questions, 1):
            output.append(f"""
#### 问题 {i}: {q['question']}

**为什么会问**: {q['why_asked']}

**回答框架**: {q['answer_framework']}
""")
        return '\n'.join(output)

    def _format_executive_questions(self, questions: List[Dict[str, str]]) -> str:
        """Format executive round questions."""
        output = []
        for i, q in enumerate(questions, 1):
            output.append(f"""
#### 问题 {i}: {q['question']}

**回答方向**: {q['answer_direction']}
""")
        return '\n'.join(output)

    def _format_macro_topics(self, topics: List[Dict[str, str]]) -> str:
        """Format macro topics."""
        if not topics:
            return "- 暂无特定话题"

        output = []
        for topic in topics:
            output.append(f"- **{topic['topic']}**: {topic['angle']}")
        return '\n'.join(output)

    def _format_killer_cases(self, cases: List[Dict[str, Any]]) -> str:
        """Format killer cases."""
        output = []
        for i, case in enumerate(cases, 1):
            output.append(f"""
### 案例 {i}: {case['case_name']}

**要求**: {case['requirement']}

**结构**:
{self._format_case_structure(case['structure'])}

**准备检查清单**:
{self._format_list(case['prep_checklist'])}
""")
        return '\n'.join(output)

    def _format_case_structure(self, structure: Dict[str, str]) -> str:
        """Format case structure."""
        output = []
        for key, value in structure.items():
            output.append(f"- **{key}**: {value}")
        return '\n'.join(output)

    def _format_risk_mitigation(self, mitigation: Dict[str, Any]) -> str:
        """Format risk mitigation."""
        output = [f"**识别风险**: {', '.join(mitigation['identified_risks']) if mitigation['identified_risks'] else '无明显风险'}"]

        if mitigation['mitigation_strategies']:
            output.append("\n**缓解策略**:")
            for strategy in mitigation['mitigation_strategies']:
                output.append(f"\n**风险**: {strategy['risk']}")
                output.append(f"**策略**: {strategy['approach']}")
                output.append(f"**战术**:\n{self._format_list(strategy['tactics'])}")

        return '\n'.join(output)


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        print("Interview Strategy Generator")
        print("\nUsage:")
        print("  python interview_strategy.py generate --company-path <path> --resume <version> --jd-analysis <file> [--gaps <gap1,gap2>]")
        print("\nExamples:")
        print('  python interview_strategy.py generate --company-path ~/InterviewIntel/companies/MiniMax --resume v1.0 --jd-analysis jd_analysis.json --gaps "跨行转型,开放平台经验不足"')
        sys.exit(1)

    command = sys.argv[1]

    # Parse arguments
    args = {}
    i = 2
    while i < len(sys.argv):
        if sys.argv[i].startswith("--"):
            key = sys.argv[i][2:]
            if i + 1 < len(sys.argv) and not sys.argv[i + 1].startswith("--"):
                args[key] = sys.argv[i + 1]
                i += 2
            else:
                args[key] = True
                i += 1
        else:
            i += 1

    try:
        if command == "generate":
            company_path = args["company-path"]
            resume_version = args.get("resume-version") or args.get("resume")
            company = args.get("company", "")
            role = args.get("role", "Unknown")

            # JD analysis file is optional - if not provided, use minimal analysis
            jd_analysis_file = args.get("jd-analysis")

            if jd_analysis_file and os.path.exists(jd_analysis_file):
                # Load JD analysis
                with open(jd_analysis_file, 'r', encoding='utf-8') as f:
                    jd_analysis = json.load(f)
            else:
                # Use minimal analysis if file not provided
                jd_analysis = {
                    "role": role,
                    "core_competencies": [],
                    "hard_requirements": {}
                }

            # Parse gaps
            gaps = []
            if "gaps" in args:
                gaps = [g.strip() for g in args["gaps"].split(',')]

            generator = InterviewStrategy(company_path)

            print(f"🎯 生成面试策略")
            print(f"简历版本: {resume_version}")
            print(f"职位: {jd_analysis.get('role', 'Unknown')}")
            print(f"识别风险: {len(gaps)} 个")

            strategy = generator.generate_full_strategy(resume_version, jd_analysis, gaps)

            output_file = generator.export_strategy_report(strategy)

            print(f"\n✅ 策略已生成")
            print(f"📄 报告: {output_file}")

        else:
            print(f"Unknown command: {command}")
            sys.exit(1)

    except KeyError as e:
        print(f"❌ Missing required argument: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
