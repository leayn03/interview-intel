#!/usr/bin/env python3
"""
All-in-One Interview Intel Workflow

One-command execution to generate complete interview preparation package.
Input: JD + Resume Version
Output: Company background, JD analysis, resume matching, interview strategy, icebreaker messages
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

class AllInOneWorkflow:
    """Orchestrates the complete interview preparation workflow."""

    def __init__(self, base_path: str):
        """
        Initialize workflow.

        Args:
            base_path: Base path where companies/ folder lives
        """
        self.base_path = Path(base_path)
        self.scripts_dir = Path(__file__).parent

    def execute(
        self,
        company_name: str,
        role_name: str,
        jd_text: str,
        resume_version: str,
        resume_content: Optional[str] = None,
        top_achievement: Optional[str] = None,
        years_experience: Optional[int] = None,
        industry_insight: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Execute complete workflow.

        Args:
            company_name: Target company name
            role_name: Target role/position
            jd_text: Job description text
            resume_version: Resume version identifier (e.g., "v1.0")
            resume_content: Resume text content for matching analysis
            top_achievement: Top achievement for icebreaker
            years_experience: Years of relevant experience
            industry_insight: Industry insight for icebreaker strategy B

        Returns:
            Dictionary with paths to all generated files
        """
        print(f"\n{'='*70}")
        print(f"🚀 Interview Intel 一键执行工作流")
        print(f"{'='*70}\n")
        print(f"📋 公司: {company_name}")
        print(f"📋 职位: {role_name}")
        print(f"📋 简历版本: {resume_version}")
        print(f"\n{'='*70}\n")

        results = {
            "company": company_name,
            "role": role_name,
            "resume_version": resume_version,
            "generated_at": datetime.now().isoformat(),
            "files": {}
        }

        try:
            # Step 1: Setup company folder
            print("📁 Step 1/6: 创建公司文件夹结构...")
            folder_info = self._setup_company_folder(company_name, role_name)
            results["company_path"] = folder_info["company_folder"]
            print(f"✅ 文件夹创建完成: {folder_info['company_folder']}")

            # Step 2: Save original JD
            print("\n📄 Step 2/6: 保存原始 JD...")
            jd_file = self._save_jd(folder_info, jd_text, role_name)
            results["files"]["jd_original"] = str(jd_file)
            print(f"✅ JD 已保存: {jd_file}")

            # Step 3: Extract JD keywords
            print("\n🔍 Step 3/6: 提取 JD 关键词...")
            keywords_file = self._extract_keywords(jd_file, folder_info, role_name)
            results["files"]["jd_keywords"] = str(keywords_file)
            print(f"✅ 关键词已提取: {keywords_file}")

            # Step 4: Generate JD deep analysis + Resume matching
            print("\n🧠 Step 4/6: 生成 JD 深度分析和简历匹配报告...")
            analysis_files = self._generate_analysis(
                company_name, role_name, jd_file, resume_version,
                resume_content, folder_info
            )
            results["files"].update(analysis_files)
            print(f"✅ JD 分析完成: {analysis_files.get('jd_analysis')}")
            print(f"✅ 简历匹配完成: {analysis_files.get('resume_mapping')}")

            # Step 5: Generate interview strategy
            print("\n⚔️ Step 5/6: 生成面试攻防策略...")
            strategy_file = self._generate_strategy(
                company_name, role_name, resume_version, folder_info
            )
            results["files"]["interview_strategy"] = str(strategy_file)
            print(f"✅ 面试策略完成: {strategy_file}")

            # Step 6: Generate icebreaker messages
            print("\n💬 Step 6/6: 生成破冰文案...")
            icebreaker_file = self._generate_icebreaker(
                company_name, role_name, keywords_file,
                top_achievement, years_experience, industry_insight, folder_info
            )
            results["files"]["icebreaker"] = str(icebreaker_file)
            print(f"✅ 破冰文案完成: {icebreaker_file}")

            # Final summary
            print(f"\n{'='*70}")
            print(f"✅ 工作流执行完成！")
            print(f"{'='*70}\n")
            print(f"📂 所有文件已保存到: {results['company_path']}")
            print(f"\n生成的文件:")
            for key, path in results["files"].items():
                print(f"  - {key}: {Path(path).name}")

            # Save workflow metadata
            metadata_file = Path(results['company_path']) / f"workflow_metadata_{role_name}.json"
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)

            return results

        except Exception as e:
            print(f"\n❌ 错误: {e}")
            import traceback
            traceback.print_exc()
            raise

    def _setup_company_folder(self, company_name: str, role_name: str) -> Dict[str, Any]:
        """Step 1: Setup company folder structure."""
        script = self.scripts_dir / "setup_company_folder.py"
        cmd = [
            "python3", str(script),
            str(self.base_path),
            company_name,
            role_name
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"Failed to setup folder: {result.stderr}")

        # Parse JSON output - extract JSON from the output
        # The script outputs both human-readable text and JSON (after "--- JSON OUTPUT ---")
        output = result.stdout
        if "--- JSON OUTPUT ---" in output:
            json_start = output.index("--- JSON OUTPUT ---") + len("--- JSON OUTPUT ---")
            json_str = output[json_start:].strip()
            return json.loads(json_str)
        else:
            # Fallback: try to parse the entire output as JSON
            return json.loads(output)

    def _save_jd(self, folder_info: Dict[str, Any], jd_text: str, role_name: str) -> Path:
        """Step 2: Save original JD text."""
        jd_file = Path(folder_info['raw_data_folder']) / f"jd_original_{role_name}.txt"
        with open(jd_file, 'w', encoding='utf-8') as f:
            f.write(jd_text)
        return jd_file

    def _extract_keywords(self, jd_file: Path, folder_info: Dict[str, Any], role_name: str) -> Path:
        """Step 3: Extract JD keywords."""
        script = self.scripts_dir / "extract_jd_keywords.py"
        keywords_file = Path(folder_info['raw_data_folder']) / f"jd_keywords_{role_name}.txt"

        cmd = [
            "python3", str(script),
            str(jd_file)
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"Failed to extract keywords: {result.stderr}")

        # Save keywords output
        with open(keywords_file, 'w', encoding='utf-8') as f:
            f.write(result.stdout)

        return keywords_file

    def _generate_analysis(
        self,
        company_name: str,
        role_name: str,
        jd_file: Path,
        resume_version: str,
        resume_content: Optional[str],
        folder_info: Dict[str, Any]
    ) -> Dict[str, str]:
        """Step 4: Generate JD analysis and resume matching using resume_optimizer.py."""
        script = self.scripts_dir / "resume_optimizer.py"
        company_path = folder_info['company_folder']

        # Build command
        cmd = [
            "python3", str(script),
            "analyze",
            "--company-path", company_path,
            "--company", company_name,
            "--role", role_name,
            "--jd-file", str(jd_file),
            "--resume-version", resume_version
        ]

        # Add resume content if provided
        if resume_content:
            # Save resume content to temp file
            temp_resume = Path(folder_info['resumes_folder']) / f"temp_resume_{resume_version}.txt"
            with open(temp_resume, 'w', encoding='utf-8') as f:
                f.write(resume_content)
            cmd.extend(["--resume-file", str(temp_resume)])

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"Failed to generate analysis: {result.stderr}")

        # Return paths to generated files
        return {
            "jd_analysis": str(Path(company_path) / f"jd_analysis_{role_name}.md"),
            "resume_mapping": str(Path(company_path) / f"resume_mapping_{role_name}.md")
        }

    def _generate_strategy(
        self,
        company_name: str,
        role_name: str,
        resume_version: str,
        folder_info: Dict[str, Any]
    ) -> Path:
        """Step 5: Generate interview strategy using interview_strategy.py."""
        script = self.scripts_dir / "interview_strategy.py"
        company_path = folder_info['company_folder']

        cmd = [
            "python3", str(script),
            "generate",
            "--company-path", company_path,
            "--company", company_name,
            "--role", role_name,
            "--resume-version", resume_version
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"Failed to generate strategy: {result.stderr}")

        return Path(company_path) / f"interview_strategy_{role_name}.md"

    def _generate_icebreaker(
        self,
        company_name: str,
        role_name: str,
        keywords_file: Path,
        top_achievement: Optional[str],
        years_experience: Optional[int],
        industry_insight: Optional[str],
        folder_info: Dict[str, Any]
    ) -> Path:
        """Step 6: Generate icebreaker messages using icebreaker_generator.py."""
        script = self.scripts_dir / "icebreaker_generator.py"
        company_path = folder_info['company_folder']

        # Extract top keywords from keywords file
        keywords = self._extract_top_keywords(keywords_file)

        # Use default achievement if not provided
        if not top_achievement:
            top_achievement = "多年产品和技术经验，独立完成多个项目从 0 到 1"

        cmd = [
            "python3", str(script),
            "generate",
            "--company-path", company_path,
            "--company", company_name,
            "--role", role_name,
            "--keywords", ",".join(keywords[:3]),  # Top 3 keywords
            "--achievement", top_achievement
        ]

        if years_experience:
            cmd.extend(["--years", str(years_experience)])

        if industry_insight:
            cmd.extend(["--insight", industry_insight])

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"Failed to generate icebreaker: {result.stderr}")

        return Path(company_path) / f"icebreaker_{company_name}_{role_name}.md"

    def _extract_top_keywords(self, keywords_file: Path) -> list:
        """Extract top keywords from keywords extraction output."""
        keywords = []

        try:
            with open(keywords_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Simple extraction: look for lines that start with "- " in technical skills section
            in_tech_section = False
            for line in content.split('\n'):
                if 'Technical Skills' in line or '技术技能' in line:
                    in_tech_section = True
                    continue
                if in_tech_section and line.strip().startswith('-'):
                    # Extract keyword (remove "- " and any trailing notes)
                    keyword = line.strip()[2:].split('(')[0].split('：')[0].strip()
                    if keyword:
                        keywords.append(keyword)
                    if len(keywords) >= 5:
                        break
                elif in_tech_section and not line.strip():
                    break
        except Exception:
            # Fallback keywords
            keywords = ["产品设计", "需求分析", "项目管理"]

        return keywords if keywords else ["产品设计", "需求分析", "项目管理"]


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        print("""
Interview Intel - All-in-One Workflow

一键生成完整面试准备包。

Usage:
  python all_in_one.py execute --base-path <path> --company <name> --role <title> --jd-file <file> --resume-version <version> [options]

Required Arguments:
  --base-path <path>          Base path (contains companies/ folder)
  --company <name>            Company name
  --role <title>              Role/position title
  --jd-file <file>            Path to JD text file
  --resume-version <version>  Resume version (e.g., v1.0, v2.0)

Optional Arguments:
  --resume-file <file>        Path to resume content file (for matching analysis)
  --achievement <text>        Top achievement for icebreaker
  --years <number>            Years of relevant experience
  --insight <text>            Industry insight for icebreaker strategy B

Examples:
  # Basic usage
  python all_in_one.py execute \\
    --base-path ~/InterviewIntel \\
    --company "京东物流" \\
    --role "运输产品经理" \\
    --jd-file jd.txt \\
    --resume-version v1.0

  # With full options
  python all_in_one.py execute \\
    --base-path ~/InterviewIntel \\
    --company "京东物流" \\
    --role "运输产品经理" \\
    --jd-file jd.txt \\
    --resume-version v1.0 \\
    --resume-file resume_v1.0.txt \\
    --achievement "主导 AI 产品从 0 到 1，用户增长 300%" \\
    --years 6 \\
    --insight "物流供应链智能化"

Output:
  所有文件将保存到: <base-path>/companies/<company>/
  包含: JD 分析、简历匹配、面试策略、破冰文案等
""")
        sys.exit(1)

    command = sys.argv[1]

    if command != "execute":
        print(f"Unknown command: {command}")
        sys.exit(1)

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

    # Validate required arguments
    required = ["base-path", "company", "role", "jd-file", "resume-version"]
    missing = [arg for arg in required if arg not in args]
    if missing:
        print(f"❌ Missing required arguments: {', '.join(missing)}")
        sys.exit(1)

    try:
        # Read JD file
        with open(args["jd-file"], 'r', encoding='utf-8') as f:
            jd_text = f.read()

        # Read resume file if provided
        resume_content = None
        if "resume-file" in args:
            with open(args["resume-file"], 'r', encoding='utf-8') as f:
                resume_content = f.read()

        # Initialize workflow
        workflow = AllInOneWorkflow(args["base-path"])

        # Execute workflow
        results = workflow.execute(
            company_name=args["company"],
            role_name=args["role"],
            jd_text=jd_text,
            resume_version=args["resume-version"],
            resume_content=resume_content,
            top_achievement=args.get("achievement"),
            years_experience=int(args["years"]) if "years" in args else None,
            industry_insight=args.get("insight")
        )

        # Print success summary
        print(f"\n🎉 完成！所有文件已生成。")
        print(f"\n下一步:")
        print(f"  1. 查看 JD 分析: {Path(results['files']['jd_analysis']).name}")
        print(f"  2. 查看简历匹配: {Path(results['files']['resume_mapping']).name}")
        print(f"  3. 查看面试策略: {Path(results['files']['interview_strategy']).name}")
        print(f"  4. 查看破冰文案: {Path(results['files']['icebreaker']).name}")

    except KeyError as e:
        print(f"❌ Missing required argument: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
