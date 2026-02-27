#!/usr/bin/env python3
"""
JD Keyword Extractor

Extracts key technical skills, requirements, and important phrases from job descriptions.
Helps quickly identify the most important aspects of a JD for interview preparation.
"""

import re
import sys
from collections import Counter
from typing import Dict, List, Set

# Common technical skills and technologies
TECH_KEYWORDS = {
    # Programming Languages
    'languages': ['Python', 'Java', 'JavaScript', 'TypeScript', 'Go', 'Rust', 'C\\+\\+', 'C#',
                  'Ruby', 'PHP', 'Swift', 'Kotlin', 'Scala', 'R', 'Julia'],

    # Frontend
    'frontend': ['React', 'Vue', 'Angular', 'Svelte', 'Next\\.js', 'Nuxt', 'HTML', 'CSS',
                 'Tailwind', 'Bootstrap', 'Webpack', 'Vite', 'Redux', 'MobX'],

    # Backend
    'backend': ['Node\\.js', 'Django', 'Flask', 'FastAPI', 'Spring', 'Express', 'Rails',
                'Laravel', '\\.NET', 'ASP\\.NET', 'GraphQL', 'REST', 'gRPC', 'API'],

    # Databases
    'databases': ['PostgreSQL', 'MySQL', 'MongoDB', 'Redis', 'Elasticsearch', 'DynamoDB',
                  'Cassandra', 'Oracle', 'SQL Server', 'Neo4j', 'ClickHouse'],

    # Cloud & Infrastructure
    'cloud': ['AWS', 'Azure', 'GCP', 'Google Cloud', 'Kubernetes', 'Docker', 'Terraform',
              'CloudFormation', 'Jenkins', 'GitLab CI', 'GitHub Actions', 'CircleCI'],

    # Data & ML
    'data_ml': ['Spark', 'Hadoop', 'Kafka', 'Airflow', 'TensorFlow', 'PyTorch', 'scikit-learn',
                'Pandas', 'NumPy', 'Jupyter', 'MLflow', 'Databricks'],

    # Tools & Practices
    'tools': ['Git', 'Linux', 'Bash', 'Agile', 'Scrum', 'CI/CD', 'Microservices',
              'REST API', 'OAuth', 'JWT', 'WebSocket']
}

# Experience indicators
EXPERIENCE_PATTERNS = [
    r'(\d+)\+?\s*years?',
    r'(\d+)\+?\s*yrs?',
    r'(senior|junior|mid-level|staff|principal|lead)',
]

# Soft skill indicators
SOFT_SKILLS = [
    'communication', 'leadership', 'collaboration', 'teamwork', 'problem-solving',
    'analytical', 'mentoring', 'ownership', 'autonomy', 'agile', 'cross-functional',
    'stakeholder', 'influence', 'documentation', 'presentation'
]

# Requirement strength indicators
STRONG_INDICATORS = ['required', 'must have', 'must-have', 'essential', 'critical']
PREFERRED_INDICATORS = ['preferred', 'nice to have', 'nice-to-have', 'bonus', 'plus']


def extract_tech_keywords(text: str) -> Dict[str, List[str]]:
    """Extract technical keywords by category."""
    found = {}
    text_lower = text.lower()

    for category, keywords in TECH_KEYWORDS.items():
        category_matches = []
        for keyword in keywords:
            pattern = re.compile(r'\b' + keyword + r'\b', re.IGNORECASE)
            matches = pattern.findall(text)
            if matches:
                # Use the actual match (preserves case) instead of the pattern
                category_matches.extend(set(matches))

        if category_matches:
            found[category] = sorted(set(category_matches))

    return found


def extract_experience_requirements(text: str) -> List[str]:
    """Extract experience level requirements."""
    requirements = []

    for pattern in EXPERIENCE_PATTERNS:
        matches = re.findall(pattern, text, re.IGNORECASE)
        requirements.extend(matches)

    return list(set(requirements))


def extract_soft_skills(text: str) -> List[str]:
    """Extract mentioned soft skills."""
    text_lower = text.lower()
    found = []

    for skill in SOFT_SKILLS:
        if skill in text_lower:
            found.append(skill)

    return found


def categorize_requirements(text: str) -> Dict[str, List[str]]:
    """Categorize requirements by strength (required vs preferred)."""
    result = {'required': [], 'preferred': []}

    # Split into sentences
    sentences = re.split(r'[.!?]\s+', text)

    for sentence in sentences:
        sentence_lower = sentence.lower()

        # Check if sentence contains strong requirement indicators
        is_required = any(indicator in sentence_lower for indicator in STRONG_INDICATORS)
        is_preferred = any(indicator in sentence_lower for indicator in PREFERRED_INDICATORS)

        if is_required:
            result['required'].append(sentence.strip())
        elif is_preferred:
            result['preferred'].append(sentence.strip())

    return result


def extract_key_phrases(text: str, top_n: int = 10) -> List[tuple]:
    """Extract most common meaningful phrases (2-3 words)."""
    # Remove common stop words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
                  'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'be', 'been'}

    # Extract 2-3 word phrases
    words = re.findall(r'\b[a-z]+\b', text.lower())

    bigrams = []
    trigrams = []

    for i in range(len(words) - 1):
        if words[i] not in stop_words or words[i+1] not in stop_words:
            bigrams.append(f"{words[i]} {words[i+1]}")

    for i in range(len(words) - 2):
        if not all(w in stop_words for w in [words[i], words[i+1], words[i+2]]):
            trigrams.append(f"{words[i]} {words[i+1]} {words[i+2]}")

    # Count frequencies
    phrase_counts = Counter(bigrams + trigrams)

    return phrase_counts.most_common(top_n)


def analyze_jd(jd_text: str) -> Dict:
    """Main analysis function."""
    return {
        'tech_keywords': extract_tech_keywords(jd_text),
        'experience_requirements': extract_experience_requirements(jd_text),
        'soft_skills': extract_soft_skills(jd_text),
        'categorized_requirements': categorize_requirements(jd_text),
        'key_phrases': extract_key_phrases(jd_text)
    }


def format_output(analysis: Dict) -> str:
    """Format analysis results as readable text."""
    output = []

    output.append("=" * 60)
    output.append("JD KEYWORD ANALYSIS")
    output.append("=" * 60)

    # Technical Keywords
    output.append("\n## TECHNICAL SKILLS\n")
    tech_keywords = analysis['tech_keywords']
    if tech_keywords:
        for category, keywords in tech_keywords.items():
            output.append(f"### {category.upper()}")
            for keyword in keywords:
                output.append(f"  - {keyword}")
            output.append("")
    else:
        output.append("  No specific technical keywords detected.\n")

    # Experience Requirements
    output.append("## EXPERIENCE REQUIREMENTS\n")
    exp_reqs = analysis['experience_requirements']
    if exp_reqs:
        for req in exp_reqs:
            output.append(f"  - {req}")
        output.append("")
    else:
        output.append("  No specific experience requirements detected.\n")

    # Soft Skills
    output.append("## SOFT SKILLS MENTIONED\n")
    soft_skills = analysis['soft_skills']
    if soft_skills:
        for skill in soft_skills:
            output.append(f"  - {skill}")
        output.append("")
    else:
        output.append("  No specific soft skills detected.\n")

    # Required vs Preferred
    output.append("## REQUIREMENT STRENGTH\n")
    categorized = analysis['categorized_requirements']

    if categorized['required']:
        output.append("### REQUIRED (Must-have)")
        for req in categorized['required'][:5]:  # Top 5
            output.append(f"  - {req}")
        output.append("")

    if categorized['preferred']:
        output.append("### PREFERRED (Nice-to-have)")
        for req in categorized['preferred'][:5]:  # Top 5
            output.append(f"  - {req}")
        output.append("")

    # Key Phrases
    output.append("## KEY PHRASES (Most Common)\n")
    key_phrases = analysis['key_phrases']
    if key_phrases:
        for phrase, count in key_phrases:
            output.append(f"  - '{phrase}' (mentioned {count}x)")
        output.append("")

    output.append("=" * 60)

    return "\n".join(output)


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        # Read from file
        file_path = sys.argv[1]
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                jd_text = f.read()
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.", file=sys.stderr)
            sys.exit(1)
    else:
        # Read from stdin
        print("Paste the job description (press Ctrl+D when done):")
        jd_text = sys.stdin.read()

    if not jd_text.strip():
        print("Error: No input provided.", file=sys.stderr)
        sys.exit(1)

    analysis = analyze_jd(jd_text)
    output = format_output(analysis)
    print(output)


if __name__ == "__main__":
    main()
