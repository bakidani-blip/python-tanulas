"""
Mobil tananyag-nezo generator.

Beolvassa az osszes Python lecke/gyakorlat fajlt,
es egyetlen offline HTML fajlt general beloluk.
A gyakorlat fajloknal interaktiv szerkeszto + Python futtato (Skulpt).

Hasznalat:
    python3 build_viewer.py

Kimenet:
    python_lessons.html (ugyanebben a mappaban)
"""

import html
import re
from pathlib import Path

# ============================================================
# KONFIGURACIO
# ============================================================

EXERCISES_DIR = Path(__file__).parent / "01-python-clean-code" / "exercises"
OUTPUT_FILE = Path(__file__).parent / "python_lessons.html"


# ============================================================
# FAJL BEOLVASAS ES RENDEZES
# ============================================================

def discover_files(directory: Path) -> list[dict]:
    """Megkeresi a .py fajlokat es parosba rendezi: lecke + gyakorlat(ok)."""
    lessons = {}
    exercises = {}

    for f in sorted(directory.glob("*.py")):
        name = f.stem
        content = f.read_text(encoding="utf-8")
        title = extract_title(content, name)
        entry = {"name": name, "filename": f.name, "title": title, "content": content}

        if name.startswith("exercise"):
            num = re.match(r"exercise_(\d+)", name)
            if num:
                key = num.group(1)
                entry["type"] = "exercise"
                exercises.setdefault(key, []).append(entry)
        else:
            num = re.match(r"(\d+)_", name)
            if num:
                key = num.group(1)
                entry["type"] = "lesson"
                lessons[key] = entry

    # Parositas: lecke + hozza tartozo gyakorlat(ok)
    paired = []
    for key in sorted(lessons.keys()):
        pair = {
            "key": key,
            "lesson": lessons[key],
            "exercises": exercises.get(key, []),
        }
        # Rovid nev a fulhoz
        title = lessons[key]["title"]
        # Az elso ertelmes szo(k) a cimbol
        short_names = {
            "00": "Alapok",
            "01": "Nevek",
            "02": "Fuggvenyek",
            "03": "DRY/KISS",
            "04": "Tipusok",
            "05": "Hibak",
        }
        pair["short_name"] = short_names.get(key, f"Lecke {key}")
        paired.append(pair)

    return paired


def extract_title(content: str, fallback: str) -> str:
    """Kiolvassa a cimet a docstringbol."""
    lines = content.split("\n")
    in_docstring = False
    found_separator = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('"""') or stripped.startswith("'''"):
            in_docstring = not in_docstring
            if stripped.count('"""') == 2 or stripped.count("'''") == 2:
                in_docstring = False
            continue
        if in_docstring:
            if re.match(r"^=+$", stripped):
                if found_separator:
                    found_separator = False
                else:
                    found_separator = True
                continue
            if found_separator and stripped:
                return stripped
    return fallback.replace("_", " ").title()


# ============================================================
# TARTALOM FELDOLGOZAS
# ============================================================

def parse_sections(content: str) -> list[list[dict]]:
    """Szetvalasztja a fajlt szekciokra."""
    lines = content.split("\n")

    # Docstring kiszedese
    cleaned_lines = []
    in_docstring = False
    docstring_done = False
    for line in lines:
        stripped = line.strip()
        if not docstring_done and (stripped.startswith('"""') or stripped.startswith("'''")):
            in_docstring = not in_docstring
            if stripped.count('"""') >= 2 or stripped.count("'''") >= 2:
                in_docstring = False
                docstring_done = True
            continue
        if in_docstring:
            continue
        if not docstring_done and not in_docstring and stripped:
            docstring_done = True
        if docstring_done:
            cleaned_lines.append(line)

    # Szekciokra bontas
    sections = []
    current_lines = []

    for line in cleaned_lines:
        stripped = line.strip()
        if re.match(r"^#\s*={10,}$", stripped):
            if current_lines:
                sections.append(current_lines)
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines:
        sections.append(current_lines)

    result = []
    for section_lines in sections:
        blocks = parse_blocks(section_lines)
        if blocks:
            result.append(blocks)

    return result


def parse_blocks(lines: list[str]) -> list[dict]:
    """Egy szekcio sorait text/code blokkokra bontja."""
    blocks = []
    current_type = None
    current_lines = []

    for line in lines:
        stripped = line.strip()

        if not stripped:
            if current_type in ("code", "text"):
                current_lines.append("")
            continue

        if stripped.startswith("#"):
            comment_text = re.sub(r"^#\s?", "", stripped)
            if current_type != "text":
                if current_lines and current_type:
                    blocks.append({"type": current_type, "content": "\n".join(current_lines).strip()})
                current_lines = []
                current_type = "text"
            current_lines.append(comment_text)
        else:
            if current_type != "code":
                if current_lines and current_type:
                    blocks.append({"type": current_type, "content": "\n".join(current_lines).strip()})
                current_lines = []
                current_type = "code"
            current_lines.append(line)

    if current_lines and current_type:
        blocks.append({"type": current_type, "content": "\n".join(current_lines).strip()})

    return blocks


# ============================================================
# HTML GENERALAS
# ============================================================

def render_text_block(text: str) -> str:
    """Szoveges blokkot HTML-re alakit."""
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"`(.+?)`", r'<code class="inline">\1</code>', escaped)
    if "\u2554" in escaped or "\u2551" in escaped:
        return f'<pre class="box">{escaped}</pre>'

    lines = escaped.split("\n")
    result_lines = []
    for line in lines:
        stripped = line.strip()
        if re.match(r"^-{3,}", stripped):
            continue
        if stripped and len(stripped) < 80 and (
            re.match(r"^\\d+\\.", stripped) or
            stripped.isupper() or
            re.match(r"^[A-Z\u00c1\u00c9\u00cd\u00d3\u00d6\u0150\u00da\u00dc\u0170]", stripped) and "\u2192" not in stripped and "=" not in stripped
        ):
            if stripped.isupper() or (len(stripped) < 50 and not stripped.endswith(".")):
                result_lines.append(f"<h3>{stripped}</h3>")
                continue
        result_lines.append(stripped)

    paragraphs = []
    current_p = []
    for line in result_lines:
        if line.startswith("<h3>"):
            if current_p:
                paragraphs.append("<p>" + "<br>".join(current_p) + "</p>")
                current_p = []
            paragraphs.append(line)
        elif not line:
            if current_p:
                paragraphs.append("<p>" + "<br>".join(current_p) + "</p>")
                current_p = []
        else:
            current_p.append(line)
    if current_p:
        paragraphs.append("<p>" + "<br>".join(current_p) + "</p>")

    return "\n".join(paragraphs)


def render_code_block(code: str) -> str:
    """Kod blokkot syntax-highlighted HTML-re alakit."""
    escaped = html.escape(code)
    return f'<pre class="code-block"><code>{escaped}</code></pre>'


def render_lesson(file_info: dict) -> str:
    """Egy lecke fajlt HTML-re alakit (csak olvasas)."""
    sections = parse_sections(file_info["content"])
    parts = [f'<div class="file-content" id="{file_info["name"]}">']
    parts.append('<div class="file-header">')
    parts.append('<span class="badge lesson">Lecke</span>')
    parts.append(f'<h2>{html.escape(file_info["title"])}</h2>')
    parts.append(f'<span class="filename">{html.escape(file_info["filename"])}</span>')
    parts.append('</div>')

    for section in sections:
        parts.append('<div class="section">')
        for block in section:
            if block["type"] == "text":
                parts.append(render_text_block(block["content"]))
            elif block["type"] == "code":
                parts.append(render_code_block(block["content"]))
        parts.append('</div>')

    parts.append('</div>')
    return "\n".join(parts)


def render_exercise(file_info: dict, index: int) -> str:
    """Egy exercise fajlt interaktiv szerkesztovel renderel."""
    escaped_content = html.escape(file_info["content"])
    exercise_id = f"exercise-{index}"

    return f'''<div class="file-content" id="{file_info["name"]}">
<div class="file-header">
<span class="badge exercise">Gyakorlat</span>
<h2>{html.escape(file_info["title"])}</h2>
<span class="filename">{html.escape(file_info["filename"])}</span>
</div>
<div class="exercise-editor">
<div class="editor-toolbar">
<button class="run-btn" onclick="runCode('{exercise_id}')">&#9654; Futtat\u00e1s</button>
<button class="reset-btn" onclick="resetCode('{exercise_id}')">&#8634; Vissza\u00e1ll\u00edt\u00e1s</button>
</div>
<textarea id="{exercise_id}" class="code-editor" spellcheck="false" autocapitalize="off" autocomplete="off" autocorrect="off">{escaped_content}</textarea>
<div id="{exercise_id}-output" class="output-area">
<span class="output-placeholder">Nyomd meg a &#9654; Futtat\u00e1s gombot az eredm\u00e9ny\u00e9rt</span>
</div>
</div>
</div>'''


def generate_html(pairs: list[dict]) -> str:
    """A teljes HTML oldalt generalja parosított leckekbol."""

    # Navigacios fulek
    tabs_html = []
    for i, pair in enumerate(pairs):
        active = "active" if i == 0 else ""
        lesson_title = html.escape(pair["lesson"]["title"])
        tabs_html.append(
            f'<button class="tab {active}" data-index="{i}" title="{lesson_title}">'
            f'{pair["short_name"]}</button>'
        )

    # Tartalom panelek: lecke + accordion gyakorlat(ok)
    panels_html = []
    exercise_global_idx = 0
    for i, pair in enumerate(pairs):
        display = "" if i == 0 else ' style="display:none"'
        panels_html.append(f'<div class="panel" data-index="{i}"{display}>')

        # Lecke resz
        panels_html.append(render_lesson(pair["lesson"]))

        # Gyakorlat(ok) accordion-ban
        for ex in pair["exercises"]:
            ex_id = f"exercise-{exercise_global_idx}"
            escaped_content = html.escape(ex["content"])
            panels_html.append(f'''
<div class="accordion">
<button class="accordion-toggle" onclick="toggleAccordion(this)">
<span>\u270f\ufe0f Gyakorlat: {html.escape(ex["title"])}</span>
<span class="accordion-arrow">\u25bc</span>
</button>
<div class="accordion-content" style="display:none">
<div class="exercise-editor">
<div class="editor-toolbar">
<button class="run-btn" onclick="runCode('{ex_id}')">\u25b6 Futtat\u00e1s</button>
<button class="reset-btn" onclick="resetCode('{ex_id}')">\u21ba Vissza\u00e1ll\u00edt\u00e1s</button>
</div>
<textarea id="{ex_id}" class="code-editor" spellcheck="false" autocapitalize="off" autocomplete="off" autocorrect="off">{escaped_content}</textarea>
<div id="{ex_id}-output" class="output-area">
<span class="output-placeholder">Nyomd meg a \u25b6 Futtat\u00e1s gombot az eredm\u00e9ny\u00e9rt</span>
</div>
</div>
</div>
</div>''')
            exercise_global_idx += 1

        panels_html.append('</div>')

    # Original contents for reset
    originals = {}
    ex_idx = 0
    for pair in pairs:
        for ex in pair["exercises"]:
            originals[f"exercise-{ex_idx}"] = ex["content"]
            ex_idx += 1

    originals_js = "var ORIGINALS = {" + ", ".join(
        f'"{k}": {repr(v)}' for k, v in originals.items()
    ) + "};"

    return get_html_template(
        tabs="\n".join(tabs_html),
        panels="\n".join(panels_html),
        originals_js=originals_js
    )


def get_html_template(tabs: str, panels: str, originals_js: str) -> str:
    """Returns the complete HTML template with content inserted."""

    # Build the template in parts to avoid triple-quote issues
    part1 = """<!DOCTYPE html>
<html lang="hu" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<title>Python Leckek</title>
<style>
:root {
  --bg-primary: #1e1e2e;
  --bg-secondary: #181825;
  --bg-card: #313244;
  --bg-card-hover: #45475a;
  --bg-surface: #11111b;
  --text-primary: #cdd6f4;
  --text-secondary: #a6adc8;
  --text-muted: #6c7086;
  --accent: #89b4fa;
  --accent-green: #a6e3a1;
  --accent-yellow: #f9e2af;
  --accent-red: #f38ba8;
  --accent-purple: #cba6f7;
  --accent-peach: #fab387;
  --border: #45475a;
  --shadow: rgba(0, 0, 0, 0.3);
  --font-size: 15px;
  --syn-keyword: #cba6f7;
  --syn-string: #a6e3a1;
  --syn-comment: #6c7086;
  --syn-number: #fab387;
  --syn-builtin: #89b4fa;
  --syn-decorator: #f9e2af;
  --syn-self: #f38ba8;
}

[data-theme="light"] {
  --bg-primary: #eff1f5;
  --bg-secondary: #e6e9ef;
  --bg-card: #ffffff;
  --bg-card-hover: #dce0e8;
  --bg-surface: #ccd0da;
  --text-primary: #4c4f69;
  --text-secondary: #6c6f85;
  --text-muted: #9ca0b0;
  --accent: #1e66f5;
  --accent-green: #40a02b;
  --accent-yellow: #df8e1d;
  --accent-red: #d20f39;
  --accent-purple: #8839ef;
  --accent-peach: #fe640b;
  --border: #ccd0da;
  --shadow: rgba(0, 0, 0, 0.1);
  --syn-keyword: #8839ef;
  --syn-string: #40a02b;
  --syn-comment: #9ca0b0;
  --syn-number: #fe640b;
  --syn-builtin: #1e66f5;
  --syn-decorator: #df8e1d;
  --syn-self: #d20f39;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: var(--font-size); -webkit-text-size-adjust: 100%; }
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
  background: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.6;
  min-height: 100vh;
  padding-bottom: 70px;
}

.topbar {
  position: sticky; top: 0; z-index: 100;
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border);
  padding: 8px 16px;
  display: flex; align-items: center; justify-content: space-between; gap: 8px;
  -webkit-backdrop-filter: blur(10px); backdrop-filter: blur(10px);
}
.topbar h1 { font-size: 1rem; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; flex: 1; }
.topbar-controls { display: flex; gap: 4px; flex-shrink: 0; }
.topbar-btn {
  background: var(--bg-card); color: var(--text-primary);
  border: 1px solid var(--border); border-radius: 8px;
  padding: 6px 10px; font-size: 1rem; cursor: pointer;
  min-width: 40px; min-height: 40px;
  display: flex; align-items: center; justify-content: center;
  -webkit-tap-highlight-color: transparent;
}
.topbar-btn:active { background: var(--bg-card-hover); }

.content { max-width: 800px; margin: 0 auto; padding: 16px; }
.file-content { animation: fadeIn 0.2s ease; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

.file-header { margin-bottom: 24px; padding-bottom: 16px; border-bottom: 2px solid var(--border); }
.file-header h2 { font-size: 1.4rem; font-weight: 700; margin: 8px 0 4px; }
.filename { font-family: 'SF Mono', 'Menlo', 'Monaco', 'Courier New', monospace; font-size: 0.8rem; color: var(--text-muted); }

.badge { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }
.badge.lesson { background: var(--accent-green); color: #1e1e2e; }
.badge.exercise { background: var(--accent-yellow); color: #1e1e2e; }

.section { margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--border); }
.section:last-child { border-bottom: none; }
.section h3 { font-size: 1.1rem; font-weight: 700; color: var(--accent); margin: 16px 0 8px; }
.section p { color: var(--text-secondary); margin-bottom: 12px; line-height: 1.7; }
.section strong { color: var(--text-primary); }

code.inline {
  font-family: 'SF Mono', 'Menlo', 'Monaco', 'Courier New', monospace;
  background: var(--bg-card); padding: 2px 6px; border-radius: 4px;
  font-size: 0.9em; color: var(--accent-peach);
}
pre.box {
  font-family: 'SF Mono', 'Menlo', 'Monaco', 'Courier New', monospace;
  background: var(--bg-card); border: 1px solid var(--accent);
  border-radius: 8px; padding: 12px 16px; margin: 12px 0;
  font-size: 0.85rem; overflow-x: auto; line-height: 1.5; color: var(--accent);
}
pre.code-block {
  background: var(--bg-surface); border: 1px solid var(--border);
  border-radius: 10px; padding: 14px 16px; margin: 12px 0;
  overflow-x: auto; -webkit-overflow-scrolling: touch;
  font-size: 0.85rem; line-height: 1.6;
}
pre.code-block code {
  font-family: 'SF Mono', 'Menlo', 'Monaco', 'Courier New', monospace;
  color: var(--text-primary);
}
.syn-kw { color: var(--syn-keyword); font-weight: 500; }
.syn-str { color: var(--syn-string); }
.syn-cmt { color: var(--syn-comment); font-style: italic; }
.syn-num { color: var(--syn-number); }
.syn-bi { color: var(--syn-builtin); }
.syn-dec { color: var(--syn-decorator); }
.syn-self { color: var(--syn-self); }

/* ============ EXERCISE EDITOR ============ */
.exercise-editor { margin-top: 8px; }

.editor-toolbar {
  display: flex; gap: 8px; margin-bottom: 8px;
}

.run-btn {
  background: var(--accent-green); color: #1e1e2e;
  border: none; border-radius: 8px;
  padding: 10px 20px; font-size: 1rem; font-weight: 700;
  cursor: pointer; min-height: 44px;
  -webkit-tap-highlight-color: transparent;
  flex: 1;
}
.run-btn:active { opacity: 0.8; }
.run-btn.running { background: var(--accent-yellow); }

.reset-btn {
  background: var(--bg-card); color: var(--text-secondary);
  border: 1px solid var(--border); border-radius: 8px;
  padding: 10px 16px; font-size: 0.9rem;
  cursor: pointer; min-height: 44px;
  -webkit-tap-highlight-color: transparent;
}
.reset-btn:active { background: var(--bg-card-hover); }

.code-editor {
  width: 100%;
  min-height: 400px;
  background: var(--bg-surface);
  color: var(--text-primary);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px 16px;
  font-family: 'SF Mono', 'Menlo', 'Monaco', 'Courier New', monospace;
  font-size: 0.85rem;
  line-height: 1.6;
  resize: vertical;
  -webkit-overflow-scrolling: touch;
  tab-size: 4;
  white-space: pre;
  overflow-wrap: normal;
  overflow-x: auto;
}
.code-editor:focus {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.output-area {
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px 16px;
  margin-top: 8px;
  font-family: 'SF Mono', 'Menlo', 'Monaco', 'Courier New', monospace;
  font-size: 0.85rem;
  line-height: 1.6;
  white-space: pre-wrap;
  word-break: break-word;
  max-height: 400px;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
}
.output-placeholder { color: var(--text-muted); font-style: italic; }
.output-error { color: var(--accent-red); }
.output-success { color: var(--accent-green); }

/* ============ BOTTOM NAV ============ */
.bottom-nav {
  position: fixed; bottom: 0; left: 0; right: 0; z-index: 100;
  background: var(--bg-secondary);
  border-top: 1px solid var(--border);
  display: flex; overflow-x: auto; -webkit-overflow-scrolling: touch;
  padding: 4px 4px calc(4px + env(safe-area-inset-bottom));
  gap: 2px; scrollbar-width: none;
}
.bottom-nav::-webkit-scrollbar { display: none; }

.tab {
  flex-shrink: 0; background: transparent; color: var(--text-muted);
  border: none; border-radius: 8px;
  padding: 10px 14px; font-size: 0.8rem; font-weight: 500;
  cursor: pointer; white-space: nowrap; min-height: 44px;
  -webkit-tap-highlight-color: transparent; transition: all 0.15s ease;
}
.tab.active { background: var(--accent); color: #1e1e2e; font-weight: 700; }
.tab:not(.active):active { background: var(--bg-card); color: var(--text-primary); }

/* ============ ACCORDION ============ */
.accordion {
  margin-top: 24px;
  border: 2px solid var(--accent-yellow);
  border-radius: 12px;
  overflow: hidden;
}
.accordion-toggle {
  width: 100%;
  background: var(--bg-card);
  color: var(--text-primary);
  border: none;
  padding: 14px 16px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 50px;
  -webkit-tap-highlight-color: transparent;
}
.accordion-toggle:active { background: var(--bg-card-hover); }
.accordion-arrow { transition: transform 0.2s ease; font-size: 0.8rem; }
.accordion-toggle.open .accordion-arrow { transform: rotate(180deg); }
.accordion-content {
  padding: 16px;
  border-top: 1px solid var(--border);
}

.scroll-top {
  position: fixed; bottom: 80px; right: 16px;
  background: var(--accent); color: #1e1e2e;
  border: none; border-radius: 50%;
  width: 44px; height: 44px; font-size: 1.2rem;
  cursor: pointer; display: none;
  align-items: center; justify-content: center;
  box-shadow: 0 2px 8px var(--shadow); z-index: 90;
  -webkit-tap-highlight-color: transparent;
}
</style>
</head>
<body>

<div class="topbar">
  <h1 id="current-title">Python Leckek</h1>
  <div class="topbar-controls">
    <button class="topbar-btn" id="font-down" title="Kisebb betu">A-</button>
    <button class="topbar-btn" id="font-up" title="Nagyobb betu">A+</button>
    <button class="topbar-btn" id="theme-toggle" title="Tema valtas"></button>
  </div>
</div>

<div class="content" id="content">
"""

    part2 = """
</div>

<nav class="bottom-nav" id="bottom-nav">
"""

    part3 = """
</nav>

<button class="scroll-top" id="scroll-top" title="Fel">&uarr;</button>

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script>
(function() {
"""

    # JS code - build separately to avoid escape issues
    js_code = originals_js + """

  // ---- Accordion toggle ----
  window.toggleAccordion = function(btn) {
    var content = btn.nextElementSibling;
    var isOpen = content.style.display !== 'none';
    content.style.display = isOpen ? 'none' : 'block';
    btn.classList.toggle('open', !isOpen);
  };

  // ---- Skulpt Python runner ----
  window.runCode = function(editorId) {
    var editor = document.getElementById(editorId);
    var outputEl = document.getElementById(editorId + '-output');
    var code = editor.value;

    // Save to localStorage
    localStorage.setItem('code-' + editorId, code);

    outputEl.innerHTML = '';
    var outputText = '';

    function outf(text) {
      outputText += text;
    }
    function builtinRead(x) {
      if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
        throw "File not found: '" + x + "'";
      return Sk.builtinFiles["files"][x];
    }

    Sk.configure({
      output: outf,
      read: builtinRead,
      __future__: Sk.python3
    });

    Sk.misceval.asyncToPromise(function() {
      return Sk.importMainWithBody("<stdin>", false, code, true);
    }).then(function() {
      // Format output with colors
      var lines = outputText.split('\\n');
      var html = lines.map(function(line) {
        if (line.indexOf('\\u2713') >= 0 || line.indexOf('\\u2714') >= 0 || line.indexOf('OK') >= 0 && line.indexOf('\\u2713') >= 0) {
          return '<span class="output-success">' + escapeHtml(line) + '</span>';
        } else if (line.indexOf('\\u2717') >= 0 || line.indexOf('\\u2718') >= 0 || line.indexOf('HIBA') >= 0) {
          return '<span class="output-error">' + escapeHtml(line) + '</span>';
        } else if (line.indexOf('MINDEN FELADAT') >= 0 || line.indexOf('\\ud83c\\udf89') >= 0) {
          return '<span class="output-success"><strong>' + escapeHtml(line) + '</strong></span>';
        }
        return escapeHtml(line);
      }).join('\\n');
      outputEl.innerHTML = html;
    }).catch(function(err) {
      var errMsg = err.toString();
      // Make error message more helpful
      var match = errMsg.match(/line (\\d+)/);
      var lineInfo = match ? ' (sor: ' + match[1] + ')' : '';
      outputEl.innerHTML = '<span class="output-error">Hiba' + lineInfo + ':\\n' + escapeHtml(errMsg) + '</span>';
    });
  };

  window.resetCode = function(editorId) {
    if (confirm('Biztosan visszaallitod az eredeti kodot? A valtoztatasaid elvesznek!')) {
      var editor = document.getElementById(editorId);
      if (ORIGINALS[editorId]) {
        editor.value = ORIGINALS[editorId];
        localStorage.removeItem('code-' + editorId);
        document.getElementById(editorId + '-output').innerHTML =
          '<span class="output-placeholder">Visszaallitva. Nyomd meg a \\u25b6 Futtatas gombot.</span>';
      }
    }
  };

  function escapeHtml(text) {
    var div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Restore saved code from localStorage
  document.querySelectorAll('.code-editor').forEach(function(editor) {
    var saved = localStorage.getItem('code-' + editor.id);
    if (saved) editor.value = saved;

    // Auto-save on change
    editor.addEventListener('input', function() {
      localStorage.setItem('code-' + this.id, this.value);
    });

    // Tab key support in textarea
    editor.addEventListener('keydown', function(e) {
      if (e.key === 'Tab') {
        e.preventDefault();
        var start = this.selectionStart;
        var end = this.selectionEnd;
        this.value = this.value.substring(0, start) + '    ' + this.value.substring(end);
        this.selectionStart = this.selectionEnd = start + 4;
      }
    });
  });

  // ---- Syntax highlighting for lesson code blocks ----
  var KW = new Set(['False','None','True','and','as','assert','async','await','break','class','continue','def','del','elif','else','except','finally','for','from','global','if','import','in','is','lambda','nonlocal','not','or','pass','raise','return','try','while','with','yield']);
  var BI = new Set(['print','len','range','int','str','float','list','dict','set','tuple','bool','input','open','type','isinstance','enumerate','zip','map','filter','sorted','reversed','sum','min','max','abs','round','any','all','super','property','staticmethod','classmethod','hasattr','getattr','setattr']);

  function hlPy(code) {
    var r = '', i = 0;
    while (i < code.length) {
      if (code[i]==='@' && (i===0||code[i-1]==='\\n')) { var e=code.indexOf('\\n',i); if(e===-1)e=code.length; r+='<span class="syn-dec">'+code.slice(i,e)+'</span>'; i=e; continue; }
      if (code[i]==='#') { var e=code.indexOf('\\n',i); if(e===-1)e=code.length; r+='<span class="syn-cmt">'+code.slice(i,e)+'</span>'; i=e; continue; }
      var tq='"'+'"'+'"', tq2="'"+"'"+"'";
      if (code.slice(i,i+3)===tq||code.slice(i,i+3)===tq2) { var q=code.slice(i,i+3),e=code.indexOf(q,i+3); if(e===-1)e=code.length-3; e+=3; r+='<span class="syn-str">'+code.slice(i,e)+'</span>'; i=e; continue; }
      if (code[i]==='"'||code[i]==="'") { var q=code[i],j=i+1; while(j<code.length&&code[j]!==q&&code[j]!=='\\n'){if(code[j]==='\\\\')j++;j++;} if(j<code.length&&code[j]===q)j++; r+='<span class="syn-str">'+code.slice(i,j)+'</span>'; i=j; continue; }
      if ((code[i]==='f'||code[i]==='F')&&i+1<code.length&&(code[i+1]==='"'||code[i+1]==="'")) { var q=code[i+1],j=i+2; while(j<code.length&&code[j]!==q&&code[j]!=='\\n'){if(code[j]==='\\\\')j++;j++;} if(j<code.length&&code[j]===q)j++; r+='<span class="syn-str">'+code.slice(i,j)+'</span>'; i=j; continue; }
      if (/\\d/.test(code[i])&&(i===0||/[\\s(,=+\\-*/<>\\[\\]:]/.test(code[i-1]))) { var j=i; while(j<code.length&&/[\\d._]/.test(code[j]))j++; r+='<span class="syn-num">'+code.slice(i,j)+'</span>'; i=j; continue; }
      if (/[a-zA-Z_]/.test(code[i])) { var j=i; while(j<code.length&&/[a-zA-Z0-9_]/.test(code[j]))j++; var w=code.slice(i,j); if(w==='self')r+='<span class="syn-self">'+w+'</span>'; else if(KW.has(w))r+='<span class="syn-kw">'+w+'</span>'; else if(BI.has(w)&&j<code.length&&code[j]==='(')r+='<span class="syn-bi">'+w+'</span>'; else r+=w; i=j; continue; }
      r+=code[i]; i++;
    }
    return r;
  }

  document.querySelectorAll('pre.code-block code').forEach(function(el) {
    el.innerHTML = hlPy(el.textContent);
  });

  // ---- Tab navigation ----
  var tabs = document.querySelectorAll('.tab');
  var panels = document.querySelectorAll('.panel');
  var titleEl = document.getElementById('current-title');

  function showPanel(index) {
    panels.forEach(function(p) { p.style.display = 'none'; });
    tabs.forEach(function(t) { t.classList.remove('active'); });
    panels[index].style.display = '';
    tabs[index].classList.add('active');
    titleEl.textContent = tabs[index].title;
    window.scrollTo(0, 0);
    tabs[index].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    localStorage.setItem('lastTab', index);
    location.hash = 'tab-' + index;
  }

  tabs.forEach(function(tab) {
    tab.addEventListener('click', function() {
      showPanel(parseInt(this.dataset.index));
    });
  });

  var hashMatch = location.hash.match(/tab-(\\d+)/);
  var lastTab = hashMatch ? parseInt(hashMatch[1]) : parseInt(localStorage.getItem('lastTab') || '0');
  if (lastTab >= 0 && lastTab < panels.length) showPanel(lastTab);

  // ---- Theme toggle ----
  var themeBtn = document.getElementById('theme-toggle');
  var savedTheme = localStorage.getItem('theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);
  themeBtn.textContent = savedTheme === 'dark' ? '\\u2600\\ufe0f' : '\\ud83c\\udf19';

  themeBtn.addEventListener('click', function() {
    var current = document.documentElement.getAttribute('data-theme');
    var next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    this.textContent = next === 'dark' ? '\\u2600\\ufe0f' : '\\ud83c\\udf19';
    localStorage.setItem('theme', next);
  });

  // ---- Font size ----
  var fontSize = parseInt(localStorage.getItem('fontSize') || '15');
  document.documentElement.style.setProperty('--font-size', fontSize + 'px');

  document.getElementById('font-up').addEventListener('click', function() {
    fontSize = Math.min(fontSize + 2, 24);
    document.documentElement.style.setProperty('--font-size', fontSize + 'px');
    localStorage.setItem('fontSize', fontSize);
  });
  document.getElementById('font-down').addEventListener('click', function() {
    fontSize = Math.max(fontSize - 2, 10);
    document.documentElement.style.setProperty('--font-size', fontSize + 'px');
    localStorage.setItem('fontSize', fontSize);
  });

  // ---- Scroll to top ----
  var scrollBtn = document.getElementById('scroll-top');
  window.addEventListener('scroll', function() {
    scrollBtn.style.display = window.scrollY > 300 ? 'flex' : 'none';
  });
  scrollBtn.addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
})();
"""

    part4 = """
</script>
</body>
</html>"""

    return part1 + panels + part2 + tabs + part3 + js_code + part4


# ============================================================
# FUTTATAS
# ============================================================

def main():
    if not EXERCISES_DIR.exists():
        print(f"HIBA: Nem talalhato a mappa: {EXERCISES_DIR}")
        return

    pairs = discover_files(EXERCISES_DIR)
    if not pairs:
        print(f"HIBA: Nincs .py fajl a mappaban: {EXERCISES_DIR}")
        return

    print(f"Talalt modulok ({len(pairs)}):")
    for pair in pairs:
        lesson = pair["lesson"]
        exercises = pair["exercises"]
        print(f"  \U0001f4d6 {lesson['filename']} \u2014 {lesson['title']}")
        for ex in exercises:
            print(f"    \u270f\ufe0f {ex['filename']}")

    html_content = generate_html(pairs)
    OUTPUT_FILE.write_text(html_content, encoding="utf-8")

    size_kb = OUTPUT_FILE.stat().st_size / 1024
    print(f"\n\u2705 Generalva: {OUTPUT_FILE}")
    print(f"   Meret: {size_kb:.0f} KB")
    print(f"\n\U0001f4a1 Nyisd meg bongeszobben, vagy kuldd at a telefonodra.")


if __name__ == "__main__":
    main()
