#!/usr/bin/env python3
"""
Icebreaker Message Generator

Generates compelling opening messages for job applications on platforms like Boss直聘.
Two strategies: Professional Match and Business Insight.
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any


class IcebreakerGenerator:
    """Generates icebreaker messages for job applications."""

    def __init__(self, company_path: str):
        """
        Initialize the generator.

        Args:
            company_path: Path to company folder
        """
        self.company_path = Path(company_path)

    def generate_messages(
        self,
        company_name: str,
        role: str,
        jd_keywords: List[str],
        top_achievement: str,
        years_experience: Optional[int] = None,
        industry_insights: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate two styles of icebreaker messages.

        Args:
            company_name: Company name
            role: Target role
            jd_keywords: Key requirements from JD
            top_achievement: Candidate's top relevant achievement
            years_experience: Years of relevant experience
            industry_insights: Industry/business insights

        Returns:
            Dictionary with both message styles
        """
        messages = {
            "generated_at": datetime.now().isoformat(),
            "company": company_name,
            "role": role,
            "strategy_a_professional": self._generate_professional_match(
                company_name, role, jd_keywords, top_achievement, years_experience
            ),
            "strategy_b_insight": self._generate_business_insight(
                company_name, role, industry_insights, top_achievement
            ),
            "usage_guide": self._generate_usage_guide()
        }

        return messages

    def _generate_professional_match(
        self,
        company_name: str,
        role: str,
        jd_keywords: List[str],
        top_achievement: str,
        years_experience: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Generate Strategy A: Professional precise match.

        Style: Professional, concise, result-oriented
        For: HR, formal process
        """
        # Pick top 2 keywords
        keywords_str = "、".join(jd_keywords[:2]) if jd_keywords else role

        # Build hook
        hook = f"看到贵司在招{keywords_str}方向的{role}，"

        # Build proof
        if years_experience:
            proof = f"我有{years_experience}年相关经验，{top_achievement}。"
        else:
            proof = f"{top_achievement}。"

        # Build CTA
        cta = "简历已备好，期待您的查看。"

        message = hook + proof + cta

        return {
            "message": message,
            "word_count": len(message),
            "structure": {
                "hook": hook,
                "proof": proof,
                "cta": cta
            },
            "适用场景": "HR筛选、正规流程",
            "优势": "专业、数据导向、直截了当",
            "注意事项": [
                "确保提到的关键词在JD中确实存在",
                "成就必须可验证，不要夸大",
                "保持简洁，100字以内"
            ]
        }

    def _generate_business_insight(
        self,
        company_name: str,
        role: str,
        industry_insights: Optional[str],
        top_achievement: str
    ) -> Dict[str, Any]:
        """
        Generate Strategy B: Business pain point resonance.

        Style: Warm, insightful, peer-to-peer
        For: Business leads, startup teams
        """
        # Build hook with insight
        if industry_insights:
            hook = f"非常认可贵司在{industry_insights}的布局，"
        else:
            hook = f"一直关注贵司{role}团队的发展，"

        # Build proof with similar scenario
        proof = f"我之前在类似场景下{top_achievement}，"

        # Build curiosity-driven CTA
        cta = "希望能聊聊具体的业务挑战。"

        message = hook + proof + cta

        return {
            "message": message,
            "word_count": len(message),
            "structure": {
                "hook": hook,
                "proof": proof,
                "cta": cta
            },
            "适用场景": "业务负责人、创业团队、技术驱动公司",
            "优势": "展示认知、引发共鸣、像同行交流",
            "注意事项": [
                "需要对公司业务有深入了解",
                "行业洞察要准确，不要讲外行话",
                "展示解决问题的能力，而非只是关注"
            ]
        }

    def _generate_usage_guide(self) -> Dict[str, Any]:
        """Generate usage guide for the messages."""
        return {
            "选择策略": {
                "使用策略A": [
                    "应聘大公司、正规流程",
                    "对方是HR或招聘专员",
                    "强调匹配度和专业性"
                ],
                "使用策略B": [
                    "应聘创业公司、小团队",
                    "对方是业务负责人或技术 Leader",
                    "展示行业理解和业务思维"
                ]
            },
            "发送时机": [
                "投递简历后24小时内发送（趁热打铁）",
                "工作日上午10-11点或下午3-4点（对方精力充沛）",
                "避开周一上午和周五下午（太忙或快周末了）"
            ],
            "禁忌词汇": [
                "❌ 希望能有一个机会",
                "❌ 我会努力学习",
                "❌ 请多多指教",
                "❌ 给我一个机会证明自己",
                "❌ 我很感兴趣，想试试"
            ],
            "加分技巧": [
                "✅ 提及具体数据和成果",
                "✅ 使用对方公司的产品或服务",
                "✅ 展示对公司业务的理解",
                "✅ 表达合作意愿而非求职姿态",
                "✅ 简洁有力，不超过100字"
            ]
        }

    def export_messages(
        self,
        messages: Dict[str, Any],
        output_file: Optional[str] = None
    ) -> str:
        """
        Export messages to file.

        Args:
            messages: Generated messages
            output_file: Output file path

        Returns:
            Path to generated file
        """
        if not output_file:
            role = messages['role'].replace(' ', '_')
            output_file = self.company_path / f"icebreaker_{messages['company']}_{role}.md"

        content = self._format_messages(messages)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

        return str(output_file)

    def _format_messages(self, messages: Dict[str, Any]) -> str:
        """Format messages as markdown."""
        report = f"""# 破冰开场白 - {messages['company']} {messages['role']}

**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 策略 A: 实力精准匹配

### 适用场景
{self._format_list(messages['strategy_a_professional']['适用场景'])}

### 开场白文案

```
{messages['strategy_a_professional']['message']}
```

**字数**: {messages['strategy_a_professional']['word_count']} 字

### 结构拆解
- **挂钩**: {messages['strategy_a_professional']['structure']['hook']}
- **证明**: {messages['strategy_a_professional']['structure']['proof']}
- **行动**: {messages['strategy_a_professional']['structure']['cta']}

### 优势
{messages['strategy_a_professional']['优势']}

### 注意事项
{self._format_list(messages['strategy_a_professional']['注意事项'])}

---

## 策略 B: 业务痛点共鸣

### 适用场景
{messages['strategy_b_insight']['适用场景']}

### 开场白文案

```
{messages['strategy_b_insight']['message']}
```

**字数**: {messages['strategy_b_insight']['word_count']} 字

### 结构拆解
- **挂钩**: {messages['strategy_b_insight']['structure']['hook']}
- **证明**: {messages['strategy_b_insight']['structure']['proof']}
- **行动**: {messages['strategy_b_insight']['structure']['cta']}

### 优势
{messages['strategy_b_insight']['优势']}

### 注意事项
{self._format_list(messages['strategy_b_insight']['注意事项'])}

---

## 使用指南

### 如何选择策略

**使用策略 A 当**:
{self._format_list(messages['usage_guide']['选择策略']['使用策略A'])}

**使用策略 B 当**:
{self._format_list(messages['usage_guide']['选择策略']['使用策略B'])}

### 最佳发送时机
{self._format_list(messages['usage_guide']['发送时机'])}

### 禁忌词汇
{self._format_list(messages['usage_guide']['禁忌词汇'])}

### 加分技巧
{self._format_list(messages['usage_guide']['加分技巧'])}

---

**生成工具**: Interview Intel - Icebreaker Generator
"""
        return report

    def _format_list(self, items) -> str:
        """Format items as markdown list."""
        if isinstance(items, str):
            return f"- {items}"
        elif isinstance(items, list):
            return '\n'.join([f"- {item}" for item in items])
        else:
            return str(items)


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        print("Icebreaker Message Generator")
        print("\nUsage:")
        print("  python icebreaker_generator.py generate --company-path <path> --company <name> --role <role> --keywords <kw1,kw2> --achievement <text> [--years <n>] [--insight <text>]")
        print("\nExamples:")
        print('  python icebreaker_generator.py generate --company-path ~/InterviewIntel/companies/MiniMax --company MiniMax --role "产品经理" --keywords "AI,开放平台" --achievement "主导AI产品从0到1，用户增长300%" --years 5 --insight "大模型to B商业化"')
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
            company_name = args["company"]
            role = args["role"]
            keywords = [k.strip() for k in args["keywords"].split(',')]
            achievement = args["achievement"]
            years = int(args.get("years", 0)) if "years" in args else None
            insight = args.get("insight")

            generator = IcebreakerGenerator(company_path)

            print(f"✍️ 生成破冰文案")
            print(f"公司: {company_name}")
            print(f"职位: {role}")

            messages = generator.generate_messages(
                company_name, role, keywords, achievement, years, insight
            )

            output_file = generator.export_messages(messages)

            print(f"\n✅ 文案已生成")
            print(f"📄 文件: {output_file}")
            print(f"\n📝 策略 A (专业匹配):")
            print(f"   {messages['strategy_a_professional']['message']}")
            print(f"\n📝 策略 B (业务洞察):")
            print(f"   {messages['strategy_b_insight']['message']}")

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
