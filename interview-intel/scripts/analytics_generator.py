#!/usr/bin/env python3
"""
Analytics Generator

Generates statistics, reports, and visualizations for interview tracking data.
"""

import os
import sys
import json
import csv
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional


class AnalyticsGenerator:
    """Generates analytics from interview tracking data."""

    def __init__(self, base_path: str):
        """
        Initialize the analytics generator.

        Args:
            base_path: Base directory for InterviewIntel
        """
        self.base_path = Path(base_path)
        self.analytics_path = self.base_path / ".analytics"
        self.exports_path = self.analytics_path / "exports"

        # Ensure directories exist
        self.analytics_path.mkdir(exist_ok=True)
        self.exports_path.mkdir(exist_ok=True)

        # Load resume registry
        self.resume_registry_path = self.base_path / "resumes" / "resume_registry.json"
        self.resume_registry = self._load_resume_registry()

    def _load_resume_registry(self) -> Dict[str, Any]:
        """Load resume registry."""
        if self.resume_registry_path.exists():
            with open(self.resume_registry_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"versions": [], "tailored_versions": []}

    def _get_all_company_folders(self) -> List[Path]:
        """Get all company folders in the base path."""
        companies = []
        for item in self.base_path.iterdir():
            if item.is_dir() and not item.name.startswith('.') and item.name not in ['resumes', 'interview-intel']:
                # Check if it has an interviews folder
                if (item / "interviews").exists():
                    companies.append(item)
        return companies

    def _load_company_tracking(self, company_path: Path) -> Optional[Dict[str, Any]]:
        """Load tracking data for a company."""
        tracking_path = company_path / "interviews" / "tracking.json"
        if tracking_path.exists():
            with open(tracking_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None

    def generate_global_stats(self) -> Dict[str, Any]:
        """Generate global statistics across all companies."""
        companies = self._get_all_company_folders()

        stats = {
            "generated_at": datetime.now().isoformat(),
            "summary": {
                "total_companies_applied": len(companies),
                "total_applications": 0,
                "companies_with_response": 0,
                "response_rate": 0.0,
                "average_response_time_days": 0.0,
                "total_interviews_scheduled": 0,
                "total_interviews_completed": 0,
                "total_offers": 0,
                "offer_rate": 0.0,
                "active_processes": 0,
                "rejected": 0,
                "withdrawn": 0
            },
            "by_resume_version": {},
            "by_position_type": {},
            "timeline": {
                "first_application": None,
                "last_application": None,
                "duration_days": 0,
                "applications_per_week": 0
            },
            "interview_performance": {
                "total_interviews": 0,
                "passed": 0,
                "failed": 0,
                "pass_rate": 0.0,
                "average_difficulty": 0.0,
                "average_confidence": 0.0
            }
        }

        all_app_dates = []
        total_difficulty = 0
        total_confidence = 0
        difficulty_count = 0
        confidence_count = 0

        for company_path in companies:
            tracking = self._load_company_tracking(company_path)
            if not tracking:
                continue

            stats["summary"]["total_applications"] += 1

            # Application date tracking
            app_date = tracking["application"].get("application_date")
            if app_date:
                all_app_dates.append(app_date)

            # Response tracking
            if len(tracking.get("interviews", [])) > 0:
                stats["summary"]["companies_with_response"] += 1

            # Interview counts
            interviews = tracking.get("interviews", [])
            stats["summary"]["total_interviews_scheduled"] += len(interviews)
            completed = [i for i in interviews if i.get("status") == "completed"]
            stats["summary"]["total_interviews_completed"] += len(completed)

            # Difficulty and confidence
            for interview in completed:
                if interview.get("difficulty"):
                    total_difficulty += interview["difficulty"]
                    difficulty_count += 1
                if interview.get("confidence"):
                    total_confidence += interview["confidence"]
                    confidence_count += 1

            # Pass/fail tracking
            for interview in completed:
                result = interview.get("result")
                if result == "passed":
                    stats["interview_performance"]["passed"] += 1
                elif result == "failed":
                    stats["interview_performance"]["failed"] += 1

            # Decision tracking
            decision = tracking.get("decision")
            if decision == "offer":
                stats["summary"]["total_offers"] += 1
            elif decision == "rejected":
                stats["summary"]["rejected"] += 1
            elif decision in ["withdrew", "withdrawn"]:
                stats["summary"]["withdrawn"] += 1

            # Active processes
            if tracking.get("overall_status") not in ["offer", "rejected", "withdrew", "withdrawn"]:
                stats["summary"]["active_processes"] += 1

            # Resume version tracking
            resume_version = tracking["application"].get("resume_version_used", "unknown")
            if resume_version not in stats["by_resume_version"]:
                stats["by_resume_version"][resume_version] = {
                    "applications": 0,
                    "responses": 0,
                    "interviews": 0,
                    "offers": 0
                }
            stats["by_resume_version"][resume_version]["applications"] += 1
            if len(interviews) > 0:
                stats["by_resume_version"][resume_version]["responses"] += 1
                stats["by_resume_version"][resume_version]["interviews"] += len(interviews)
            if decision == "offer":
                stats["by_resume_version"][resume_version]["offers"] += 1

            # Position type tracking
            role = tracking["application"].get("role", "Unknown")
            if role not in stats["by_position_type"]:
                stats["by_position_type"][role] = {
                    "applications": 0,
                    "average_rounds": 0,
                    "success_rate": 0.0
                }
            stats["by_position_type"][role]["applications"] += 1

        # Calculate rates and averages
        if stats["summary"]["total_applications"] > 0:
            stats["summary"]["response_rate"] = (
                stats["summary"]["companies_with_response"] / stats["summary"]["total_applications"]
            )
            stats["summary"]["offer_rate"] = (
                stats["summary"]["total_offers"] / stats["summary"]["total_applications"]
            )

        total_completed_interviews = stats["summary"]["total_interviews_completed"]
        if total_completed_interviews > 0:
            stats["interview_performance"]["total_interviews"] = total_completed_interviews
            stats["interview_performance"]["pass_rate"] = (
                stats["interview_performance"]["passed"] / total_completed_interviews
            )

        if difficulty_count > 0:
            stats["interview_performance"]["average_difficulty"] = total_difficulty / difficulty_count
        if confidence_count > 0:
            stats["interview_performance"]["average_confidence"] = total_confidence / confidence_count

        # Timeline analysis
        if all_app_dates:
            all_app_dates.sort()
            stats["timeline"]["first_application"] = all_app_dates[0]
            stats["timeline"]["last_application"] = all_app_dates[-1]

            first = datetime.fromisoformat(all_app_dates[0])
            last = datetime.fromisoformat(all_app_dates[-1])
            duration = (last - first).days
            stats["timeline"]["duration_days"] = duration

            if duration > 0:
                stats["timeline"]["applications_per_week"] = (
                    len(all_app_dates) / (duration / 7)
                )

        # Save to file
        output_path = self.analytics_path / "global_stats.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)

        return stats

    def generate_company_stats(self, company_name: str) -> Dict[str, Any]:
        """Generate statistics for a specific company."""
        company_path = self.base_path / company_name
        tracking = self._load_company_tracking(company_path)

        if not tracking:
            return {"error": f"No tracking data found for {company_name}"}

        stats = {
            "company": tracking["application"]["company"],
            "role": tracking["application"]["role"],
            "application_date": tracking["application"]["application_date"],
            "resume_version": tracking["application"]["resume_version_used"],
            "overall_status": tracking["overall_status"],
            "total_rounds": len(tracking.get("interviews", [])),
            "completed_rounds": tracking.get("total_rounds_completed", 0),
            "pass_rate": tracking.get("pass_rate", 0.0),
            "decision": tracking.get("decision"),
            "timeline_events": len(tracking.get("timeline", [])),
            "interviews": []
        }

        for interview in tracking.get("interviews", []):
            stats["interviews"].append({
                "round": interview["round"],
                "name": interview["round_name"],
                "date": interview.get("date"),
                "status": interview.get("status"),
                "result": interview.get("result"),
                "difficulty": interview.get("difficulty"),
                "confidence": interview.get("confidence")
            })

        return stats

    def export_to_csv(self, output_file: str):
        """Export all interview data to CSV."""
        companies = self._get_all_company_folders()

        rows = []
        for company_path in companies:
            tracking = self._load_company_tracking(company_path)
            if not tracking:
                continue

            app = tracking["application"]
            base_row = {
                "company": app.get("company"),
                "role": app.get("role"),
                "application_date": app.get("application_date"),
                "application_method": app.get("application_method"),
                "resume_version": app.get("resume_version_used"),
                "overall_status": tracking.get("overall_status"),
                "decision": tracking.get("decision"),
                "total_rounds": len(tracking.get("interviews", [])),
                "completed_rounds": tracking.get("total_rounds_completed", 0),
                "pass_rate": tracking.get("pass_rate", 0.0)
            }

            # Add row for each interview round
            for interview in tracking.get("interviews", []):
                row = base_row.copy()
                row.update({
                    "round_number": interview["round"],
                    "round_name": interview["round_name"],
                    "interview_date": interview.get("date"),
                    "interview_status": interview.get("status"),
                    "interview_result": interview.get("result"),
                    "difficulty": interview.get("difficulty"),
                    "confidence": interview.get("confidence"),
                    "interviewer": interview.get("interviewer", {}).get("name")
                })
                rows.append(row)

            # If no interviews, add one row with company info
            if not tracking.get("interviews"):
                rows.append(base_row)

        # Write to CSV
        if rows:
            output_path = self.exports_path / output_file
            fieldnames = rows[0].keys()

            with open(output_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

            print(f"✅ Exported to {output_path}")
        else:
            print("⚠️  No data to export")

    def generate_html_dashboard(self, output_file: str):
        """Generate HTML dashboard with visualizations."""
        stats = self.generate_global_stats()

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interview Intel Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: #f5f7fa;
            padding: 20px;
            color: #333;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        header {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}
        h1 {{
            font-size: 32px;
            color: #2c3e50;
            margin-bottom: 10px;
        }}
        .subtitle {{
            color: #7f8c8d;
            font-size: 14px;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        .stat-label {{
            font-size: 14px;
            color: #7f8c8d;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 10px;
        }}
        .stat-value {{
            font-size: 36px;
            font-weight: bold;
            color: #2c3e50;
        }}
        .stat-value.success {{
            color: #27ae60;
        }}
        .stat-value.warning {{
            color: #f39c12;
        }}
        .stat-value.info {{
            color: #3498db;
        }}
        .charts-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .chart-card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        .chart-title {{
            font-size: 18px;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 20px;
        }}
        canvas {{
            max-height: 300px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📊 Interview Intel Dashboard</h1>
            <p class="subtitle">Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        </header>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-label">Total Applications</div>
                <div class="stat-value info">{stats["summary"]["total_applications"]}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Response Rate</div>
                <div class="stat-value">{stats["summary"]["response_rate"]:.1%}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Total Interviews</div>
                <div class="stat-value">{stats["summary"]["total_interviews_completed"]}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Interview Pass Rate</div>
                <div class="stat-value success">{stats["interview_performance"]["pass_rate"]:.1%}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Offers Received</div>
                <div class="stat-value success">{stats["summary"]["total_offers"]}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Offer Rate</div>
                <div class="stat-value success">{stats["summary"]["offer_rate"]:.1%}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Active Processes</div>
                <div class="stat-value warning">{stats["summary"]["active_processes"]}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Avg Difficulty</div>
                <div class="stat-value">{stats["interview_performance"]["average_difficulty"]:.1f}/5</div>
            </div>
        </div>

        <div class="charts-grid">
            <div class="chart-card">
                <h3 class="chart-title">Applications by Status</h3>
                <canvas id="statusChart"></canvas>
            </div>
            <div class="chart-card">
                <h3 class="chart-title">Resume Version Performance</h3>
                <canvas id="resumeChart"></canvas>
            </div>
            <div class="chart-card">
                <h3 class="chart-title">Interview Pass Rate</h3>
                <canvas id="passRateChart"></canvas>
            </div>
            <div class="chart-card">
                <h3 class="chart-title">Applications by Position Type</h3>
                <canvas id="positionChart"></canvas>
            </div>
        </div>
    </div>

    <script>
        // Status Chart
        new Chart(document.getElementById('statusChart'), {{
            type: 'doughnut',
            data: {{
                labels: ['Active', 'Offers', 'Rejected', 'Withdrawn'],
                datasets: [{{
                    data: [
                        {stats["summary"]["active_processes"]},
                        {stats["summary"]["total_offers"]},
                        {stats["summary"]["rejected"]},
                        {stats["summary"]["withdrawn"]}
                    ],
                    backgroundColor: ['#f39c12', '#27ae60', '#e74c3c', '#95a5a6']
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: true
            }}
        }});

        // Resume Version Chart
        new Chart(document.getElementById('resumeChart'), {{
            type: 'bar',
            data: {{
                labels: {json.dumps(list(stats["by_resume_version"].keys()))},
                datasets: [{{
                    label: 'Applications',
                    data: {json.dumps([v["applications"] for v in stats["by_resume_version"].values()])},
                    backgroundColor: '#3498db'
                }}, {{
                    label: 'Interviews',
                    data: {json.dumps([v["interviews"] for v in stats["by_resume_version"].values()])},
                    backgroundColor: '#9b59b6'
                }}, {{
                    label: 'Offers',
                    data: {json.dumps([v["offers"] for v in stats["by_resume_version"].values()])},
                    backgroundColor: '#27ae60'
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: true,
                scales: {{
                    y: {{
                        beginAtZero: true
                    }}
                }}
            }}
        }});

        // Pass Rate Chart
        new Chart(document.getElementById('passRateChart'), {{
            type: 'pie',
            data: {{
                labels: ['Passed', 'Failed'],
                datasets: [{{
                    data: [
                        {stats["interview_performance"]["passed"]},
                        {stats["interview_performance"]["failed"]}
                    ],
                    backgroundColor: ['#27ae60', '#e74c3c']
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: true
            }}
        }});

        // Position Type Chart
        new Chart(document.getElementById('positionChart'), {{
            type: 'bar',
            data: {{
                labels: {json.dumps(list(stats["by_position_type"].keys()))},
                datasets: [{{
                    label: 'Applications',
                    data: {json.dumps([v["applications"] for v in stats["by_position_type"].values()])},
                    backgroundColor: '#3498db'
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: true,
                indexAxis: 'y',
                scales: {{
                    x: {{
                        beginAtZero: true
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>"""

        output_path = self.exports_path / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"✅ Generated dashboard: {output_path}")
        print(f"💡 Open in browser: file://{output_path.absolute()}")

        return output_path


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        print("Analytics Generator")
        print("\nUsage:")
        print("  python analytics_generator.py generate [--scope global|company] [--company <name>]")
        print("  python analytics_generator.py export --format csv --output <filename>")
        print("  python analytics_generator.py dashboard --output <filename.html>")
        print("\nExamples:")
        print('  python analytics_generator.py generate --scope global')
        print('  python analytics_generator.py generate --scope company --company SIF')
        print('  python analytics_generator.py export --format csv --output interview_data.csv')
        print('  python analytics_generator.py dashboard --output dashboard.html')
        sys.exit(1)

    # Determine base path
    base_path = os.getcwd()

    # Initialize generator
    generator = AnalyticsGenerator(base_path)

    command = sys.argv[1]

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

    try:
        if command == "generate":
            scope = args.get("scope", "global")

            if scope == "global":
                stats = generator.generate_global_stats()
                print("\n📊 Global Statistics Generated\n")
                print(f"Total Applications: {stats['summary']['total_applications']}")
                print(f"Response Rate: {stats['summary']['response_rate']:.1%}")
                print(f"Interview Pass Rate: {stats['interview_performance']['pass_rate']:.1%}")
                print(f"Offers: {stats['summary']['total_offers']}")
                print(f"\n✅ Saved to .analytics/global_stats.json")

            elif scope == "company":
                company = args.get("company")
                if not company:
                    print("Error: --company required for company scope")
                    sys.exit(1)

                stats = generator.generate_company_stats(company)
                if "error" in stats:
                    print(f"❌ {stats['error']}")
                else:
                    print(f"\n📊 Statistics for {stats['company']}\n")
                    print(f"Role: {stats['role']}")
                    print(f"Status: {stats['overall_status']}")
                    print(f"Total Rounds: {stats['total_rounds']}")
                    print(f"Pass Rate: {stats['pass_rate']:.1%}")
                    print(json.dumps(stats, indent=2))

        elif command == "export":
            format_type = args.get("format", "csv")
            output = args.get("output", "interview_data.csv")

            if format_type == "csv":
                generator.export_to_csv(output)

        elif command == "dashboard":
            output = args.get("output", "dashboard.html")
            generator.generate_html_dashboard(output)

        else:
            print(f"Unknown command: {command}")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
