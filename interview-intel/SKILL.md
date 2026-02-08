---
name: interview-intel
description: Comprehensive job application strategy system with one-click workflow combining resume optimization, interview preparation, and recruitment game theory. Use when the user needs to (1) Generate complete interview preparation package with a single command (JD analysis + resume matching + interview strategy + icebreaker messages), (2) Analyze and match resume to JD with STAR-based suggestions, (3) Generate interview attack-defense strategies for HR/Business/Executive rounds, (4) Create compelling icebreaker messages for platforms like Boss直聘, (5) Track interviews and maintain application records. Features all_in_one.py script for instant setup. Organizes all materials by company in a structured folder hierarchy under companies/ directory.
---

# Interview Intel

## Overview

A comprehensive job application strategy system that helps candidates bridge the gap between their resume and target positions in a competitive job market. Goes beyond simple document preparation to implement recruitment game theory, STAR-based optimization, and multi-round interview attack-defense strategies.

**Core Capabilities**:
1. **Smart Resume-JD Matching**: Deep JD analysis with hidden insights + STAR-based resume rewrite suggestions
2. **Interview Strategy Generation**: Simulates HR/Business/Executive rounds with defense scripts and killer cases
3. **Icebreaker Message Creation**: Generates platform-optimized opening messages (Boss直聘, LinkedIn)
4. **Interview Tracking**: Structured tracking of all application stages and feedback
5. **Resume Version Management**: Maintains multiple resume versions with usage tracking

**IMPORTANT**: All materials are organized under `companies/[CompanyName]/` directory structure for easy navigation.

## ⚡ Quick Start: One-Click Execution

**The fastest way to use this skill**: Run the all-in-one workflow script that generates everything in one command.

### Basic Usage

```bash
python scripts/all_in_one.py execute \
  --base-path ~/InterviewIntel \
  --company "公司名称" \
  --role "职位名称" \
  --jd-file jd.txt \
  --resume-version v1.0
```

### What It Does

One command generates:
1. ✅ Company folder structure (`companies/公司名称/`)
2. ✅ JD deep analysis with hidden insights
3. ✅ Resume-JD matching report with STAR rewrite suggestions
4. ✅ Interview attack-defense strategy (HR/Business/Executive rounds)
5. ✅ Icebreaker messages (Strategy A + B)
6. ✅ All raw data and metadata

### Full Example

```bash
python scripts/all_in_one.py execute \
  --base-path ~/InterviewIntel \
  --company "京东物流" \
  --role "运输产品经理" \
  --jd-file jd_logistics.txt \
  --resume-version v1.0 \
  --resume-file my_resume.txt \
  --achievement "主导 AI 产品从 0 到 1,用户增长 300%" \
  --years 6 \
  --insight "物流供应链智能化"
```

### Output Structure

All files are saved to `companies/京东物流/`:
```
companies/京东物流/
├── jd_analysis_运输产品经理.md              # JD 深度分析
├── resume_mapping_运输产品经理.md           # 简历匹配报告
├── interview_strategy_运输产品经理.md       # 面试攻防策略
├── icebreaker_京东物流_运输产品经理.md      # 破冰文案
├── raw_data/
│   ├── jd_original_运输产品经理.txt        # 原始 JD
│   └── jd_keywords_运输产品经理.txt        # 关键词提取
└── workflow_metadata_运输产品经理.json      # 工作流元数据
```

### When to Use One-Click vs Individual Scripts

**Use one-click workflow when**:
- Starting analysis for a new company/role
- Need complete preparation package quickly
- Want consistent output structure

**Use individual scripts when**:
- Only need specific analysis (e.g., just JD keywords)
- Iterating on specific sections
- Fine-tuning parameters for advanced use cases

## New Features (v4.0 → v5.0)

### 1. Resume Optimizer (`resume_optimizer.py`)
- **JD Deep Analysis**: Extracts hard requirements, core competencies, and hidden insights ("what they really want")
- **STAR-Based Rewriting**: Provides structured suggestions to rewrite experiences using Situation-Task-Action-Result framework
- **Keyword Highlighting**: Identifies and highlights matching keywords between resume and JD
- **Match Score Calculation**: Quantifies resume-JD alignment across multiple dimensions

### 2. Interview Strategy Generator (`interview_strategy.py`)
- **Round 1 (HR)**: Risk identification + defense scripts for common concerns (job hopping, gaps, career change)
- **Round 2 (Business)**: Predicts likely questions + killer case templates + deep-dive topic preparation
- **Round 3 (Executive)**: Strategic questions + macro topics + business thinking preparation
- **Risk Mitigation**: Turns weaknesses into strengths with tactical approaches

### 3. Icebreaker Generator (`icebreaker_generator.py`)
- **Strategy A (Professional Match)**: For HR and formal processes - direct, data-driven, concise
- **Strategy B (Business Insight)**: For business leads and startups - warm, insightful, peer-to-peer
- **Usage Guide**: When to use each strategy, timing, forbidden phrases, bonus tips

## Core Principles

1. **Precision Matching**: Align resume with JD keywords without fabrication
2. **STAR Framework**: All experience rewrites follow Situation-Task-Action-Result structure with quantified results
3. **Transparency**: Hidden insights expose what recruiters really want beyond surface requirements
4. **No BS**: Direct, professional output focused on passing screening stages

## File Organization

### Automatic Folder Structure

All company materials are organized under `companies/` directory:

```
companies/
└── [CompanyName]/
    ├── company_intel_brief.md              # Company background research
    ├── jd_analysis_[RoleName].md          # JD analysis for specific roles
    ├── jd_deep_analysis_[RoleName].json   # 🆕 Deep JD insights (hidden requirements)
    ├── resume_mapping_[RoleName].md       # Resume-to-JD alignment
    ├── resume_optimization_[RoleName].md  # 🆕 STAR-based rewrite suggestions
    ├── interview_prep_[RoleName].md       # Comprehensive prep report
    ├── interview_strategy_[RoleName].md   # 🆕 Attack-defense strategies
    ├── icebreaker_[CompanyName]_[Role].md # 🆕 Opening messages
    ├── raw_data/                          # Original data
    │   ├── jd_original_[RoleName].txt    # Original JD text
    │   └── jd_keywords_[RoleName].txt    # Keyword extraction output
    ├── resumes/                           # Company-specific resume versions
    │   ├── resume_[RoleName]_v1.pdf      # Tailored resume versions
    │   └── tailoring_log.json            # Resume customization log
    ├── interviews/                        # Interview tracking
    │   ├── tracking.json                 # Structured interview data
    │   ├── round_1_notes.md              # Detailed round notes
    │   ├── round_2_notes.md
    │   └── feedback.md                   # Interview feedback
    ├── notes.md                           # Interview notes and updates
    └── README.md                          # Folder overview
```

**Global directories**:
```
resumes/                               # Master resume versions
├── master_resume_v1.0.pdf
├── master_resume_v2.0.pdf
├── resume_registry.json               # Version tracking
└── CHANGELOG.md                       # Version history
```

### Setup Tool

**Before starting any analysis**, run the setup script to create the folder structure:

```bash
python scripts/setup_company_folder.py <base_path> "<CompanyName>" ["<RoleName>"]
```

**Example**:
```bash
python scripts/setup_company_folder.py ~/InterviewIntel "Google" "Senior Backend Engineer"
```

The script will:
1. Create the company folder with sanitized name
2. Set up subfolders: raw_data/, resumes/, interviews/
3. Generate README.md and notes.md templates
4. Initialize tracking.json for interview tracking
5. Output JSON with all file paths for easy reference

**Always save outputs to the appropriate files in the company folder structure.**

## Core Capabilities

### 1. Company Intelligence Gathering
Research and compile actionable intelligence about target companies, focusing on:
- Product and business model understanding
- Recent developments and strategic direction
- Technology stack and engineering culture
- Team structure and key leadership

**When to use**: Before starting interview prep, or when user asks to research a company.

**Output**: Use the [company_intel_brief_template.md](assets/company_intel_brief_template.md) to create structured company intelligence reports.

**Process**:
1. Start with company basics (size, stage, funding, industry)
2. Understand their products and target market
3. Research recent developments (last 6-12 months)
4. Investigate culture and values (Glassdoor, blog posts)
5. Identify key team members and leadership
6. Compile interview process intelligence if available

**Reference**: See [company_research_guide.md](references/company_research_guide.md) for detailed research framework and source recommendations.

### 2. Job Description Analysis
Systematically extract and categorize requirements from job postings:
- Technical skills (must-have vs nice-to-have)
- Experience requirements and levels
- Soft skills and cultural fit indicators
- Responsibility scope and impact expectations

**When to use**: When user provides a JD or asks to analyze a role's requirements.

**Tools**:
- **Script**: Use [extract_jd_keywords.py](scripts/extract_jd_keywords.py) to automatically extract technical keywords, experience requirements, and common phrases from JD text
  - Usage: `python scripts/extract_jd_keywords.py jd_file.txt` or pipe JD text via stdin
  - Output: Categorized technical skills, experience levels, soft skills, and requirement strength (required vs preferred)

**Process**:
1. Run the extraction script for initial keyword analysis
2. Classify the role (level, type, team focus)
3. Separate required vs preferred skills
4. Identify experience expectations (years, complexity, scale)
5. Extract soft skill emphasis
6. Analyze team stage and context clues
7. Prioritize preparation topics

**Reference**: See [jd_analysis_framework.md](references/jd_analysis_framework.md) for comprehensive analysis structure and output templates.

### 3. Resume-JD Alignment Mapping
Map candidate background to role requirements to identify:
- Direct matches (strong evidence)
- Adjacent matches (transferable experience)
- Gaps (areas to address or learn)
- Key stories to prepare

**When to use**: After analyzing JD and when user provides their resume or background.

**Process**:
1. Extract key requirements from JD analysis
2. For each requirement, find resume evidence
3. Categorize match strength (strong/medium/weak)
4. Identify gaps and develop mitigation strategies
5. Select top 5-7 stories that demonstrate strengths
6. Prepare talking points for gaps

**Output Format**:
- Strength assessment matrix (requirement → evidence → match type → strength)
- Gap analysis with mitigation strategies
- Prioritized story preparation list
- Questions to ask based on gaps or interests

**Reference**: See [resume_jd_mapping.md](references/resume_jd_mapping.md) for detailed mapping methodology and story preparation templates.

### 4. Resume Version Management
Manage multiple resume versions with complete file storage and tracking:
- Create and store master resume versions with metadata
- Tailor resumes for specific companies and roles
- Track which version was used for each application
- Compare versions to understand changes
- Recommend best version for a given JD

**When to use**: When user has multiple resume versions or needs to tailor resume for specific applications.

**Tools**:
- **Script**: Use [resume_manager.py](scripts/resume_manager.py) for complete resume version management
  - Create new versions: `python scripts/resume_manager.py create --file resume.pdf --version v1.0 --desc "Description" --target "Backend,Full-stack" --skills "Python,AWS"`
  - List all versions: `python scripts/resume_manager.py list [--filter Backend]`
  - Tailor for company: `python scripts/resume_manager.py tailor --base v1.0 --company SIF --role "Backend Engineer" --output ~/InterviewIntel/SIF/resumes/`
  - Compare versions: `python scripts/resume_manager.py compare --v1 v1.0 --v2 v2.0`
  - Get recommendations: `python scripts/resume_manager.py recommend --target "Backend Engineer" --requirements "Python,Docker,AWS"`
  - Usage report: `python scripts/resume_manager.py report [--version v1.0]`

**Process**:
1. Create master resume versions in the global `resumes/` folder
2. Each version has metadata: target positions, key skills, description
3. When applying to a company, tailor a version for that specific role
4. Tailored versions are stored in the company's `resumes/` folder
5. Track which version was used in interview tracking data

**Global Resume Structure**:
```
resumes/
├── master_resume_v1.0.pdf           # Master version files
├── master_resume_v2.0.pdf
├── resume_registry.json             # Version metadata and tracking
└── CHANGELOG.md                     # Version history
```

**Template**: Use [resume_changelog_template.md](assets/resume_changelog_template.md) to document resume version changes.

### 5. Interview Tracking
Track interview progress with structured data and detailed notes:
- Initialize tracking for each application
- Record each interview round with metadata
- Track interviewer information and focus areas
- Document feedback, difficulty, and confidence levels
- Maintain timeline of all events
- Record final decision and offer details

**When to use**: When user starts applying to companies and scheduling interviews.

**Tools**:
- **Script**: Use [interview_tracker.py](scripts/interview_tracker.py) for structured interview tracking
  - Initialize tracking: `python scripts/interview_tracker.py init --company-path ~/InterviewIntel/SIF --company SIF --role "Backend Engineer" --resume v2.0`
  - Add interview round: `python scripts/interview_tracker.py add-round --company-path ~/InterviewIntel/SIF --round 1 --name "Phone Screen" --date 2026-01-25 --interviewer "John Doe"`
  - Update round status: `python scripts/interview_tracker.py update --company-path ~/InterviewIntel/SIF --round 1 --status completed --result passed --difficulty 3 --confidence 4`
  - View status: `python scripts/interview_tracker.py status --company-path ~/InterviewIntel/SIF`
  - Generate timeline: `python scripts/interview_tracker.py timeline --company-path ~/InterviewIntel/SIF [--format text|json]`

**Process**:
1. Initialize tracking when application is submitted
2. Add interview rounds as they are scheduled
3. For each round, create detailed notes using the template
4. Update round status and results after completion
5. Track follow-up actions (thank you emails, connections)
6. Update final decision when received

**Tracking Data Structure**:
- Application info: company, role, date, resume version used
- Timeline: chronological events (submitted, scheduled, completed, decision)
- Interview rounds: detailed info per round (interviewer, focus areas, result, feedback)
- Overall statistics: pass rate, total rounds, current status
- Decision: final outcome and offer details if applicable

**Template**: Use [interview_round_notes_template.md](assets/interview_round_notes_template.md) for detailed round notes.

### 6. Analytics and Statistics
Generate comprehensive statistics and visualizations across all applications:
- Global statistics: total applications, response rate, offer rate
- Resume version performance: which versions get more responses
- Position type analysis: success rates by role type
- Interview performance: pass rates, difficulty, confidence tracking
- Timeline visualization: application history and trends
- Export data to CSV for external analysis
- Generate HTML dashboard with interactive charts

**When to use**: When user wants to review overall progress or analyze interview performance.

**Tools**:
- **Script**: Use [analytics_generator.py](scripts/analytics_generator.py) for statistics and reports
  - Generate global stats: `python scripts/analytics_generator.py generate --scope global`
  - Company-specific stats: `python scripts/analytics_generator.py generate --scope company --company SIF`
  - Export to CSV: `python scripts/analytics_generator.py export --format csv --output interview_data.csv`
  - Generate HTML dashboard: `python scripts/analytics_generator.py dashboard --output dashboard.html`

**Process**:
1. Script scans all company folders for tracking.json files
2. Aggregates data across all applications
3. Calculates statistics: response rates, pass rates, averages
4. Groups by resume version, position type, timeline
5. Generates visualizations and reports

**Output Formats**:
- JSON: Detailed statistics in `.analytics/global_stats.json`
- CSV: Tabular data for Excel/spreadsheet analysis
- HTML: Interactive dashboard with Chart.js visualizations

**Analytics Structure**:
```
.analytics/
├── global_stats.json                # Aggregated statistics
├── company_stats.json               # Per-company breakdowns
├── resume_usage.json                # Resume version performance
└── exports/
    ├── interview_data.csv           # CSV exports
    └── dashboard.html               # Interactive dashboard
```

### 7. Comprehensive Interview Preparation Report
Generate a complete prep document combining all analyses:
- Company intelligence summary
- JD requirements breakdown
- Resume alignment and gaps
- Preparation priorities
- Story bank (STAR format)
- Questions to ask
- Key talking points

**When to use**: After completing company research, JD analysis, and resume mapping.

**Template**: Use [interview_prep_report_template.md](assets/interview_prep_report_template.md) as the structure for final preparation reports.

**This should include**:
- Executive summary with key takeaways
- Company overview and recent context
- Role analysis with technical and soft skill requirements
- Alignment matrix showing strengths and gaps
- Top 5+ prepared stories in STAR format
- Prioritized study topics
- Strategic questions to ask
- Key talking points and value proposition

## Workflow

### Standard Interview Prep Flow

```
1. User provides target company and role
   ↓
2. Setup company folder structure
   - Run: setup_company_folder.py <base_path> "<Company>" "<Role>"
   - Creates organized folder structure
   - Outputs file paths in JSON
   ↓
3. Gather company intelligence
   - Research company basics, products, culture
   - Save to: [Company]/company_intel_brief.md
   ↓
4. Analyze job description
   - Save original JD to: [Company]/raw_data/jd_original_[Role].txt
   - Run JD extraction script, save output to: [Company]/raw_data/jd_keywords_[Role].txt
   - Perform detailed analysis
   - Save to: [Company]/jd_analysis_[Role].md
   ↓
5. Map resume to requirements
   - Assess alignment (strong/medium/weak)
   - Identify gaps and prepare stories
   - Save to: [Company]/resume_mapping_[Role].md
   ↓
6. Generate comprehensive prep report
   - Combine all analyses
   - Prioritize preparation
   - Create story bank
   - Save to: [Company]/interview_prep_[Role].md
   ↓
7. Maintain interview notes
   - Update [Company]/notes.md with interview experiences
   - Track timeline and follow-ups
```

### Quick JD Analysis Flow

```
1. User provides JD text or file
   ↓
2. Setup company folder (if not exists)
   - Run: setup_company_folder.py <base_path> "<Company>" "<Role>"
   ↓
3. Save original JD
   - Save to: [Company]/raw_data/jd_original_[Role].txt
   ↓
4. Run extract_jd_keywords.py script
   - Save output to: [Company]/raw_data/jd_keywords_[Role].txt
   ↓
5. Perform detailed JD analysis
   - Save to: [Company]/jd_analysis_[Role].md
```

### Company Research Only Flow

```
1. User requests company research
   ↓
2. Setup company folder (if not exists)
   - Run: setup_company_folder.py <base_path> "<Company>"
   ↓
3. Gather intelligence using research guide
   ↓
4. Save to: [Company]/company_intel_brief.md
```

## Usage Examples

### Example 1: Full Interview Prep

**User**: "Help me prepare for a Senior Backend Engineer interview at DataCorp. Here's the JD: [JD text]. And here's my resume: [resume]."

**Response**:
1. Run setup_company_folder.py to create DataCorp folder structure
2. Save original JD to DataCorp/raw_data/jd_original_Senior_Backend_Engineer.txt
3. Extract and analyze JD using the script, save to raw_data/jd_keywords_Senior_Backend_Engineer.txt
4. Research DataCorp company intelligence, save to DataCorp/company_intel_brief.md
5. Map user's resume to JD requirements, save to DataCorp/resume_mapping_Senior_Backend_Engineer.md
6. Generate comprehensive Interview Prep Report, save to DataCorp/interview_prep_Senior_Backend_Engineer.md
7. Highlight top 3 strengths and top 2 gaps in the report
8. Provide 5 key stories to prepare
9. Suggest priority study topics

### Example 2: JD Analysis Only

**User**: "Can you analyze this job description and tell me what I should focus on? [JD text]"

**Response**:
1. Ask for company name and role title
2. Run setup_company_folder.py to create folder structure
3. Save JD to [Company]/raw_data/jd_original_[Role].txt
4. Run extract_jd_keywords.py, save to [Company]/raw_data/jd_keywords_[Role].txt
5. Perform detailed analysis using framework
6. Save structured JD analysis to [Company]/jd_analysis_[Role].md
7. Suggest preparation priorities

### Example 3: Company Research

**User**: "I have an interview with TechStartup next week. What should I know about them?"

**Response**:
1. Run setup_company_folder.py ~/InterviewIntel "TechStartup"
2. Research company using company_research_guide
3. Gather product, business, culture info
4. Find recent developments
5. Identify interview relevance
6. Save Company Intel Brief to TechStartup/company_intel_brief.md

## Tips for Effective Use

### When Gathering Company Intelligence
- Start with company website, blog, and LinkedIn
- Try their product if possible (hands-on experience impresses)
- Look for recent news (last 6 months most relevant)
- Check Glassdoor for culture insights
- Note engineering blog posts for technical culture

### When Analyzing JDs
- Pay attention to what's mentioned repeatedly (true priorities)
- Distinguish "must have" from "nice to have" (often buried in language)
- Look for scale indicators (users, traffic, data volume)
- Note the team stage (build/scale/maintain mode)
- Consider context: same title means different things at different companies

### When Mapping Resume to JD
- Be honest about match strength (gaps are opportunities to show learning ability)
- Prepare stories for your strongest matches
- For gaps, emphasize transferable concepts
- Quantify everything possible (team size, user scale, performance improvements)
- Practice articulating the "why" behind technical decisions

### When Preparing Stories
- Use STAR format (Situation, Task, Action, Result)
- Include specific metrics and outcomes
- Prepare 2-minute and 5-minute versions
- Make them adaptable to different question angles
- Focus on your individual contributions, not just "we"

### General Best Practices
- Update analysis as you learn more through interviews
- Prepare questions that show you've done research
- Connect your experience to their specific challenges
- Show enthusiasm for their product/mission
- Be ready to discuss both successes and learning from failures

## Resources Reference

### Scripts

- **all_in_one.py** ⭐ (推荐): One-click workflow for complete interview preparation
  - Usage: `python scripts/all_in_one.py execute --base-path <path> --company <name> --role <title> --jd-file <file> --resume-version <version> [options]`
  - Generates: JD analysis, resume matching, interview strategy, icebreaker messages - all in one command
  - Best for: Starting analysis for a new company/role

- **setup_company_folder.py**: Creates organized folder structure for each company/role
  - Usage: `python scripts/setup_company_folder.py <base_path> "<Company>" ["<Role>"]`
  - Outputs: JSON with all file paths

- **extract_jd_keywords.py**: Automated JD keyword and requirement extraction
  - Usage: `python scripts/extract_jd_keywords.py jd_file.txt`
  - Outputs: Categorized technical skills, experience, soft skills

- **resume_optimizer.py**: JD deep analysis and resume-JD matching with STAR suggestions
  - Usage: `python scripts/resume_optimizer.py analyze --company-path <path> --company <name> --role <title> --jd-file <file> --resume-version <version>`
  - Generates: JD analysis + resume matching report

- **interview_strategy.py**: Multi-round interview attack-defense strategy generator
  - Usage: `python scripts/interview_strategy.py generate --company-path <path> --company <name> --role <title> --resume-version <version>`
  - Generates: HR/Business/Executive round strategies

- **icebreaker_generator.py**: Opening message generator for job applications
  - Usage: `python scripts/icebreaker_generator.py generate --company-path <path> --company <name> --role <title> --keywords <kw1,kw2> --achievement <text>`
  - Generates: Strategy A (Professional) + Strategy B (Business Insight)

- **resume_manager.py**: Complete resume version management system
  - Usage: `python scripts/resume_manager.py [create|list|tailor|compare|recommend|report] [options]`
  - Manages: Master versions, tailored versions, comparisons, recommendations

- **interview_tracker.py**: Structured interview progress tracking
  - Usage: `python scripts/interview_tracker.py [init|add-round|update|status|timeline] [options]`
  - Tracks: Applications, rounds, interviewers, feedback, decisions

- **analytics_generator.py**: Statistics and visualization generation
  - Usage: `python scripts/analytics_generator.py [generate|export|dashboard] [options]`
  - Produces: Global stats, CSV exports, HTML dashboards

### References (Load as Needed)
- **company_research_guide.md**: Framework for researching target companies
- **jd_analysis_framework.md**: Structured approach to analyzing job descriptions
- **resume_jd_mapping.md**: Methods for aligning resume experience to JD requirements

### Assets (Templates for Output)
- **company_intel_brief_template.md**: Template for company research output
- **interview_prep_report_template.md**: Comprehensive interview preparation report template
- **resume_changelog_template.md**: Template for documenting resume version changes
- **interview_round_notes_template.md**: Template for detailed interview round notes

Load reference files when you need detailed guidance on specific analysis steps. Use asset templates as the structure for final outputs.

## File Management Best Practices

1. **Always start with folder setup**: Run setup_company_folder.py before creating any files
2. **Save all outputs to company folders**: Keep materials organized by company name
3. **Use consistent naming**: Script automatically sanitizes names (e.g., "Google LLC" → "Google_LLC")
4. **Track multiple roles**: Same company, different roles → separate files with role suffix
5. **Manage resume versions**: Store master versions globally, tailored versions per company
6. **Initialize tracking early**: Run interview_tracker.py init when submitting application
7. **Update tracking regularly**: Keep interview status and feedback current
8. **Take detailed notes**: Use the round notes template for each interview
9. **Generate analytics periodically**: Review progress with analytics_generator.py
10. **Update notes.md**: Keep interview timeline and learnings in the notes file
11. **Preserve raw data**: Always save original JD and script outputs in raw_data/
