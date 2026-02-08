# 简历目录

请将你的简历文件放在这个目录下。

## 📋 命名建议

```
你的名字-职位类型-版本.pdf

示例：
- 张三-产品经理V1.0.pdf
- 李四-后端工程师V2.0.pdf
- 王五-数据分析师-通用版.pdf
```

## 🚀 使用方法

### 1. 添加简历

```bash
# 复制你的简历到这个目录
cp ~/Downloads/我的简历.pdf resumes/张三-产品经理V1.0.pdf
```

### 2. 开始使用

```bash
# 生成面试准备包
python3 interview-intel/scripts/all_in_one_v6.1.py \
  --base-path . \
  --company "目标公司" \
  --role "目标职位" \
  --resume-version "张三-产品经理V1.0.pdf" \
  --years 3
```

## 📚 更多信息

查看完整文档：[USER_SETUP_GUIDE.md](../USER_SETUP_GUIDE.md)
