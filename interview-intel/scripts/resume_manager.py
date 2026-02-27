#!/usr/bin/env python3
"""
Resume Version Manager

Manages multiple resume versions with complete file storage and tracking.
Supports creating master versions, tailoring for specific companies, and analyzing usage.
"""

import os
import sys
import json
import shutil
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any


class ResumeManager:
    """Manages resume versions and their associated metadata."""

    def __init__(self, base_path: str):
        """
        Initialize the resume manager.

        Args:
            base_path: Base directory for InterviewIntel (contains resumes/ folder)
        """
        self.base_path = Path(base_path)
        self.resumes_path = self.base_path / "resumes"
        self.registry_path = self.resumes_path / "resume_registry.json"

        # Ensure resumes directory exists
        self.resumes_path.mkdir(parents=True, exist_ok=True)

        # Load or initialize registry
        self.registry = self._load_registry()

    def _load_registry(self) -> Dict[str, Any]:
        """Load the resume registry from disk."""
        if self.registry_path.exists():
            with open(self.registry_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return {
                "versions": [],
                "tailored_versions": []
            }

    def _save_registry(self):
        """Save the resume registry to disk."""
        with open(self.registry_path, 'w', encoding='utf-8') as f:
            json.dump(self.registry, f, indent=2, ensure_ascii=False)

    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA256 hash of a file."""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def _get_file_extension(self, file_path: Path) -> str:
        """Get file extension."""
        return file_path.suffix

    def create_version(
        self,
        file_path: str,
        version_id: str,
        description: str,
        target_positions: List[str],
        key_skills: List[str]
    ) -> Dict[str, Any]:
        """
        Create a new master resume version.

        Args:
            file_path: Path to the resume file
            version_id: Version identifier (e.g., "v1.0", "v2.0")
            description: Description of this version
            target_positions: Target position types
            key_skills: Key skills highlighted in this version

        Returns:
            Dictionary with version metadata
        """
        source_file = Path(file_path)

        if not source_file.exists():
            raise FileNotFoundError(f"Resume file not found: {file_path}")

        # Check if version already exists
        for version in self.registry["versions"]:
            if version["version_id"] == version_id:
                raise ValueError(f"Version {version_id} already exists")

        # Copy file to resumes directory
        file_ext = self._get_file_extension(source_file)
        dest_filename = f"master_resume_{version_id}{file_ext}"
        dest_path = self.resumes_path / dest_filename
        shutil.copy2(source_file, dest_path)

        # Calculate file hash
        file_hash = self._calculate_file_hash(dest_path)

        # Create version metadata
        version_data = {
            "version_id": version_id,
            "file": dest_filename,
            "file_path": str(dest_path),
            "file_hash": file_hash,
            "created_at": datetime.now().isoformat(),
            "description": description,
            "target_positions": target_positions,
            "key_skills": key_skills,
            "file_size_bytes": dest_path.stat().st_size
        }

        # Add change tracking if not first version
        if self.registry["versions"]:
            version_data["changes_from_previous"] = {
                "note": "Manual change tracking - describe changes here"
            }

        # Add to registry
        self.registry["versions"].append(version_data)
        self._save_registry()

        return version_data

    def list_versions(self, filter_target: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        List all master resume versions.

        Args:
            filter_target: Optional filter by target position

        Returns:
            List of version metadata dictionaries
        """
        versions = self.registry["versions"]

        if filter_target:
            versions = [
                v for v in versions
                if filter_target.lower() in [pos.lower() for pos in v.get("target_positions", [])]
            ]

        return versions

    def tailor_resume(
        self,
        base_version: str,
        company: str,
        role: str,
        output_dir: str,
        tailoring_notes: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create a company-specific tailored resume from a base version.

        Args:
            base_version: Base version ID to tailor from
            company: Company name
            role: Role name
            output_dir: Output directory (typically Company/resumes/)
            tailoring_notes: Optional notes about customizations

        Returns:
            Dictionary with tailored version metadata
        """
        # Find base version
        base = None
        for version in self.registry["versions"]:
            if version["version_id"] == base_version:
                base = version
                break

        if not base:
            raise ValueError(f"Base version {base_version} not found")

        # Create output directory
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Copy file
        base_file = Path(base["file_path"])
        file_ext = self._get_file_extension(base_file)

        # Sanitize role name for filename
        role_sanitized = role.replace(" ", "_").replace("/", "_")
        dest_filename = f"resume_{role_sanitized}_v1{file_ext}"
        dest_path = output_path / dest_filename

        # Check if file exists, increment version if needed
        counter = 1
        while dest_path.exists():
            counter += 1
            dest_filename = f"resume_{role_sanitized}_v{counter}{file_ext}"
            dest_path = output_path / dest_filename

        shutil.copy2(base_file, dest_path)

        # Create tailored version metadata
        tailored_data = {
            "base_version": base_version,
            "company": company,
            "role": role,
            "file": dest_filename,
            "file_path": str(dest_path),
            "created_at": datetime.now().isoformat(),
            "tailoring": tailoring_notes or {
                "emphasized": [],
                "added_keywords": [],
                "reordered_sections": False,
                "notes": "Add tailoring details here"
            }
        }

        # Add to registry
        self.registry["tailored_versions"].append(tailored_data)
        self._save_registry()

        return tailored_data

    def compare_versions(self, version1: str, version2: str) -> Dict[str, Any]:
        """
        Compare two resume versions.

        Args:
            version1: First version ID
            version2: Second version ID

        Returns:
            Dictionary with comparison data
        """
        v1 = None
        v2 = None

        for version in self.registry["versions"]:
            if version["version_id"] == version1:
                v1 = version
            if version["version_id"] == version2:
                v2 = version

        if not v1:
            raise ValueError(f"Version {version1} not found")
        if not v2:
            raise ValueError(f"Version {version2} not found")

        comparison = {
            "version1": v1["version_id"],
            "version2": v2["version_id"],
            "created_at_diff_days": (
                datetime.fromisoformat(v2["created_at"]) -
                datetime.fromisoformat(v1["created_at"])
            ).days,
            "target_positions": {
                "v1": v1.get("target_positions", []),
                "v2": v2.get("target_positions", []),
                "added": list(set(v2.get("target_positions", [])) - set(v1.get("target_positions", []))),
                "removed": list(set(v1.get("target_positions", [])) - set(v2.get("target_positions", [])))
            },
            "key_skills": {
                "v1": v1.get("key_skills", []),
                "v2": v2.get("key_skills", []),
                "added": list(set(v2.get("key_skills", [])) - set(v1.get("key_skills", []))),
                "removed": list(set(v1.get("key_skills", [])) - set(v2.get("key_skills", [])))
            },
            "descriptions": {
                "v1": v1.get("description", ""),
                "v2": v2.get("description", "")
            }
        }

        return comparison

    def recommend_version(self, target_position: str, key_requirements: List[str]) -> Dict[str, Any]:
        """
        Recommend best resume version for a position.

        Args:
            target_position: Target position type
            key_requirements: Key requirements from JD

        Returns:
            Dictionary with recommendation and match scores
        """
        recommendations = []

        for version in self.registry["versions"]:
            score = 0
            reasons = []

            # Check target positions match
            if target_position.lower() in [pos.lower() for pos in version.get("target_positions", [])]:
                score += 50
                reasons.append(f"Targets {target_position} position")

            # Check key skills overlap
            version_skills = [skill.lower() for skill in version.get("key_skills", [])]
            matched_skills = [req for req in key_requirements if req.lower() in version_skills]

            if matched_skills:
                skill_score = (len(matched_skills) / len(key_requirements)) * 50
                score += skill_score
                reasons.append(f"Matches {len(matched_skills)}/{len(key_requirements)} key requirements")

            recommendations.append({
                "version_id": version["version_id"],
                "score": score,
                "reasons": reasons,
                "description": version.get("description", "")
            })

        # Sort by score
        recommendations.sort(key=lambda x: x["score"], reverse=True)

        return {
            "recommended": recommendations[0] if recommendations else None,
            "all_scores": recommendations
        }

    def get_usage_report(self, version_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate usage report for resume versions.

        Args:
            version_id: Optional specific version to report on

        Returns:
            Dictionary with usage statistics
        """
        if version_id:
            # Report for specific version
            tailored = [
                t for t in self.registry["tailored_versions"]
                if t["base_version"] == version_id
            ]

            return {
                "version_id": version_id,
                "total_tailored": len(tailored),
                "companies": list(set(t["company"] for t in tailored)),
                "roles": [{"company": t["company"], "role": t["role"]} for t in tailored]
            }
        else:
            # Global report
            report = {
                "total_master_versions": len(self.registry["versions"]),
                "total_tailored_versions": len(self.registry["tailored_versions"]),
                "by_version": {}
            }

            for version in self.registry["versions"]:
                vid = version["version_id"]
                tailored = [
                    t for t in self.registry["tailored_versions"]
                    if t["base_version"] == vid
                ]
                report["by_version"][vid] = {
                    "tailored_count": len(tailored),
                    "companies": list(set(t["company"] for t in tailored))
                }

            return report


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        print("Resume Version Manager")
        print("\nUsage:")
        print("  python resume_manager.py create --file <path> --version <id> --desc <description> --target <positions> --skills <skills>")
        print("  python resume_manager.py list [--filter <target>]")
        print("  python resume_manager.py tailor --base <version> --company <name> --role <title> --output <dir>")
        print("  python resume_manager.py compare --v1 <version1> --v2 <version2>")
        print("  python resume_manager.py recommend --target <position> --requirements <req1,req2,...>")
        print("  python resume_manager.py report [--version <id>]")
        print("\nExamples:")
        print('  python resume_manager.py create --file ~/resume.pdf --version v1.0 --desc "General tech resume" --target "Backend,Full-stack" --skills "Python,React,AWS"')
        print('  python resume_manager.py list --filter Backend')
        print('  python resume_manager.py tailor --base v1.0 --company SIF --role "Backend Engineer" --output ~/InterviewIntel/SIF/resumes/')
        sys.exit(1)

    # Determine base path (current directory or specified)
    base_path = os.getcwd()

    # Initialize manager
    manager = ResumeManager(base_path)

    command = sys.argv[1]

    try:
        if command == "create":
            # Parse arguments
            args = {}
            i = 2
            while i < len(sys.argv):
                if sys.argv[i].startswith("--"):
                    key = sys.argv[i][2:]
                    if i + 1 < len(sys.argv):
                        args[key] = sys.argv[i + 1]
                        i += 2
                    else:
                        i += 1
                else:
                    i += 1

            result = manager.create_version(
                file_path=args["file"],
                version_id=args["version"],
                description=args["desc"],
                target_positions=args["target"].split(","),
                key_skills=args["skills"].split(",")
            )

            print(f"✅ Created resume version: {result['version_id']}")
            print(f"📄 File: {result['file']}")
            print(f"📝 Description: {result['description']}")
            print(f"🎯 Target positions: {', '.join(result['target_positions'])}")

        elif command == "list":
            filter_target = None
            if "--filter" in sys.argv:
                idx = sys.argv.index("--filter")
                if idx + 1 < len(sys.argv):
                    filter_target = sys.argv[idx + 1]

            versions = manager.list_versions(filter_target=filter_target)

            if not versions:
                print("No resume versions found.")
            else:
                print(f"\n📋 Resume Versions ({len(versions)} found):\n")
                for v in versions:
                    print(f"Version: {v['version_id']}")
                    print(f"  Description: {v['description']}")
                    print(f"  Target: {', '.join(v['target_positions'])}")
                    print(f"  Skills: {', '.join(v['key_skills'])}")
                    print(f"  Created: {v['created_at'][:10]}")
                    print(f"  File: {v['file']}")
                    print()

        elif command == "tailor":
            args = {}
            i = 2
            while i < len(sys.argv):
                if sys.argv[i].startswith("--"):
                    key = sys.argv[i][2:]
                    if i + 1 < len(sys.argv):
                        args[key] = sys.argv[i + 1]
                        i += 2
                    else:
                        i += 1
                else:
                    i += 1

            result = manager.tailor_resume(
                base_version=args["base"],
                company=args["company"],
                role=args["role"],
                output_dir=args["output"]
            )

            print(f"✅ Created tailored resume for {result['company']}")
            print(f"📄 Role: {result['role']}")
            print(f"📁 File: {result['file_path']}")
            print(f"🔗 Based on: {result['base_version']}")

        elif command == "compare":
            args = {}
            i = 2
            while i < len(sys.argv):
                if sys.argv[i].startswith("--"):
                    key = sys.argv[i][2:]
                    if i + 1 < len(sys.argv):
                        args[key] = sys.argv[i + 1]
                        i += 2
                    else:
                        i += 1
                else:
                    i += 1

            result = manager.compare_versions(args["v1"], args["v2"])

            print(f"\n📊 Comparison: {result['version1']} vs {result['version2']}\n")
            print(f"Time difference: {result['created_at_diff_days']} days")
            print(f"\nTarget Positions:")
            print(f"  Added: {', '.join(result['target_positions']['added']) or 'None'}")
            print(f"  Removed: {', '.join(result['target_positions']['removed']) or 'None'}")
            print(f"\nKey Skills:")
            print(f"  Added: {', '.join(result['key_skills']['added']) or 'None'}")
            print(f"  Removed: {', '.join(result['key_skills']['removed']) or 'None'}")

        elif command == "recommend":
            args = {}
            i = 2
            while i < len(sys.argv):
                if sys.argv[i].startswith("--"):
                    key = sys.argv[i][2:]
                    if i + 1 < len(sys.argv):
                        args[key] = sys.argv[i + 1]
                        i += 2
                    else:
                        i += 1
                else:
                    i += 1

            result = manager.recommend_version(
                target_position=args["target"],
                key_requirements=args["requirements"].split(",")
            )

            if result["recommended"]:
                rec = result["recommended"]
                print(f"\n🎯 Recommended Version: {rec['version_id']}")
                print(f"Score: {rec['score']:.1f}/100")
                print(f"Reasons:")
                for reason in rec['reasons']:
                    print(f"  - {reason}")
                print(f"\nDescription: {rec['description']}")

                print(f"\n📊 All Scores:")
                for item in result["all_scores"]:
                    print(f"  {item['version_id']}: {item['score']:.1f}/100")
            else:
                print("No versions available for recommendation.")

        elif command == "report":
            version_id = None
            if "--version" in sys.argv:
                idx = sys.argv.index("--version")
                if idx + 1 < len(sys.argv):
                    version_id = sys.argv[idx + 1]

            result = manager.get_usage_report(version_id)

            if version_id:
                print(f"\n📊 Usage Report for {result['version_id']}:\n")
                print(f"Total tailored versions: {result['total_tailored']}")
                print(f"Companies: {', '.join(result['companies']) or 'None'}")
                print(f"\nRoles:")
                for item in result['roles']:
                    print(f"  - {item['company']}: {item['role']}")
            else:
                print(f"\n📊 Global Usage Report:\n")
                print(f"Total master versions: {result['total_master_versions']}")
                print(f"Total tailored versions: {result['total_tailored_versions']}")
                print(f"\nBy Version:")
                for vid, data in result['by_version'].items():
                    print(f"  {vid}: {data['tailored_count']} tailored versions")
                    if data['companies']:
                        print(f"    Companies: {', '.join(data['companies'])}")

        else:
            print(f"Unknown command: {command}")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
