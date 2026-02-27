#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
专业化流水线团队 - 测试脚本

快速测试 pipeline_team.py 的功能
"""

import os
import sys
from pathlib import Path

# 添加路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.pipeline_team import PipelineTeam


def test_pipeline_team():
    """测试专业化流水线团队"""

    print("🧪 专业化流水线团队 - 功能测试")
    print("=" * 60)
    print()

    # 测试参数
    test_company = "测试公司"
    test_role = "产品经理"
    test_candidate = "测试候选人"
    test_jd = """职位名称：产品经理

职位描述：
1. 负责产品规划和设计
2. 协调开发和设计团队
3. 分析用户需求和市场趋势

任职要求：
1. 3年以上产品经验
2. 良好的沟通能力
3. 数据驱动思维
"""

    # 查找测试简历
    resume_path = None
    resumes_dir = Path(__file__).parent.parent / "resumes"

    if resumes_dir.exists():
        # 查找第一个PDF文件
        pdf_files = list(resumes_dir.glob("*.pdf"))
        if pdf_files:
            resume_path = str(pdf_files[0])
            print(f"📄 使用简历: {resume_path}")
        else:
            print("⚠️  警告: resumes/ 目录中没有找到PDF文件")
            print("   将创建模拟简历进行测试...")
    else:
        print("⚠️  警告: resumes/ 目录不存在")
        print("   将创建模拟简历进行测试...")

    # 如果没有简历，创建模拟文件
    if not resume_path:
        resume_path = "/tmp/test_resume.pdf"
        # 创建一个简单的文本文件作为测试
        with open(resume_path, 'w') as f:
            f.write("测试简历内容\n")
        print(f"📄 创建测试简历: {resume_path}")

    print()
    print("📋 测试参数:")
    print(f"   公司: {test_company}")
    print(f"   职位: {test_role}")
    print(f"   候选人: {test_candidate}")
    print()

    input("按 Enter 开始测试...")

    # 启动团队
    try:
        team = PipelineTeam(base_path="..")
        output_dir = team.launch(
            company=test_company,
            role=test_role,
            candidate=test_candidate,
            jd_content=test_jd,
            resume_path=resume_path
        )

        print()
        print("=" * 60)
        print("✅ 测试完成!")
        print()
        print(f"📁 输出目录: {output_dir}")
        print()
        print("验证结果:")

        # 验证生成的文件
        expected_files = [
            "01_company_intel_brief.md",
            "02_resume_jd_matching.md",
            "03_interview_prep_report.md",
            "04_icebreaker_messages.md",
            "05_final_analysis_report.md"
        ]

        for filename in expected_files:
            file_path = output_dir / filename
            if file_path.exists():
                size = file_path.stat().st_size / 1024
                print(f"   ✅ {filename} ({size:.1f}K)")
            else:
                print(f"   ❌ {filename} 未生成")

        print()
        print("💡 提示: 测试成功！可以使用真实参数调用:")
        print()
        print("python scripts/pipeline_team.py \\")
        print("  --company \"阿里云\" \\")
        print("  --role \"AI产品经理\" \\")
        print("  --candidate \"王蕾\" \\")
        print("  --jd \"jd.txt\" \\")
        print("  --resume \"resumes/王蕾-AI产品经理V1.0.pdf\"")

    except KeyboardInterrupt:
        print("\n\n⚠️  测试中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def main():
    """主入口"""
    import argparse

    parser = argparse.ArgumentParser(description="专业化流水线团队测试")
    parser.add_argument("--quick", action="store_true", help="快速测试（使用模拟数据）")
    parser.add_argument("--real", action="store_true", help="真实测试（使用真实简历）")

    args = parser.parse_args()

    if args.real:
        print("🧪 真实测试模式")
        print("请确保提供了真实的JD和简历路径")
        print()

        # 真实测试需要用户提供参数
        company = input("公司名称: ")
        role = input("职位名称: ")
        candidate = input("候选人姓名: ")
        jd_path = input("JD文件路径: ")
        resume_path = input("简历文件路径: ")

        # 读取JD
        with open(jd_path, 'r', encoding='utf-8') as f:
            jd_content = f.read()

        team = PipelineTeam()
        team.launch(company, role, candidate, jd_content, resume_path)
    else:
        # 默认快速测试
        test_pipeline_team()


if __name__ == "__main__":
    main()
