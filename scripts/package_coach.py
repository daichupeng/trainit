#!/usr/bin/env python3
"""Package reusable coach files only; never discover files recursively."""

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_FILES = (
    "README.md",
    ".gitignore",
    "AGENTS.md",
    "initiation.md",
    "capability_assessment_methodology.md",
    "templates/profile.md",
    "templates/current_status.md",
    "templates/training_log.md",
    "templates/training_plan.md",
    "fitness-site/README.md",
    "scripts/capability_sensitivity.py",
    "scripts/package_coach.py",
)


def package(output, force=False):
    output = Path(output).resolve()
    # Resolve and validate every allowlisted source before creating output.
    sources = []
    for relative in PACKAGE_FILES:
        source = ROOT / relative
        if source.is_symlink() or source.resolve() != source.absolute():
            raise ValueError(f"Refusing linked package source: {relative}")
        if not source.is_file():
            raise ValueError(f"Missing reusable source: {relative}")
        sources.append((source, f"ai-training-coach/{relative}"))
    if output == ROOT or ROOT in output.parents and output.parts[len(ROOT.parts)] in {
        "archives", "sources", "training-reference", "templates"
    }:
        raise ValueError("Output must not replace archives, references, or templates.")
    if output.suffix.lower() != ".zip":
        raise ValueError("Output must have a .zip extension.")
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w" if force else "x", ZIP_DEFLATED) as bundle:
        for source, destination in sources:
            bundle.write(source, destination)
    with ZipFile(output) as bundle:
        if sorted(bundle.namelist()) != sorted(name for _, name in sources):
            raise ValueError("Unexpected package contents.")
        if bundle.testzip() is not None:
            raise ValueError("Package integrity check failed.")
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("outputs/ai-training-coach.zip"))
    parser.add_argument("--force", action="store_true", help="Replace an existing ZIP.")
    args = parser.parse_args()
    try:
        result = package(args.output, args.force)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Package not created: {exc}\n")
    print(f"Created {result} ({len(PACKAGE_FILES)} reusable files; no personal records).")


if __name__ == "__main__":
    main()
