#!/usr/bin/env python3
"""
Interview Intel - All-in-One v6.0
一键生成 5 个标准面试准备文件
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

# 添加脚本目录到路径
SCRIPT_DIR = Path(__file__).parent
sys.path.append(str(SCRIPT_DIR))


def create_company_folder(base_path, company):
    """创建公司文件夹结构"""
    company_path = Path(base_path) / "companies" / company
    company_path.mkdir(parents=True, exist_ok=True)

    # 创建子文件夹
    (company_path / "raw_data").mkdir(exist_ok=True)
    (company_path / "resumes").mkdir(exist_ok=True)
    (company_path / "interviews").mkdir(exist_ok=True)

    return company_path


def generate_file_01_company_intel(company_path, company, role, industry=""):
    """生成文件 1: 公司背景业务信息"""
    print(f"\n📋 生成文件 1/5: 公司背景业务信息...")

    # TODO: 这里需要实际的公司调研逻辑
    # 当前生成基础模板,需要手动补充或通过 AI 生成实际内容

    template = f"""# {company} - 公司情报简报

**更新日期**: {datetime.now().strftime('%Y-%m-%d')}
**目标职位**: {role}
**行业**: {industry if industry else '待补充'}

---

## 📊 一分钟速览(精简版)

**公司规模**: [待补充]
**业务模式**: [待补充]
**核心优势**: [待补充]
**目标岗位**: {role}
**匹配度**: ⭐⭐⭐⭐ (75/100)

### 关键信息
- **成立时间**: [待补充]
- **融资阶段**: [待补充]
- **团队规模**: [待补充]
- **核心产品**: [待补充]

### 一句话总结
[用一句话描述这家公司的核心业务和竞争力]

---

## 详细版

### 一、公司核心信息

#### 1.1 公司定位
[公司的市场定位、业务方向、核心竞争力]

#### 1.2 产品线
**核心产品**:
- [产品 1]: [描述]
- [产品 2]: [描述]

**目标用户**:
- [用户群体 1]
- [用户群体 2]

#### 1.3 市场地位
**行业排名**: [待补充]
**主要竞争对手**: [待补充]
**差异化优势**: [待补充]

---

### 二、技术栈与产品

#### 2.1 核心技术
[技术栈、技术团队、技术挑战]

#### 2.2 产品系统
[核心产品系统架构]

---

### 三、企业文化与价值观

#### 3.1 价值观
[公司价值观]

#### 3.2 工作文化
[工作节奏、协作方式、加班文化]

---

### 四、招聘岗位解读

#### 4.1 岗位定位
**级别**: [推测]
**职责范围**: [核心职责]

#### 4.2 为什么招这个岗位
[推测招聘原因]

---

### 五、竞争对手分析
[主要竞品的优劣势分析]

---

### 六、行业趋势
[行业技术趋势、业务趋势]

---

### 七、面试准备关键情报

#### 必须了解的信息
- [ ] 公司官网浏览
- [ ] 产品体验
- [ ] 年报阅读(如有)

#### 高频问题准备
**Q: 为什么想加入我们公司?**
[回答方向]

---

**建议阅读时间**: 15-20 分钟
**下一步**: 阅读《简历分析和匹配》
"""

    output_file = company_path / "01_company_intel_brief.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template)

    print(f"  ✅ 已生成: {output_file.name}")
    return output_file


def generate_file_02_resume_matching(company_path, company, role, jd_file, resume_version):
    """生成文件 2: 简历分析和匹配"""
    print(f"\n📋 生成文件 2/5: 简历分析和匹配...")

    # 读取 JD 文件
    jd_content = ""
    if jd_file and os.path.exists(jd_file):
        with open(jd_file, 'r', encoding='utf-8') as f:
            jd_content = f.read()

    template = f"""# 简历-JD 匹配分析 - {company} {role}

**分析日期**: {datetime.now().strftime('%Y-%m-%d')}
**简历版本**: {resume_version}
**职位**: {role}
**公司**: {company}

---

## 📊 匹配度速览(精简版)

### 整体评分: ⭐⭐⭐⭐ (75/100)

**匹配等级**: 良好 - 推荐投递

**核心优势**:
- ✅ [优势 1]
- ✅ [优势 2]
- ✅ [优势 3]

**主要短板**:
- ❌ [短板 1]
- ⚠️ [短板 2]

### 快速对照

| 类别 | 匹配度 | 说明 |
|------|--------|------|
| 行业经验 | ⚠️ 60% | 缺乏行业背景 |
| 产品能力 | ✅ 90% | 方法论通用 |
| 技术理解 | ✅ 85% | 技术背景强 |
| 软技能 | ✅ 90% | 沟通协作好 |

---

## 详细版

### 一、匹配度总览

#### 能力象限图
```
      高匹配
         |
    II   |   I
  [能力]  [能力]
         |
---------+--------- 重要性
         |
   III   |   IV
  [能力]  [能力]
         |
      低匹配
```

---

### 二、详细对照表

| JD 要求 | 重要性 | 匹配度 | 差距说明 | 弥补策略 |
|---------|--------|--------|----------|---------|
| [要求1] | ⭐⭐⭐⭐⭐ | ✅ 90% | 完全匹配 | 保持优势 |
| [要求2] | ⭐⭐⭐⭐ | ⚠️ 60% | 需补充 | 提前学习 |
| [要求3] | ⭐⭐⭐ | ❌ 30% | 缺失 | 展示潜力 |

---

### 三、STAR 改写建议

#### 案例 1: [核心经历]

**【原】简历写法**:
```
[原始描述]
```

**【改】STAR 升级版**:
```
**S (Situation)**:
[背景描述,3-5句话]

**T (Task)**:
[任务目标,明确量化]

**A (Action)**:
• [行动1]
• [行动2]
• [行动3]

**R (Result)**:
• [结果1]: 数据支撑
• [结果2]: 数据支撑

**【🔗 关联 {role}】**:
[建立与目标职位的关联]
```

---

### 四、简历优化策略

#### 策略 1: 结构优化
[具体建议]

#### 策略 2: 措辞优化
[具体建议]

#### 策略 3: 关键词匹配
[JD 关键词列表及如何融入简历]

---

### 五、差距弥补方案

**最大短板**: [识别出的核心问题]

**应对策略**:
1. [策略1]
2. [策略2]
3. [策略3]

---

**建议阅读时间**: 20-30 分钟
**下一步**: 根据 STAR 建议优化简历
"""

    output_file = company_path / "02_resume_jd_matching.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template)

    print(f"  ✅ 已生成: {output_file.name}")
    return output_file


def generate_file_03_interview_prep(company_path, company, role, resume_version):
    """生成文件 3: 面试准备报告"""
    print(f"\n📋 生成文件 3/5: 面试准备报告...")

    template = f"""# 面试准备报告 - {company} {role}

**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}
**目标职位**: {role}
**简历版本**: {resume_version}

---

## 📊 快速速览(精简版)

### 核心策略
**定位**: [一句话定位你的核心优势]
**风险**: [最大风险点]
**应对**: [核心应对策略]

### 三轮面试关注点
- **Round 1 (HR)**: 稳定性、薪资、文化
- **Round 2 (业务)**: 实战能力、技术深度
- **Round 3 (高管)**: 潜力、商业思维、价值观

### 必备话术
**开场白(1分钟版)**:
```
[30秒自我介绍模板]
```

**核心优势**:
- [优势1一句话]
- [优势2一句话]
- [优势3一句话]

---

## 详细版

### 一、Round 1: HR 筛选面试

#### 关注重点
- 职业稳定性
- 薪资期望合理性
- 离职原因
- 文化契合度

#### 防坑话术

**Q: 为什么离开上家公司?**
**A (防坑话术)**:
```
[3个正面理由版本]
```

#### 准备建议
- [ ] 准备 3 个离职原因(真实但积极)
- [ ] 准备薪资区间(市场价 + 15-20%)
- [ ] 准备对公司的了解
- [ ] 准备职业规划(3-5 年)

---

### 二、Round 2: 业务负责人面试

#### 高概率问题

**问题 1: 遇到过最大的挑战?如何解决?**

**回答框架**:
```
[STAR 框架模板]
```

**示例答案**:
```
[完整示例]
```

#### 必杀技案例准备

**案例 1: 核心成就案例**
- **要求**: 与 JD 高度相关
- **结构**: STAR
- **数据**: 前后对比

**案例 2: 问题解决案例**
- **要求**: 展示分析能力
- **结构**: Problem-Analysis-Solution-Result
- **亮点**: 创新性

---

### 三、Round 3: 高管/终面

#### 高概率问题

**问题 1: 如何看待[行业/技术]的未来?**
**回答方向**: [行业洞察要点]

**问题 2: 3-5 年职业规划?**
**回答方向**: [清晰路径,与公司一致]

#### 宏观话题准备
- [话题1]: [核心观点]
- [话题2]: [核心观点]

---

### 四、风险缓解策略

**识别风险**: [从简历匹配分析中识别]

**应对话术**:
```
[针对每个风险的话术模板]
```

---

### 五、反向提问清单

**问业务的问题**:
1. [问题1]
2. [问题2]

**问团队的问题**:
1. [问题1]
2. [问题2]

**问文化的问题**:
1. [问题1]
2. [问题2]

---

**建议阅读时间**: 30-40 分钟
**下一步**: 模拟面试练习话术
"""

    output_file = company_path / "03_interview_prep_report.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template)

    print(f"  ✅ 已生成: {output_file.name}")
    return output_file


def generate_file_04_icebreaker(company_path, company, role, keywords, achievement):
    """生成文件 4: 破冰文案"""
    print(f"\n📋 生成文件 4/5: 破冰文案...")

    template = f"""# 破冰开场白 - {company} {role}

**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## 策略 A: 专业匹配型

### 适用场景
- HR 筛选、正规流程
- 大公司、成熟团队

### 开场白文案

```
看到贵司在招{keywords}方向的{role},我有{achievement},简历已备好,期待您的查看。
```

**字数**: [自动计算]

### 结构拆解
- **挂钩**: 看到贵司在招...
- **证明**: {achievement}
- **行动**: 简历已备好

---

## 策略 B: 业务洞察型

### 适用场景
- 业务负责人、创业公司
- 技术驱动公司

### 开场白文案

```
一直关注贵司{role}团队的发展,我之前在类似场景下{achievement},希望能聊聊具体的业务挑战。
```

**字数**: [自动计算]

### 结构拆解
- **挂钩**: 一直关注贵司...
- **证明**: {achievement}
- **行动**: 希望能聊聊...

---

## 使用指南

### 如何选择策略

**使用策略 A 当**:
- 应聘大公司、正规流程
- 对方是 HR 或招聘专员
- 强调匹配度和专业性

**使用策略 B 当**:
- 应聘创业公司、小团队
- 对方是业务负责人或技术 Leader
- 展示行业理解和业务思维

### 最佳发送时机
- 投递简历后 24 小时内(趁热打铁)
- 工作日上午 10-11 点或下午 3-4 点
- 避开周一上午和周五下午

### 禁忌词汇
- ❌ "希望能有一个机会"
- ❌ "我会努力学习"
- ❌ "请多多指教"
- ❌ "给我一个机会证明自己"

### 加分技巧
- ✅ 提及具体数据和成果
- ✅ 使用对方公司的产品
- ✅ 展示对公司业务的理解
- ✅ 表达合作意愿而非求职姿态

---

**使用建议**: 根据场景选择策略,发送前检查字数(建议 80-100 字)
"""

    output_file = company_path / "04_icebreaker_messages.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template)

    print(f"  ✅ 已生成: {output_file.name}")
    return output_file


def generate_file_05_final_report(company_path, company, role):
    """生成文件 5: 最终完整分析报告"""
    print(f"\n📋 生成文件 5/5: 最终完整分析报告...")

    template = f"""# 最终分析报告 - {company} {role}

**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## 📊 执行摘要(3分钟速览)

### 关键结论

**整体匹配度**: ⭐⭐⭐⭐ (75/100)

**核心优势**:
1. ✅ [优势1]
2. ✅ [优势2]
3. ✅ [优势3]

**核心风险**:
1. ❌ [风险1]
2. ⚠️ [风险2]
3. ⚠️ [风险3]

### 成功率评估

| 阶段 | 通过率 | 关键因素 |
|------|--------|---------|
| 简历筛选 | 70% | 简历优化程度 |
| 面试 | 65% | 准备充分度 |
| 最终 Offer | 50% | 综合竞争力 |

### 一句话建议
[最关键的一条建议]

---

## 一、关键发现

### 1.1 公司分析要点
- **定位**: [一句话]
- **优势**: [核心竞争力]
- **挑战**: [主要问题]
- **适合度**: [是否适合你]

### 1.2 简历匹配要点
- **匹配项**: [Top 3 匹配能力]
- **短板**: [Top 3 短板]
- **优化方向**: [核心优化策略]

### 1.3 面试准备要点
- **核心话术**: [最重要的话术]
- **必备案例**: [2-3 个案例类型]
- **风险应对**: [核心风险的应对]

---

## 二、行动计划

### 第一阶段: 简历优化(1-2天)
- [ ] 按照 STAR 建议重写 2-3 段核心经历
- [ ] 增加关键词匹配
- [ ] 优化结构和措辞
- [ ] 检查错别字和排版

### 第二阶段: 知识补课(3-5天)
- [ ] 公司背景研究(2-3小时)
- [ ] 行业知识学习(3-4小时)
- [ ] 竞品分析(2小时)
- [ ] 产品体验(1-2小时)

### 第三阶段: 案例准备(2-3天)
- [ ] 准备 2 个核心成就案例(STAR)
- [ ] 准备 1 个问题解决案例
- [ ] 准备 1 个快速学习案例
- [ ] 每个案例练习 3 遍以上

### 第四阶段: 模拟面试(1天)
- [ ] 自我介绍 3 个版本(1/3/5分钟)
- [ ] 高频问题回答练习
- [ ] 反向提问清单
- [ ] 整体面试流程模拟

**总计准备时间**: 7-11 天

---

## 三、快速查阅

### 关键数据
- **公司规模**: [数据]
- **目标职位级别**: [P几]
- **薪资范围**: [X-Y万]

### 关键话术
**开场白(1分钟)**:
```
[模板]
```

**核心优势表达**:
```
[3句话版本]
```

**短板应对**:
```
[1句话版本]
```

### 关键问题
1. [最高频问题及答案]
2. [第二高频问题及答案]
3. [第三高频问题及答案]

---

## 四、投递建议

### 投递时机
**建议**: 完成第一、二阶段后投递

**理由**: [说明]

### 投递渠道
1. **内推**(推荐): [寻找内推方法]
2. **官网**: [投递注意事项]
3. **Boss直聘**: [使用破冰文案]
4. **LinkedIn**: [英文简历准备]

---

## 五、复习清单(面试前1天)

### 必看内容
- [ ] 公司背景速览(5分钟)
- [ ] 简历匹配度速览(3分钟)
- [ ] 面试核心话术(10分钟)
- [ ] 破冰文案(2分钟)

### 必带材料
- [ ] 简历打印版(3份)
- [ ] 笔记本+笔
- [ ] 问题清单

### 心理准备
- 保持自信但不傲慢
- 诚实但不过度暴露短板
- 展示热情但不desperat

---

## 六、祝福与鼓励

相信你已经做好充分准备!

**记住**:
1. ✅ 你的优势很明显: [Top 1优势]
2. ✅ 你已经补齐了知识短板
3. ✅ 你准备了充足的案例和话术
4. ✅ 保持真诚和自信

**加油!期待你的好消息!** 🎉

---

**生成工具**: Interview Intel v6.0
**文件清单**:
1. ✅ 01_company_intel_brief.md
2. ✅ 02_resume_jd_matching.md
3. ✅ 03_interview_prep_report.md
4. ✅ 04_icebreaker_messages.md
5. ✅ 05_final_analysis_report.md (当前文件)
"""

    output_file = company_path / "05_final_analysis_report.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template)

    print(f"  ✅ 已生成: {output_file.name}")
    return output_file


def main():
    parser = argparse.ArgumentParser(
        description='Interview Intel v6.0 - 一键生成 5 个标准面试准备文件'
    )

    parser.add_argument('--base-path', required=True, help='项目根目录')
    parser.add_argument('--company', required=True, help='公司名称')
    parser.add_argument('--role', required=True, help='职位名称')
    parser.add_argument('--jd-file', help='JD 文件路径')
    parser.add_argument('--resume-version', default='v1.0', help='简历版本')
    parser.add_argument('--industry', default='', help='所属行业')
    parser.add_argument('--keywords', default='', help='关键词(逗号分隔)')
    parser.add_argument('--achievement', default='', help='核心成就')
    parser.add_argument('--years', type=int, default=5, help='工作年限')

    args = parser.parse_args()

    print("=" * 60)
    print("🚀 Interview Intel v6.0 - 一键生成面试准备包")
    print("=" * 60)
    print(f"\n目标公司: {args.company}")
    print(f"目标职位: {args.role}")
    print(f"简历版本: {args.resume_version}")
    print()

    # 创建文件夹
    print("📁 创建文件夹结构...")
    company_path = create_company_folder(args.base_path, args.company)
    print(f"  ✅ 文件夹已创建: {company_path}")

    # 生成 5 个标准文件
    files = []

    # 文件 1: 公司背景
    file1 = generate_file_01_company_intel(
        company_path, args.company, args.role, args.industry
    )
    files.append(file1)

    # 文件 2: 简历匹配
    file2 = generate_file_02_resume_matching(
        company_path, args.company, args.role, args.jd_file, args.resume_version
    )
    files.append(file2)

    # 文件 3: 面试准备
    file3 = generate_file_03_interview_prep(
        company_path, args.company, args.role, args.resume_version
    )
    files.append(file3)

    # 文件 4: 破冰文案
    file4 = generate_file_04_icebreaker(
        company_path, args.company, args.role, args.keywords, args.achievement
    )
    files.append(file4)

    # 文件 5: 最终报告
    file5 = generate_file_05_final_report(
        company_path, args.company, args.role
    )
    files.append(file5)

    # 完成
    print("\n" + "=" * 60)
    print("✨ 所有文件生成完成!")
    print("=" * 60)
    print(f"\n📂 文件保存位置: {company_path}")
    print("\n📄 生成的文件:")
    for i, file in enumerate(files, 1):
        print(f"  {i}. {file.name}")

    print("\n📖 阅读顺序建议:")
    print("  1️⃣  01_company_intel_brief.md (了解公司)")
    print("  2️⃣  02_resume_jd_matching.md (优化简历)")
    print("  3️⃣  03_interview_prep_report.md (准备面试)")
    print("  4️⃣  04_icebreaker_messages.md (投递破冰)")
    print("  5️⃣  05_final_analysis_report.md (总览复习)")

    print("\n💡 提示:")
    print("  - 每个文件都有【精简版】(首部)和【详细版】")
    print("  - 首次阅读建议看详细版")
    print("  - 复习时只看精简版即可")
    print("  - 面试前看最终报告快速热身")

    print("\n🎉 祝你面试成功!")
    print()


if __name__ == '__main__':
    main()
