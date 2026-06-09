# Platform Adapters

Use this reference when the host agent's tool names differ. IntuitMath should
depend on capabilities, not on a single platform.

## Capability Map

| Capability | Claude examples | Codex/OpenAI examples | Hermes/OpenClaw examples | Fallback |
|---|---|---|---|---|
| Search web | `websearch`, `webfetch`, MCP tools | `web.run`, browser/search MCP | `web_search`, `web_extract` | `curl` or cite uncertainty |
| Read files | project file tools | shell/read tools | workspace tools | ask user to paste content |
| Write files | artifact/file tools | `apply_patch`, shell, file tools | workspace tools | provide copyable content |
| Run scripts | bash/shell tool | terminal/shell tool | terminal tool | explain manual steps |
| OCR/vision | image input, PDF text extraction | image input, local OCR tools | OCR/vision plugins | ask for clearer image/transcription |
| Subagents | task/delegation tools | multi-agent MCP/tools if available | `delegate_task` style tools | run roles sequentially |
| Artifact/canvas output | artifacts | files or artifact tools if present | workspace artifacts | return copyable code block |
| Filesystem path output | project files/artifacts | workspace files | workspace files | avoid file claims |
| Inline HTML only | code block/artifact preview | code block | code block | Markdown note |
| Image upload but no OCR | native vision if enabled | local image inspection if available | plugin dependent | ask user to transcribe |

## Invocation Principles

- Treat `SKILL.md` as the universal entry point.
- Do not require platform-specific metadata to use the skill.
- Use optional platform folders only as integration hints, never as the source
  of mathematical behavior.
- If a platform cannot load extra files automatically, read only the references
  listed in the load map that match the current task.

## Tool Selection Heuristics

1. Prefer built-in search/browser tools for source discovery.
2. Prefer official docs, primary papers, and stable academic references.
3. Use shell scripts only when the environment is trusted and writable.
4. For private or exam-like user material, avoid uploading images to external
   OCR services unless the user explicitly approves.
5. If tools are unavailable, answer from reasoning and state which parts would
   benefit from verification.

## Permission States

Check permissions before acting:

- **Read-only**: inspect files but do not save problem records or HTML.
- **Workspace-write**: write only inside the active skill/user workspace.
- **No network**: do not require web verification; mark uncertain history.
- **No vision**: ask for transcription or use local text/PDF extraction.
- **No external uploads**: keep OCR local or manual.
- **Review-only request**: do not edit files even if writes are available.

## Portable Output Modes

- **Dialog**: Plain explanation in chat; works everywhere.
- **Markdown**: Best for Claude/Codex/Hermes notebooks and GitHub.
- **HTML**: Use `templates/math-note.html` for single-file notes with CDN KaTeX
  by default.
- **Problem library**: Use `scripts/save-problem.py` when filesystem access is
  available.
- **Copyable artifact**: When no filesystem exists, return a complete Markdown
  or HTML code block and say it has not been saved.

## Platform-Specific Metadata

If a host supports metadata such as `agents/openai.yaml`, `claude_desktop_config`,
or Hermes/OpenClaw manifests, keep it as a thin wrapper:

- Display name and short description only.
- Optional default prompt that invokes `$intuitmath`.
- No duplicate mathematical instructions.
- No platform-specific assumptions in `SKILL.md`.
