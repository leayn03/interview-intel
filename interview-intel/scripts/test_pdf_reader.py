#!/usr/bin/env python3
"""
PDF简历读取测试脚本

用于验证 pdfplumber 是否能正确读取PDF简历文件
"""

import sys
import os

def test_pdf_reading():
    """测试PDF读取功能"""

    # 尝试导入 pdfplumber
    try:
        import pdfplumber
    except ImportError:
        print("❌ pdfplumber 未安装")
        print("正在安装 pdfplumber...")
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pdfplumber', '-q', '--user'])
        import pdfplumber
        print("✅ pdfplumber 安装成功")

    # 检查默认简历目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.dirname(os.path.dirname(script_dir))
    resumes_dir = os.path.join(base_path, "resumes")

    if not os.path.exists(resumes_dir):
        print(f"❌ 简历目录不存在: {resumes_dir}")
        return False

    # 查找PDF文件
    pdf_files = [f for f in os.listdir(resumes_dir) if f.endswith('.pdf')]

    if not pdf_files:
        print(f"❌ 简历目录中没有PDF文件: {resumes_dir}")
        return False

    print(f"✅ 找到 {len(pdf_files)} 个PDF文件")

    # 测试读取第一个PDF
    test_pdf = os.path.join(resumes_dir, pdf_files[0])
    print(f"\n📄 测试读取: {pdf_files[0]}")

    try:
        with pdfplumber.open(test_pdf) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text() + '\n'

            # 显示前100个字符
            preview = text[:100].replace('\n', ' ')
            print(f"✅ PDF读取成功!")
            print(f"   页数: {len(pdf.pages)}")
            print(f"   总字符数: {len(text)}")
            print(f"   内容预览: {preview}...")
            return True

    except Exception as e:
        print(f"❌ PDF读取失败: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("PDF简历读取测试")
    print("=" * 50)

    success = test_pdf_reading()

    print("\n" + "=" * 50)
    if success:
        print("✅ 测试通过 - PDF读取功能正常")
        print("=" * 50)
        sys.exit(0)
    else:
        print("❌ 测试失败 - 请检查PDF文件或pdfplumber安装")
        print("=" * 50)
        sys.exit(1)
