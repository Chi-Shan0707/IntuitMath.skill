#!/usr/bin/env python3
"""
Render an IntuitMath single-file HTML note from section files.

The script intentionally has no third-party dependencies. Section files may
contain either simple Markdown or raw HTML. By default it converts common
Markdown blocks to HTML while preserving KaTeX delimiters.
"""

import argparse
import datetime as dt
import html
import re
from pathlib import Path


PLACEHOLDERS = {
    "MOTIVATION",
    "INTUITIVE_DERIVATION",
    "RIGOROUS_VERSION",
    "MULTI_PERSPECTIVE",
    "CROSS_DOMAIN",
    "REFLECTION",
}


def inline_markdown(text: str) -> str:
    escaped = html.escape(text, quote=False)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    return escaped


def is_math_block_start(line: str) -> bool:
    stripped = line.strip()
    return (
        stripped.startswith("$$")
        or stripped.startswith(r"\[")
        or stripped.startswith(r"\begin{")
    )


def math_block_end_token(line: str) -> str:
    stripped = line.strip()
    if stripped.startswith("$$"):
        return "$$"
    if stripped.startswith(r"\["):
        return r"\]"
    match = re.match(r"\\begin\{([^}]+)\}", stripped)
    if match:
        return rf"\end{{{match.group(1)}}}"
    return ""


def markdown_table_to_html(rows: list[str]) -> str:
    split_rows = [
        [cell.strip() for cell in row.strip().strip("|").split("|")]
        for row in rows
    ]
    header = split_rows[0]
    body = split_rows[2:] if len(split_rows) > 2 else []
    head_html = "".join(f"<th>{inline_markdown(cell)}</th>" for cell in header)
    body_html = []
    for row in body:
        cells = "".join(f"<td>{inline_markdown(cell)}</td>" for cell in row)
        body_html.append(f"<tr>{cells}</tr>")
    return (
        "<table>\n<thead><tr>"
        + head_html
        + "</tr></thead>\n<tbody>\n"
        + "\n".join(body_html)
        + "\n</tbody>\n</table>"
    )


def markdown_to_html(markdown: str) -> str:
    blocks = []
    lines = markdown.strip().splitlines()
    index = 0
    while index < len(lines):
        line = lines[index].rstrip()
        if not line:
            index += 1
            continue
        if line.lstrip().startswith("<"):
            raw = [line]
            index += 1
            while index < len(lines) and lines[index].strip():
                raw.append(lines[index].rstrip())
                index += 1
            blocks.append("\n".join(raw))
            continue
        if line.startswith("```"):
            fence_lang = line[3:].strip()
            code = []
            index += 1
            while index < len(lines) and not lines[index].startswith("```"):
                code.append(lines[index])
                index += 1
            if index < len(lines):
                index += 1
            class_attr = f' class="language-{html.escape(fence_lang)}"' if fence_lang else ""
            blocks.append(f"<pre><code{class_attr}>{html.escape(chr(10).join(code))}</code></pre>")
            continue
        if is_math_block_start(line):
            end_token = math_block_end_token(line)
            math_lines = [line]
            index += 1
            while index < len(lines):
                math_lines.append(lines[index].rstrip())
                if end_token and lines[index].strip().endswith(end_token):
                    index += 1
                    break
                index += 1
            blocks.append("\n".join(math_lines))
            continue
        if (
            line.startswith("|")
            and index + 1 < len(lines)
            and re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", lines[index + 1])
        ):
            table = [line, lines[index + 1].rstrip()]
            index += 2
            while index < len(lines) and lines[index].startswith("|"):
                table.append(lines[index].rstrip())
                index += 1
            blocks.append(markdown_table_to_html(table))
            continue
        if line.startswith("### "):
            blocks.append(f"<h3>{inline_markdown(line[4:].strip())}</h3>")
            index += 1
            continue
        if line.startswith("## "):
            blocks.append(f"<h2>{inline_markdown(line[3:].strip())}</h2>")
            index += 1
            continue
        if line.startswith("# "):
            blocks.append(f"<h2>{inline_markdown(line[2:].strip())}</h2>")
            index += 1
            continue
        if line.startswith(("- ", "* ")):
            items = []
            while index < len(lines) and lines[index].startswith(("- ", "* ")):
                items.append(f"<li>{inline_markdown(lines[index][2:].strip())}</li>")
                index += 1
            blocks.append("<ul>\n" + "\n".join(items) + "\n</ul>")
            continue
        if re.match(r"^\d+\. ", line):
            items = []
            while index < len(lines) and re.match(r"^\d+\. ", lines[index]):
                item = re.sub(r"^\d+\. ", "", lines[index]).strip()
                items.append(f"<li>{inline_markdown(item)}</li>")
                index += 1
            blocks.append("<ol>\n" + "\n".join(items) + "\n</ol>")
            continue
        if line.startswith("> "):
            quote = []
            while index < len(lines) and lines[index].startswith("> "):
                quote.append(inline_markdown(lines[index][2:].strip()))
                index += 1
            blocks.append("<blockquote>" + "<br>\n".join(quote) + "</blockquote>")
            continue
        paragraph = [line]
        index += 1
        while index < len(lines) and lines[index].strip():
            if (
                lines[index].startswith(("# ", "## ", "### ", "- ", "* ", "> ", "```", "|"))
                or re.match(r"^\d+\. ", lines[index])
                or is_math_block_start(lines[index])
            ):
                break
            paragraph.append(lines[index].rstrip())
            index += 1
        blocks.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")
    return "\n\n".join(blocks)


def render_tags(tags: str) -> str:
    values = [tag.strip() for tag in tags.split(",") if tag.strip()]
    if not values:
        return "—"
    return " ".join(f'<span class="tag">{html.escape(tag)}</span>' for tag in values)


def parse_section(raw: str) -> tuple[str, Path]:
    if "=" not in raw:
        raise argparse.ArgumentTypeError("--section must be NAME=path")
    name, path = raw.split("=", 1)
    name = name.strip().upper()
    if name not in PLACEHOLDERS:
        allowed = ", ".join(sorted(PLACEHOLDERS))
        raise argparse.ArgumentTypeError(f"unknown section {name!r}; allowed: {allowed}")
    return name, Path(path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render an IntuitMath HTML note")
    parser.add_argument("--template", default="templates/math-note.html")
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--tags", default="")
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument("--section", action="append", default=[], type=parse_section)
    parser.add_argument("--raw-html", action="store_true", help="Do not convert section Markdown")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    template = Path(args.template).read_text(encoding="utf-8")
    replacements = {
        "TITLE": html.escape(args.title),
        "SUBTITLE": html.escape(args.subtitle),
        "TAGS": render_tags(args.tags),
        "DATE": html.escape(args.date),
    }

    for key in PLACEHOLDERS:
        replacements[key] = "<p><em>Not supplied.</em></p>"

    for key, path in args.section:
        text = path.read_text(encoding="utf-8")
        replacements[key] = text if args.raw_html else markdown_to_html(text)

    output = template
    for key, value in replacements.items():
        output = output.replace("{{" + key + "}}", value)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output, encoding="utf-8")
    print(out_path)


if __name__ == "__main__":
    main()
