#!/usr/bin/env python3
"""
Company Folder Setup Script

Creates organized folder structure for each company's interview preparation materials.
Ensures consistent organization across multiple interview prep sessions.
"""

import os
import sys
import re
import json
from pathlib import Path
from datetime import datetime


def sanitize_name(name: str) -> str:
    """
    Sanitize company or role name for use as folder/file name.

    Args:
        name: Company or role name

    Returns:
        Sanitized name suitable for folder/file naming
    """
    # Remove special characters, keep alphanumeric, spaces, hyphens, underscores
    sanitized = re.sub(r'[^\w\s-]', '', name)
    # Replace spaces with underscores
    sanitized = re.sub(r'\s+', '_', sanitized)
    # Remove consecutive underscores
    sanitized = re.sub(r'_+', '_', sanitized)
    # Trim underscores from start/end
    sanitized = sanitized.strip('_')
    return sanitized


def create_company_folder(base_path: str, company_name: str, role_name: str = None) -> dict:
    """
    Create organized folder structure for a company's interview prep.

    Args:
        base_path: Base directory for all interview prep materials
        company_name: Name of the company
        role_name: Optional role name for role-specific files

    Returns:
        Dictionary with paths to created folders and suggested file names
    """
    # Sanitize names
    company_folder = sanitize_name(company_name)
    role_suffix = f"_{sanitize_name(role_name)}" if role_name else ""

    # Create companies directory if not exists
    companies_path = Path(base_path) / "companies"
    companies_path.mkdir(parents=True, exist_ok=True)

    # Create company folder under companies/
    company_path = companies_path / company_folder
    company_path.mkdir(parents=True, exist_ok=True)

    # Create subfolders
    raw_data_path = company_path / "raw_data"
    raw_data_path.mkdir(exist_ok=True)

    resumes_path = company_path / "resumes"
    resumes_path.mkdir(exist_ok=True)

    interviews_path = company_path / "interviews"
    interviews_path.mkdir(exist_ok=True)

    # Prepare file paths
    timestamp = datetime.now().strftime("%Y%m%d")

    paths = {
        'company_folder': str(company_path),
        'raw_data_folder': str(raw_data_path),
        'resumes_folder': str(resumes_path),
        'interviews_folder': str(interviews_path),
        'company_intel': str(company_path / "company_intel_brief.md"),
        'notes': str(company_path / "notes.md"),
        'tracking': str(interviews_path / "tracking.json"),
    }

    # Add role-specific paths if role is provided
    if role_name:
        paths.update({
            'jd_analysis': str(company_path / f"jd_analysis{role_suffix}.md"),
            'resume_mapping': str(company_path / f"resume_mapping{role_suffix}.md"),
            'interview_prep': str(company_path / f"interview_prep{role_suffix}.md"),
            'jd_original': str(raw_data_path / f"jd_original{role_suffix}.txt"),
            'jd_keywords': str(raw_data_path / f"jd_keywords{role_suffix}.txt"),
        })

    # Create README if it doesn't exist
    readme_path = company_path / "README.md"
    if not readme_path.exists():
        create_readme(readme_path, company_name, role_name)

    # Initialize tracking.json if role is provided and it doesn't exist
    tracking_path = interviews_path / "tracking.json"
    if role_name and not tracking_path.exists():
        create_tracking_template(tracking_path, company_name, role_name)

    return paths


def create_readme(readme_path: Path, company_name: str, role_name: str = None):
    """Create a README file in the company folder."""
    content = f"""# {company_name} - Interview Preparation

**Created**: {datetime.now().strftime("%Y-%m-%d")}
**Status**: In Progress

## Folder Structure

- `company_intel_brief.md` - Company background research and intelligence
- `jd_analysis_*.md` - Job description analysis for specific roles
- `resume_mapping_*.md` - Resume-to-JD alignment analysis
- `interview_prep_*.md` - Comprehensive interview preparation reports
- `raw_data/` - Original JD files and extracted keyword data
- `resumes/` - Tailored resume versions for this company
- `interviews/` - Interview tracking and round notes
  - `tracking.json` - Structured interview progress data
  - `round_X_notes.md` - Detailed notes for each round
- `notes.md` - Interview notes, updates, and learnings

## Roles

"""

    if role_name:
        content += f"- {role_name} (Created: {datetime.now().strftime('%Y-%m-%d')})\n"
    else:
        content += "- [No roles added yet]\n"

    content += """
## Timeline

- [ ] Company research completed
- [ ] JD analysis completed
- [ ] Resume mapping completed
- [ ] Interview prep report generated
- [ ] Stories prepared
- [ ] Interview scheduled
- [ ] Interview completed
- [ ] Follow-up sent

## Notes

[Add any quick notes or insights here]
"""

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)


def create_notes_template(notes_path: Path, company_name: str):
    """Create a notes template file."""
    content = f"""# Interview Notes - {company_name}

## Quick Links
- [Company Intel Brief](company_intel_brief.md)
- [Interview Prep Reports](#)

---

## Interview Timeline

### [Date] - [Interview Round]
**Interviewer**: [Name, Title]
**Duration**: [Minutes]
**Focus**: [Technical/Behavioral/System Design/etc.]

#### Key Questions
1. [Question 1]
   - My answer: [Brief notes]
   - Follow-up: [Any follow-up discussion]

2. [Question 2]
   - My answer: [Brief notes]

#### Technical Discussion
- [Topic 1]: [Notes]
- [Topic 2]: [Notes]

#### Insights Gained
- [Insight about company/team/role]
- [Technical challenge they're facing]

#### My Questions Asked
1. [Question]: [Their answer summary]
2. [Question]: [Their answer summary]

#### Overall Impression
[How did it go? What went well? What could be improved?]

---

## Research Updates

### [Date]
- [New information learned about company]
- [Product updates or news]

---

## Preparation Improvements

### Things to Review More
- [ ] [Topic 1]
- [ ] [Topic 2]

### Stories to Refine
- [ ] [Story about X project]
- [ ] [Story about Y challenge]

---

## Follow-up Actions

- [ ] Send thank you email to [Interviewer]
- [ ] Research [specific technology mentioned]
- [ ] Prepare for next round focus on [topic]
"""

    with open(notes_path, 'w', encoding='utf-8') as f:
        f.write(content)


def create_tracking_template(tracking_path: Path, company_name: str, role_name: str):
    """Create an interview tracking JSON template."""
    tracking_data = {
        "application": {
            "company": company_name,
            "role": role_name,
            "application_date": datetime.now().strftime("%Y-%m-%d"),
            "application_method": "",
            "referral": None,
            "resume_version_used": "",
            "cover_letter": False,
            "jd_file": ""
        },
        "timeline": [
            {
                "date": datetime.now().strftime("%Y-%m-%d"),
                "event": "Application Submitted",
                "status": "submitted"
            }
        ],
        "interviews": [],
        "overall_status": "submitted",
        "current_stage": "application_submitted",
        "total_rounds_expected": 0,
        "total_rounds_completed": 0,
        "pass_rate": 0.0,
        "decision": None,
        "decision_date": None,
        "offer_details": None
    }

    with open(tracking_path, 'w', encoding='utf-8') as f:
        json.dump(tracking_data, f, indent=2, ensure_ascii=False)


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 3:
        print("Usage: python setup_company_folder.py <base_path> <company_name> [role_name]")
        print("\nExample:")
        print("  python setup_company_folder.py ~/InterviewIntel \"Google\" \"Senior Backend Engineer\"")
        sys.exit(1)

    base_path = sys.argv[1]
    company_name = sys.argv[2]
    role_name = sys.argv[3] if len(sys.argv) > 3 else None

    try:
        paths = create_company_folder(base_path, company_name, role_name)

        print(f"✅ Created company folder structure for: {company_name}")
        print(f"\n📁 Company Folder: {paths['company_folder']}")
        print(f"📁 Raw Data Folder: {paths['raw_data_folder']}")
        print(f"📁 Resumes Folder: {paths['resumes_folder']}")
        print(f"📁 Interviews Folder: {paths['interviews_folder']}")
        print("\n📄 Suggested file paths:")
        print(f"  - Company Intel: {paths['company_intel']}")
        print(f"  - Notes: {paths['notes']}")
        print(f"  - Interview Tracking: {paths['tracking']}")

        if role_name:
            print(f"\n📝 Role-specific files for '{role_name}':")
            print(f"  - JD Analysis: {paths['jd_analysis']}")
            print(f"  - Resume Mapping: {paths['resume_mapping']}")
            print(f"  - Interview Prep: {paths['interview_prep']}")
            print(f"  - JD Original: {paths['jd_original']}")
            print(f"  - JD Keywords: {paths['jd_keywords']}")

        # Create notes template if it doesn't exist
        notes_path = Path(paths['notes'])
        if not notes_path.exists():
            create_notes_template(notes_path, company_name)
            print(f"\n📝 Created notes template")

        # Output JSON for programmatic use
        import json
        print(f"\n--- JSON OUTPUT ---")
        print(json.dumps(paths, indent=2))

    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
