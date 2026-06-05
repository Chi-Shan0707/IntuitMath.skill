#!/usr/bin/env python3
"""
IntuitMath Problem Library Saver

Usage (from an agent or command line):
    python scripts/save-problem.py \
        --question "Why does the Fourier transform work?" \
        --summary "Fourier transform decomposes functions into frequency components..." \
        --tags "fourier-analysis,pde,physics" \
        --cross-domain "Signal processing, Quantum mechanics, Probability (characteristic functions)" \
        --reflection "Is frequency decomposition 'natural' or a mathematical artifact?" \
        [--problem-dir /path/to/problem-library]

If --problem-dir is omitted, uses ../problem-library/ relative to this script.
If --question is omitted, reads from stdin (for piping).
"""

import argparse
import datetime
import os
import re
import sys


def slugify(text: str, max_len: int = 60) -> str:
    """Convert text to a filesystem-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text)
    return text[:max_len].rstrip("-")


def update_index(problem_dir: str, date: str, topic: str, tags: str):
    """Append entry to the problem library index."""
    index_path = os.path.join(problem_dir, "index.md")
    if not os.path.exists(index_path):
        print(f"Warning: {index_path} not found, skipping index update.", file=sys.stderr)
        return

    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if "(no records yet)" placeholder exists
    if "(no records yet)" in content:
        content = content.replace(
            "| (no records yet) | — | — |",
            f"| {date} | {topic} | {tags} |",
        )
    else:
        # Append after the last table row (before the --- separator)
        marker = "\n---\n"
        if marker in content:
            parts = content.split(marker)
            # Add row to the table in the first part
            table_end = parts[0].rstrip()
            parts[0] = table_end + f"\n| {date} | {topic} | {tags} |\n"
            content = marker.join(parts)
        else:
            # Fallback: just append
            content += f"\n| {date} | {topic} | {tags} |\n"

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    parser = argparse.ArgumentParser(description="Save a problem to IntuitMath problem library")
    parser.add_argument("--question", "-q", help="The user's original question")
    parser.add_argument("--summary", "-s", required=True, help="3-5 sentence answer summary")
    parser.add_argument("--tags", "-t", default="", help="Comma-separated concept tags")
    parser.add_argument("--cross-domain", "-c", default="", help="Cross-domain connections")
    parser.add_argument("--reflection", "-r", default="", help="Reflection anchor")
    parser.add_argument("--topic", help="Short topic name (auto-derived from question if omitted)")
    parser.add_argument("--problem-dir", "-d", help="Path to problem-library/ directory")

    args = parser.parse_args()

    # Read question from stdin if not provided
    question = args.question
    if not question:
        if not sys.stdin.isatty():
            question = sys.stdin.read().strip()
        if not question:
            print("Error: --question is required (or pipe via stdin)", file=sys.stderr)
            sys.exit(1)

    # Determine problem directory
    if args.problem_dir:
        problem_dir = os.path.abspath(args.problem_dir)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        problem_dir = os.path.join(script_dir, "..", "problem-library")

    if not os.path.isdir(problem_dir):
        print(f"Error: problem-library not found at {problem_dir}", file=sys.stderr)
        sys.exit(1)

    # Generate filename
    today = datetime.date.today().isoformat()
    topic = args.topic or slugify(question)
    filename = f"{today}-{topic}.md"
    filepath = os.path.join(problem_dir, filename)

    # Build content
    tags_section = args.tags
    cross_domain_section = args.cross_domain or "None identified"
    reflection_section = args.reflection or "No reflection anchor recorded"

    record = f"""# {topic}

- **Date**: {today}
- **Tags**: {tags_section}

## Question

{question}

## Summary

{args.summary}

## Cross-Domain Connections

{cross_domain_section}

## Reflection

{reflection_section}
"""

    # Write file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(record)

    print(f"Saved: {filepath}")

    # Update index
    display_tags = ", ".join(t.strip() for t in args.tags.split(",") if t.strip()) if args.tags else "—"
    update_index(problem_dir, today, topic, display_tags)
    print(f"Index updated: {os.path.join(problem_dir, 'index.md')}")


if __name__ == "__main__":
    main()
