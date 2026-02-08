#!/bin/bash
# Interview Intel - 快速安装脚本
# 让任何人都能一键安装和配置

set -e  # 遇到错误立即退出

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 打印带颜色的消息
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_header() {
    echo -e "${BLUE}"
    echo "================================================"
    echo "  Interview Intel - 快速安装向导"
    echo "  版本: v6.2"
    echo "================================================"
    echo -e "${NC}"
}

# 检查 Python 版本
check_python() {
    print_info "检查 Python 环境..."

    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
        PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
        PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)

        if [ "$PYTHON_MAJOR" -ge 3 ] && [ "$PYTHON_MINOR" -ge 8 ]; then
            print_success "Python $PYTHON_VERSION 已安装"
            return 0
        else
            print_error "Python 版本过低 ($PYTHON_VERSION)，需要 3.8 或更高版本"
            return 1
        fi
    else
        print_error "未找到 Python 3，请先安装 Python"
        echo "  macOS: brew install python3"
        echo "  Ubuntu: sudo apt install python3"
        return 1
    fi
}

# 安装依赖
install_dependencies() {
    print_info "安装 Python 依赖..."

    # 尝试安装 pdfplumber
    if python3 -c "import pdfplumber" 2>/dev/null; then
        print_success "pdfplumber 已安装"
    else
        print_info "安装 pdfplumber..."
        if python3 -m pip install pdfplumber --user -q; then
            print_success "pdfplumber 安装成功"
        else
            print_warning "pdfplumber 安装失败，尝试使用国内镜像..."
            if python3 -m pip install pdfplumber -i https://pypi.tuna.tsinghua.edu.cn/simple --user -q; then
                print_success "pdfplumber 安装成功（使用清华镜像）"
            else
                print_error "pdfplumber 安装失败，请手动安装：pip3 install pdfplumber"
                return 1
            fi
        fi
    fi
}

# 创建必要的目录
create_directories() {
    print_info "创建项目目录结构..."

    mkdir -p resumes
    mkdir -p companies
    mkdir -p .analytics/exports

    print_success "目录结构创建完成"
}

# 验证安装
verify_installation() {
    print_info "验证安装..."

    # 检查脚本是否存在
    if [ ! -f "interview-intel/scripts/all_in_one_v6.1.py" ]; then
        print_error "核心脚本未找到"
        return 1
    fi

    # 测试脚本
    if python3 interview-intel/scripts/all_in_one_v6.1.py --help &> /dev/null; then
        print_success "脚本运行正常"
    else
        print_error "脚本测试失败"
        return 1
    fi

    print_success "安装验证通过"
}

# 显示下一步提示
show_next_steps() {
    echo ""
    echo -e "${GREEN}🎉 安装完成！${NC}"
    echo ""
    echo "下一步："
    echo ""
    echo "1️⃣  添加你的简历到 resumes/ 目录"
    echo "   ${BLUE}cp ~/你的简历.pdf resumes/你的名字-职位.pdf${NC}"
    echo ""
    echo "2️⃣  准备第一份面试分析"
    echo "   ${BLUE}python3 interview-intel/scripts/all_in_one_v6.1.py \\${NC}"
    echo "   ${BLUE}  --base-path . \\${NC}"
    echo "   ${BLUE}  --company \"公司名\" \\${NC}"
    echo "   ${BLUE}  --role \"职位名\" \\${NC}"
    echo "   ${BLUE}  --resume-version \"你的简历.pdf\" \\${NC}"
    echo "   ${BLUE}  --years 工作年限${NC}"
    echo ""
    echo "3️⃣  查看详细文档"
    echo "   ${BLUE}open USER_SETUP_GUIDE.md${NC}"
    echo ""
    echo "💡 提示：使用 Claude Code 可以一键完成所有操作！"
    echo "   只需说：'我想应聘 XXX 公司的 XXX 职位'"
    echo ""
}

# 交互式配置
interactive_setup() {
    echo ""
    read -p "是否要配置你的第一份简历？(y/n) " -n 1 -r
    echo ""

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo ""
        read -p "请输入你的姓名: " USER_NAME
        read -p "请输入你的主要职位类型（如：产品经理）: " USER_ROLE
        read -p "请输入你的工作年限: " USER_YEARS

        # 创建配置文件
        cat > ~/.interview_intel_config << EOF
# Interview Intel 个人配置
# 自动生成于 $(date)

RESUME_VERSION="${USER_NAME}-${USER_ROLE}V1.0.pdf"
USER_NAME="${USER_NAME}"
USER_ROLE="${USER_ROLE}"
YEARS=${USER_YEARS}
PROJECT_PATH="$(pwd)"

# 使用方法:
# source ~/.interview_intel_config
# python3 \$PROJECT_PATH/interview-intel/scripts/all_in_one_v6.1.py \\
#   --base-path \$PROJECT_PATH \\
#   --resume-version \$RESUME_VERSION \\
#   --years \$YEARS \\
#   ...
EOF

        print_success "配置文件已创建: ~/.interview_intel_config"
        echo ""
        print_info "请将你的简历复制到: resumes/${USER_NAME}-${USER_ROLE}V1.0.pdf"
        echo ""
    fi
}

# 主函数
main() {
    print_header

    # 检查是否在项目根目录
    if [ ! -d "interview-intel" ]; then
        print_error "请在 InterviewIntel 项目根目录运行此脚本"
        exit 1
    fi

    # 执行安装步骤
    if ! check_python; then
        exit 1
    fi

    if ! install_dependencies; then
        exit 1
    fi

    create_directories

    if ! verify_installation; then
        exit 1
    fi

    show_next_steps

    # 询问是否要交互式配置
    interactive_setup

    echo ""
    print_success "全部完成！祝你面试顺利！🚀"
    echo ""
}

# 运行主函数
main
