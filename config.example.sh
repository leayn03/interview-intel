#!/bin/bash
# Interview Intel - 配置文件示例
# 复制此文件为 ~/.interview_intel_config 并修改为你的信息

# ============================================
# 个人信息配置
# ============================================

# 你的姓名
USER_NAME="张三"

# 你的主要职位类型
USER_ROLE="产品经理"

# 工作年限
YEARS=3

# 所属行业
INDUSTRY="互联网"

# 核心成就（用于破冰文案）
ACHIEVEMENT="主导产品从0到1，MAU达到10万+"

# 默认关键词（逗号分隔）
DEFAULT_KEYWORDS="产品设计,数据分析,项目管理"

# ============================================
# 简历配置
# ============================================

# 默认简历版本（文件名）
RESUME_VERSION="${USER_NAME}-${USER_ROLE}V1.0.pdf"

# 项目路径（自动检测，无需修改）
PROJECT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 简历完整路径
RESUME_PATH="${PROJECT_PATH}/resumes/${RESUME_VERSION}"

# ============================================
# 快捷命令别名
# ============================================

# 快速生成面试准备包
alias interview-prep='python3 ${PROJECT_PATH}/interview-intel/scripts/all_in_one_v6.1.py \
  --base-path ${PROJECT_PATH} \
  --resume-version ${RESUME_VERSION} \
  --years ${YEARS} \
  --industry "${INDUSTRY}" \
  --achievement "${ACHIEVEMENT}"'

# 查看已生成的公司列表
alias interview-list='ls -1 ${PROJECT_PATH}/companies/'

# 打开最近的分析报告
alias interview-open='open ${PROJECT_PATH}/companies/*/05_final_analysis_report.md | head -1'

# ============================================
# 使用方法
# ============================================

# 1. 复制此文件到你的家目录
#    cp config.example.sh ~/.interview_intel_config

# 2. 修改上面的配置为你的信息

# 3. 在 ~/.bashrc 或 ~/.zshrc 中添加
#    source ~/.interview_intel_config

# 4. 重新加载配置
#    source ~/.bashrc  # 或 source ~/.zshrc

# 5. 使用快捷命令
#    interview-prep --company "MiniMax" --role "产品经理"
#    interview-list
#    interview-open

# ============================================
# 示例：完整的面试准备命令
# ============================================

# 方式 1：使用快捷命令（推荐）
# interview-prep --company "MiniMax" --role "AI产品经理" --keywords "AI,大模型,ToB"

# 方式 2：使用完整命令
# python3 ${PROJECT_PATH}/interview-intel/scripts/all_in_one_v6.1.py \
#   --base-path ${PROJECT_PATH} \
#   --company "MiniMax" \
#   --role "AI产品经理" \
#   --resume-version "${RESUME_VERSION}" \
#   --years ${YEARS} \
#   --industry "${INDUSTRY}" \
#   --keywords "AI,大模型,ToB" \
#   --achievement "${ACHIEVEMENT}"

# ============================================
# 高级配置（可选）
# ============================================

# 导出 PDF 的默认工具
export PDF_VIEWER="open"  # macOS: open, Linux: xdg-open, Windows: start

# Markdown 编辑器
export MD_EDITOR="code"   # VSCode: code, Typora: typora

# 默认浏览器
export BROWSER="open"     # macOS: open, Linux: xdg-open

# ============================================
# 辅助函数
# ============================================

# 快速查看公司分析报告
view_company() {
    local company=$1
    if [ -z "$company" ]; then
        echo "用法: view_company 公司名"
        return 1
    fi

    local report="${PROJECT_PATH}/companies/${company}/05_final_analysis_report.md"
    if [ -f "$report" ]; then
        ${MD_EDITOR} "$report"
    else
        echo "未找到 ${company} 的分析报告"
        echo "已有公司："
        ls -1 "${PROJECT_PATH}/companies/"
    fi
}

# 导出公司分析为 PDF
export_company_pdf() {
    local company=$1
    if [ -z "$company" ]; then
        echo "用法: export_company_pdf 公司名"
        return 1
    fi

    echo "将 ${company} 的分析导出为 PDF..."
    # 这里需要安装 pandoc 或使用其他工具
    # pandoc "${PROJECT_PATH}/companies/${company}"/*.md -o "${company}_面试准备.pdf"
}

# 清理测试数据
clean_test_data() {
    echo "⚠️  这将删除所有生成的公司分析报告"
    read -p "确定要继续吗? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf "${PROJECT_PATH}/companies/"*
        echo "✅ 清理完成"
    fi
}

# 打印当前配置
show_config() {
    echo "================================"
    echo "Interview Intel 当前配置"
    echo "================================"
    echo "姓名:       ${USER_NAME}"
    echo "职位:       ${USER_ROLE}"
    echo "年限:       ${YEARS}年"
    echo "行业:       ${INDUSTRY}"
    echo "简历版本:   ${RESUME_VERSION}"
    echo "项目路径:   ${PROJECT_PATH}"
    echo "================================"
}

# ============================================
# 初始化提示
# ============================================

echo "✅ Interview Intel 配置已加载"
echo "💡 使用 'show_config' 查看当前配置"
echo "💡 使用 'interview-prep --help' 查看帮助"
