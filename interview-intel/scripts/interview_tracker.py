#!/usr/bin/env python3
"""
Interview Tracker

Manages structured interview tracking with round-by-round details and timeline.
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any


class InterviewTracker:
    """Manages interview tracking data for a company."""

    def __init__(self, company_path: str):
        """
        Initialize the interview tracker.

        Args:
            company_path: Path to company folder
        """
        self.company_path = Path(company_path)
        self.interviews_path = self.company_path / "interviews"
        self.tracking_path = self.interviews_path / "tracking.json"

        # Ensure interviews directory exists
        self.interviews_path.mkdir(parents=True, exist_ok=True)

        # Load tracking data
        self.tracking = self._load_tracking()

    def _load_tracking(self) -> Dict[str, Any]:
        """Load tracking data from disk."""
        if self.tracking_path.exists():
            with open(self.tracking_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return None

    def _save_tracking(self):
        """Save tracking data to disk."""
        with open(self.tracking_path, 'w', encoding='utf-8') as f:
            json.dump(self.tracking, f, indent=2, ensure_ascii=False)

    def init_tracking(
        self,
        company: str,
        role: str,
        resume_version: str,
        jd_file: str = "",
        application_method: str = "",
        application_date: str = None
    ) -> Dict[str, Any]:
        """
        Initialize interview tracking for a company/role.

        Args:
            company: Company name
            role: Role title
            resume_version: Resume version used for application
            jd_file: Path to JD file
            application_method: How the application was submitted
            application_date: Date of application (defaults to today)

        Returns:
            Dictionary with tracking data
        """
        if self.tracking:
            raise ValueError("Tracking already initialized. Use update commands instead.")

        app_date = application_date or datetime.now().strftime("%Y-%m-%d")

        self.tracking = {
            "application": {
                "company": company,
                "role": role,
                "application_date": app_date,
                "application_method": application_method,
                "referral": None,
                "resume_version_used": resume_version,
                "cover_letter": False,
                "jd_file": jd_file
            },
            "timeline": [
                {
                    "date": app_date,
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

        self._save_tracking()
        return self.tracking

    def add_timeline_event(self, date: str, event: str, status: str):
        """Add an event to the timeline."""
        if not self.tracking:
            raise ValueError("Tracking not initialized. Run 'init' first.")

        self.tracking["timeline"].append({
            "date": date,
            "event": event,
            "status": status
        })
        self._save_tracking()

    def add_interview_round(
        self,
        round_num: int,
        round_name: str,
        date: str,
        time: str = "",
        duration_minutes: int = 0,
        format: str = "video",
        platform: str = "",
        interviewer_name: str = "",
        interviewer_title: str = "",
        focus_areas: List[str] = None
    ) -> Dict[str, Any]:
        """
        Add a new interview round.

        Args:
            round_num: Round number
            round_name: Name of the round (e.g., "Phone Screen", "Technical")
            date: Interview date
            time: Interview time
            duration_minutes: Expected duration
            format: Interview format (video, phone, in-person)
            platform: Platform (Zoom, Teams, etc.)
            interviewer_name: Interviewer's name
            interviewer_title: Interviewer's title
            focus_areas: List of focus areas

        Returns:
            Dictionary with round data
        """
        if not self.tracking:
            raise ValueError("Tracking not initialized. Run 'init' first.")

        round_data = {
            "round": round_num,
            "round_name": round_name,
            "date": date,
            "time": time,
            "duration_minutes": duration_minutes,
            "format": format,
            "platform": platform,
            "interviewer": {
                "name": interviewer_name,
                "title": interviewer_title,
                "linkedin": "",
                "email": ""
            },
            "focus_areas": focus_areas or [],
            "status": "scheduled",
            "result": None,
            "difficulty": 0,
            "confidence": 0,
            "feedback": {
                "positive": [],
                "areas_to_improve": [],
                "questions_asked": 0,
                "questions_answered_well": 0
            },
            "notes_file": f"interviews/round_{round_num}_notes.md",
            "follow_up": {
                "thank_you_sent": False,
                "thank_you_date": None,
                "connections_made": []
            }
        }

        self.tracking["interviews"].append(round_data)
        self._save_tracking()

        # Add to timeline
        self.add_timeline_event(date, f"Round {round_num}: {round_name} scheduled", "scheduled")

        return round_data

    def update_round(
        self,
        round_num: int,
        status: str = None,
        result: str = None,
        difficulty: int = None,
        confidence: int = None,
        positive_feedback: List[str] = None,
        improvement_areas: List[str] = None,
        questions_asked: int = None,
        questions_answered_well: int = None
    ):
        """
        Update an interview round with results and feedback.

        Args:
            round_num: Round number to update
            status: Round status (scheduled, completed, cancelled)
            result: Round result (passed, failed, pending)
            difficulty: Difficulty rating (1-5)
            confidence: Confidence rating (1-5)
            positive_feedback: List of positive feedback points
            improvement_areas: List of areas to improve
            questions_asked: Number of questions asked
            questions_answered_well: Number of questions answered well
        """
        if not self.tracking:
            raise ValueError("Tracking not initialized. Run 'init' first.")

        # Find the round
        round_data = None
        for interview in self.tracking["interviews"]:
            if interview["round"] == round_num:
                round_data = interview
                break

        if not round_data:
            raise ValueError(f"Round {round_num} not found")

        # Update fields
        if status:
            round_data["status"] = status
        if result:
            round_data["result"] = result
        if difficulty is not None:
            round_data["difficulty"] = difficulty
        if confidence is not None:
            round_data["confidence"] = confidence

        # Update feedback
        if positive_feedback:
            round_data["feedback"]["positive"] = positive_feedback
        if improvement_areas:
            round_data["feedback"]["areas_to_improve"] = improvement_areas
        if questions_asked is not None:
            round_data["feedback"]["questions_asked"] = questions_asked
        if questions_answered_well is not None:
            round_data["feedback"]["questions_answered_well"] = questions_answered_well

        # Update overall statistics
        if status == "completed":
            self.tracking["total_rounds_completed"] = sum(
                1 for i in self.tracking["interviews"] if i["status"] == "completed"
            )

            passed_rounds = sum(
                1 for i in self.tracking["interviews"]
                if i["status"] == "completed" and i["result"] == "passed"
            )

            if self.tracking["total_rounds_completed"] > 0:
                self.tracking["pass_rate"] = passed_rounds / self.tracking["total_rounds_completed"]

        self._save_tracking()

        # Add to timeline
        if status == "completed" and result:
            self.add_timeline_event(
                datetime.now().strftime("%Y-%m-%d"),
                f"Round {round_num} completed - {result}",
                result
            )

    def update_follow_up(self, round_num: int, thank_you_sent: bool, thank_you_date: str = None, connections: List[str] = None):
        """Update follow-up actions for a round."""
        if not self.tracking:
            raise ValueError("Tracking not initialized. Run 'init' first.")

        for interview in self.tracking["interviews"]:
            if interview["round"] == round_num:
                interview["follow_up"]["thank_you_sent"] = thank_you_sent
                if thank_you_date:
                    interview["follow_up"]["thank_you_date"] = thank_you_date
                if connections:
                    interview["follow_up"]["connections_made"] = connections
                break

        self._save_tracking()

    def update_decision(self, decision: str, decision_date: str = None, offer_details: Dict[str, Any] = None):
        """
        Update final decision.

        Args:
            decision: Decision (offer, rejected, withdrew)
            decision_date: Date of decision
            offer_details: Details if offer received
        """
        if not self.tracking:
            raise ValueError("Tracking not initialized. Run 'init' first.")

        self.tracking["decision"] = decision
        self.tracking["decision_date"] = decision_date or datetime.now().strftime("%Y-%m-%d")
        self.tracking["overall_status"] = decision

        if offer_details:
            self.tracking["offer_details"] = offer_details

        self._save_tracking()

        # Add to timeline
        self.add_timeline_event(
            self.tracking["decision_date"],
            f"Decision: {decision}",
            decision
        )

    def get_status(self) -> Dict[str, Any]:
        """Get current status summary."""
        if not self.tracking:
            return {"error": "No tracking data found"}

        return {
            "company": self.tracking["application"]["company"],
            "role": self.tracking["application"]["role"],
            "overall_status": self.tracking["overall_status"],
            "current_stage": self.tracking["current_stage"],
            "total_rounds": len(self.tracking["interviews"]),
            "rounds_completed": self.tracking["total_rounds_completed"],
            "pass_rate": self.tracking["pass_rate"],
            "decision": self.tracking["decision"]
        }

    def generate_timeline(self, format: str = "text") -> str:
        """
        Generate timeline visualization.

        Args:
            format: Output format (text, json)

        Returns:
            Formatted timeline string
        """
        if not self.tracking:
            return "No tracking data found"

        if format == "json":
            return json.dumps(self.tracking["timeline"], indent=2)

        # Text format
        output = []
        output.append(f"\n📅 Interview Timeline - {self.tracking['application']['company']}\n")
        output.append("=" * 60)

        for event in self.tracking["timeline"]:
            status_icon = {
                "submitted": "📤",
                "scheduled": "📆",
                "completed": "✅",
                "passed": "✅",
                "failed": "❌",
                "offer": "🎉",
                "rejected": "❌"
            }.get(event["status"], "📌")

            output.append(f"\n{status_icon} {event['date']} - {event['event']}")

        output.append("\n" + "=" * 60)
        output.append(f"\nCurrent Status: {self.tracking['overall_status'].upper()}")

        return "\n".join(output)


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        print("Interview Tracker")
        print("\nUsage:")
        print("  python interview_tracker.py init --company <name> --role <title> --resume <version>")
        print("  python interview_tracker.py add-round --company-path <path> --round <num> --name <name> --date <date>")
        print("  python interview_tracker.py update --company-path <path> --round <num> --status <status> --result <result>")
        print("  python interview_tracker.py status --company-path <path>")
        print("  python interview_tracker.py timeline --company-path <path> [--format text|json]")
        print("\nExamples:")
        print('  python interview_tracker.py init --company-path ~/InterviewIntel/SIF --company SIF --role "Backend Engineer" --resume v2.0')
        print('  python interview_tracker.py add-round --company-path ~/InterviewIntel/SIF --round 1 --name "Phone Screen" --date 2026-01-25')
        print('  python interview_tracker.py update --company-path ~/InterviewIntel/SIF --round 1 --status completed --result passed')
        sys.exit(1)

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
        if command == "init":
            company_path = args.get("company-path", os.getcwd())
            tracker = InterviewTracker(company_path)

            result = tracker.init_tracking(
                company=args["company"],
                role=args["role"],
                resume_version=args["resume"],
                jd_file=args.get("jd", ""),
                application_method=args.get("method", "")
            )

            print(f"✅ Initialized tracking for {result['application']['company']}")
            print(f"📝 Role: {result['application']['role']}")
            print(f"📄 Resume version: {result['application']['resume_version_used']}")
            print(f"📅 Application date: {result['application']['application_date']}")

        elif command == "add-round":
            company_path = args["company-path"]
            tracker = InterviewTracker(company_path)

            result = tracker.add_interview_round(
                round_num=int(args["round"]),
                round_name=args["name"],
                date=args["date"],
                time=args.get("time", ""),
                duration_minutes=int(args.get("duration", 0)),
                format=args.get("format", "video"),
                platform=args.get("platform", ""),
                interviewer_name=args.get("interviewer", ""),
                interviewer_title=args.get("title", ""),
                focus_areas=args.get("focus", "").split(",") if args.get("focus") else []
            )

            print(f"✅ Added Round {result['round']}: {result['round_name']}")
            print(f"📅 Date: {result['date']}")
            print(f"💻 Format: {result['format']}")

        elif command == "update":
            company_path = args["company-path"]
            tracker = InterviewTracker(company_path)

            tracker.update_round(
                round_num=int(args["round"]),
                status=args.get("status"),
                result=args.get("result"),
                difficulty=int(args["difficulty"]) if "difficulty" in args else None,
                confidence=int(args["confidence"]) if "confidence" in args else None,
                positive_feedback=args.get("positive", "").split(",") if args.get("positive") else None,
                improvement_areas=args.get("improve", "").split(",") if args.get("improve") else None
            )

            print(f"✅ Updated Round {args['round']}")
            if "result" in args:
                print(f"Result: {args['result']}")

        elif command == "status":
            company_path = args["company-path"]
            tracker = InterviewTracker(company_path)

            status = tracker.get_status()

            print(f"\n📊 Status for {status['company']} - {status['role']}\n")
            print(f"Overall Status: {status['overall_status'].upper()}")
            print(f"Current Stage: {status['current_stage']}")
            print(f"Total Rounds: {status['total_rounds']}")
            print(f"Completed: {status['rounds_completed']}")
            print(f"Pass Rate: {status['pass_rate']:.0%}")
            if status['decision']:
                print(f"Decision: {status['decision'].upper()}")

        elif command == "timeline":
            company_path = args["company-path"]
            tracker = InterviewTracker(company_path)

            format = args.get("format", "text")
            timeline = tracker.generate_timeline(format)
            print(timeline)

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
