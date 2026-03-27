"""
Mobil tananyag-nezo generator.

Beolvassa az osszes lecke/gyakorlat fajlt (Python es C++),
es modulonkent kulon offline HTML fajlt general beloluk.

Hasznalat:
    python3 build_viewer.py

Kimenet:
    python_lessons.html
    cpp_lessons.html
"""

import html
import re
from pathlib import Path

# ============================================================
# MODUL KONFIGURACIO
# ============================================================

BASE_DIR = Path(__file__).parent

MODULES = [
    {
        "id": "python",
        "dir": BASE_DIR / "01-python-clean-code" / "exercises",
        "ext": ".py",
        "output": BASE_DIR / "python_lessons.html",
        "title": "Python Leckek",
        "comment_line": "#",
        "section_sep": r"^#\s*={10,}$",
        "docstring_delims": ['"""', "'''"],
        "short_names": {
            "00": "Alapok",
            "01": "Nevek",
            "02": "Fuggvenyek",
            "03": "DRY/KISS",
            "04": "Tipusok",
            "05": "Hibak",
        },
        "runtime": "skulpt",
    },
    {
        "id": "cpp",
        "dir": BASE_DIR / "05-cpp-alapok" / "exercises",
        "ext": ".cpp",
        "output": BASE_DIR / "cpp_lessons.html",
        "title": "C++ Leckek",
        "comment_line": "//",
        "section_sep": r"^//\s*={10,}$",
        "docstring_delims": [],  # C++ uses /* */ block comments
        "short_names": {
            "01": "Alapok",
            "02": "Valtozok",
            "03": "Feltetel",
            "04": "Ciklus",
            "05": "Fuggveny",
        },
        "runtime": "jscpp",
    },
]


# ============================================================
# FAJL BEOLVASAS ES RENDEZES
# ============================================================

def discover_files(directory: Path, ext: str, short_names: dict) -> list[dict]:
    """Megkeresi a fajlokat es parosba rendezi: lecke + gyakorlat(ok)."""
    lessons = {}
    exercises = {}

    for f in sorted(directory.glob(f"*{ext}")):
        name = f.stem
        content = f.read_text(encoding="utf-8")
        title = extract_title(content, name, ext)
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

    paired = []
    for key in sorted(lessons.keys()):
        pair = {
            "key": key,
            "lesson": lessons[key],
            "exercises": exercises.get(key, []),
            "short_name": short_names.get(key, f"Lecke {key}"),
        }
        paired.append(pair)

    return paired


def extract_title(content: str, fallback: str, ext: str) -> str:
    """Kiolvassa a cimet a docstringbol / blokk kommentbol."""
    lines = content.split("\n")

    if ext == ".cpp":
        # C++: /* ... */ blokk kommentbol
        in_block = False
        found_separator = False
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("/*"):
                in_block = True
                continue
            if in_block and stripped.endswith("*/"):
                break
            if in_block:
                if re.match(r"^=+$", stripped):
                    if found_separator:
                        found_separator = False
                    else:
                        found_separator = True
                    continue
                if found_separator and stripped:
                    return stripped
        return fallback.replace("_", " ").title()

    # Python: """ ... """ docstringbol
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

def parse_sections(content: str, config: dict) -> list[list[dict]]:
    """Szetvalasztja a fajlt szekciokra."""
    lines = content.split("\n")
    comment_line = config["comment_line"]
    section_sep = config["section_sep"]
    ext = config["ext"]

    # Docstring / blokk komment kiszedese
    cleaned_lines = []
    if ext == ".cpp":
        # C++: /* ... */ blokk komment kiszedese az elejerol
        in_block = False
        block_done = False
        for line in lines:
            stripped = line.strip()
            if not block_done and stripped.startswith("/*"):
                in_block = True
                continue
            if in_block:
                if stripped.endswith("*/") or "*/" in stripped:
                    in_block = False
                    block_done = True
                continue
            if block_done or stripped:
                block_done = True
                cleaned_lines.append(line)
    else:
        # Python: """ ... """ kiszedese
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
        if re.match(section_sep, stripped):
            if current_lines:
                sections.append(current_lines)
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines:
        sections.append(current_lines)

    result = []
    for section_lines in sections:
        blocks = parse_blocks(section_lines, comment_line)
        if blocks:
            result.append(blocks)

    return result


def parse_blocks(lines: list[str], comment_line: str) -> list[dict]:
    """Egy szekcio sorait text/code blokkokra bontja."""
    blocks = []
    current_type = None
    current_lines = []
    prefix = comment_line  # "#" or "//"

    for line in lines:
        stripped = line.strip()

        if not stripped:
            if current_type in ("code", "text"):
                current_lines.append("")
            continue

        # Ellenorzes: komment sor-e (de C++ #include NEM komment!)
        is_comment = stripped.startswith(prefix)
        if prefix == "#" and is_comment:
            # Python: # barmilyen komment
            pass
        elif prefix == "//" and is_comment:
            # C++: // komment
            pass
        else:
            is_comment = False

        if is_comment:
            comment_text = re.sub(r"^" + re.escape(prefix) + r"\s?", "", stripped)
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


def parse_exercise_tasks(content: str) -> list[dict] | None:
    """Ha a fajl @TASK markereket tartalmaz, task-okra bontja.

    Visszaad egy listat:
      [{"title": "...", "desc": "...", "hint": "...", "code": "..."}, ...]
    Vagy None-t, ha nincs @TASK marker (regi formatum).
    """
    if "// @TASK" not in content and "# @TASK" not in content:
        return None

    tasks = []
    current = None
    mode = None  # "desc", "hint", "code"

    for line in content.split("\n"):
        stripped = line.strip()
        # Komment prefix levagasa
        clean = stripped
        for prefix in ("// ", "# "):
            if clean.startswith(prefix):
                clean = clean[len(prefix):]
                break

        if stripped.endswith("@TASK") and len(stripped.split("@TASK")) == 2:
            # Uj @TASK sor: "// @TASK 1. Cim" vagy "# @TASK 1. Cim"
            pass  # Fall through to below check

        if "@TASK" in stripped and ("// @TASK" in stripped or "# @TASK" in stripped):
            if current and current.get("code"):
                tasks.append(current)
            title = clean.replace("@TASK", "").strip()
            current = {"title": title, "desc": "", "hint": "", "code": ""}
            mode = None
            continue

        if current is None:
            continue

        if clean.startswith("@DESC"):
            text = clean[5:].strip()
            if current["desc"]:
                current["desc"] += "\n" + text
            else:
                current["desc"] = text
            mode = "desc"
            continue

        if clean.startswith("@HINT"):
            text = clean[5:].strip()
            current["hint"] = text
            mode = "hint"
            continue

        if clean.startswith("@CODE"):
            mode = "code"
            continue

        if clean.startswith("@END"):
            if current and current.get("code"):
                # Trim trailing whitespace from code
                current["code"] = current["code"].strip()
                tasks.append(current)
            current = None
            mode = None
            continue

        # Folytatas sorok
        if mode == "desc" and (stripped.startswith("// ") or stripped.startswith("# ")):
            line_text = clean.strip()
            if line_text and not line_text.startswith("@"):
                current["desc"] += "\n" + line_text
        elif mode == "hint" and (stripped.startswith("// ") or stripped.startswith("# ")):
            line_text = clean.strip()
            if line_text and not line_text.startswith("@"):
                current["hint"] += "\n" + line_text
        elif mode == "code":
            if current["code"]:
                current["code"] += "\n" + line
            else:
                current["code"] = line

    if current and current.get("code"):
        current["code"] = current["code"].strip()
        tasks.append(current)

    return tasks if tasks else None


def render_exercise_tasks(tasks: list[dict], start_idx: int) -> tuple[str, int]:
    """Task-alapu gyakorlatokat renderel kulon editorokkal.

    Visszaadja a HTML stringet es az utolso exercise index-et.
    """
    parts = []
    idx = start_idx

    for task in tasks:
        ex_id = f"exercise-{idx}"
        escaped_code = html.escape(task["code"])

        # Leiras formatazasa
        desc_html = ""
        if task["desc"]:
            desc_escaped = html.escape(task["desc"])
            desc_escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", desc_escaped)
            desc_escaped = re.sub(r"`(.+?)`", r'<code class="inline">\1</code>', desc_escaped)
            desc_html = f'<p class="task-desc">{desc_escaped}</p>'

        # Tipp
        hint_html = ""
        if task["hint"]:
            hint_escaped = html.escape(task["hint"])
            hint_escaped = re.sub(r"`(.+?)`", r'<code class="inline">\1</code>', hint_escaped)
            hint_html = f'''<details class="task-hint">
<summary>\U0001f4a1 Tipp</summary>
<p>{hint_escaped}</p>
</details>'''

        parts.append(f'''<div class="task-card">
<div class="task-header">
<h3>{html.escape(task["title"])}</h3>
</div>
{desc_html}
{hint_html}
<div class="exercise-editor">
<div class="editor-toolbar">
<button class="run-btn" onclick="runCode('{ex_id}')">\u25b6 Futtat\u00e1s</button>
<button class="reset-btn" onclick="resetCode('{ex_id}')">\u21ba Vissza\u00e1ll\u00edt\u00e1s</button>
</div>
<textarea id="{ex_id}" class="code-editor" spellcheck="false" autocapitalize="off" autocomplete="off" autocorrect="off">{escaped_code}</textarea>
<div id="{ex_id}-output" class="output-area">
<span class="output-placeholder">Nyomd meg a \u25b6 Futtat\u00e1s gombot az eredm\u00e9ny\u00e9rt</span>
</div>
</div>
</div>''')
        idx += 1

    return "\n".join(parts), idx


def render_lesson(file_info: dict) -> str:
    """Egy lecke fajlt HTML-re alakit (csak olvasas)."""
    sections = parse_sections(file_info["content"], file_info["_config"])
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


def generate_html(pairs: list[dict], config: dict) -> str:
    """A teljes HTML oldalt generalja parosított leckekbol."""

    # Config hozzaadasa a fajl info-khoz (render_lesson-nek kell)
    for pair in pairs:
        pair["lesson"]["_config"] = config

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
    originals = {}
    exercise_global_idx = 0

    for i, pair in enumerate(pairs):
        display = "" if i == 0 else ' style="display:none"'
        panels_html.append(f'<div class="panel" data-index="{i}"{display}>')

        # Lecke resz
        panels_html.append(render_lesson(pair["lesson"]))

        # Gyakorlat(ok) accordion-ban
        for ex in pair["exercises"]:
            tasks = parse_exercise_tasks(ex["content"])

            if tasks:
                # Task-alapu formatum: kulon editor minden feladathoz
                panels_html.append(f'''
<div class="accordion">
<button class="accordion-toggle" onclick="toggleAccordion(this)">
<span>\u270f\ufe0f Gyakorlat: {html.escape(ex["title"])}</span>
<span class="accordion-arrow">\u25bc</span>
</button>
<div class="accordion-content" style="display:none">''')
                tasks_html, new_idx = render_exercise_tasks(tasks, exercise_global_idx)
                panels_html.append(tasks_html)
                panels_html.append('</div>\n</div>')

                for task in tasks:
                    originals[f"exercise-{exercise_global_idx}"] = task["code"]
                    exercise_global_idx += 1
            else:
                # Regi formatum: egy nagy editor
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
                originals[f"exercise-{exercise_global_idx}"] = ex["content"]
                exercise_global_idx += 1

        panels_html.append('</div>')

    originals_js = "var ORIGINALS = {" + ", ".join(
        f'"{k}": {repr(v)}' for k, v in originals.items()
    ) + "};"

    return get_html_template(
        tabs="\n".join(tabs_html),
        panels="\n".join(panels_html),
        originals_js=originals_js,
        config=config,
    )


# ============================================================
# RUNTIME ES SYNTAX HIGHLIGHT JS
# ============================================================

def get_runtime_scripts(runtime: str) -> str:
    """CDN script tagek a runtime-hoz."""
    if runtime == "skulpt":
        return '<script src="https://skulpt.org/js/skulpt.min.js"></script>\n<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>'
    elif runtime == "jscpp":
        return '<script src="https://cdn.jsdelivr.net/npm/JSCPP@2.0.4/dist/JSCPP.es5.min.js"></script>'
    return ""


def get_run_code_js(runtime: str) -> str:
    """A runCode() fuggveny a megfelelo runtime-hoz."""
    if runtime == "skulpt":
        return """
  window.runCode = function(editorId) {
    var editor = document.getElementById(editorId);
    var outputEl = document.getElementById(editorId + '-output');
    var code = editor.value;
    localStorage.setItem('code-' + editorId, code);
    outputEl.innerHTML = '';
    var outputText = '';
    function outf(text) { outputText += text; }
    function builtinRead(x) {
      if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
        throw "File not found: '" + x + "'";
      return Sk.builtinFiles["files"][x];
    }
    Sk.configure({ output: outf, read: builtinRead, __future__: Sk.python3 });
    Sk.misceval.asyncToPromise(function() {
      return Sk.importMainWithBody("<stdin>", false, code, true);
    }).then(function() {
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
      var match = errMsg.match(/line (\\d+)/);
      var lineInfo = match ? ' (sor: ' + match[1] + ')' : '';
      outputEl.innerHTML = '<span class="output-error">Hiba' + lineInfo + ':\\n' + escapeHtml(errMsg) + '</span>';
    });
  };"""
    elif runtime == "jscpp":
        return """
  window.runCode = function(editorId) {
    var editor = document.getElementById(editorId);
    var outputEl = document.getElementById(editorId + '-output');
    var code = editor.value;
    localStorage.setItem('code-' + editorId, code);
    outputEl.innerHTML = '';
    var outputText = '';
    try {
      var exitCode = JSCPP.run(code, "", {
        stdio: {
          write: function(s) { outputText += s; }
        },
        unsigned_overflow: "warn"
      });
      var lines = outputText.split('\\n');
      var html = lines.map(function(line) {
        if (line.indexOf('\\u2713') >= 0 || line.indexOf('OK') >= 0 && line.indexOf('\\u2713') >= 0) {
          return '<span class="output-success">' + escapeHtml(line) + '</span>';
        } else if (line.indexOf('\\u2717') >= 0 || line.indexOf('HIBA') >= 0) {
          return '<span class="output-error">' + escapeHtml(line) + '</span>';
        } else if (line.indexOf('MINDEN FELADAT') >= 0) {
          return '<span class="output-success"><strong>' + escapeHtml(line) + '</strong></span>';
        }
        return escapeHtml(line);
      }).join('\\n');
      outputEl.innerHTML = html;
    } catch(err) {
      var errMsg = err.message || err.toString();
      outputEl.innerHTML = '<span class="output-error">Hiba:\\n' + escapeHtml(errMsg) + '</span>';
    }
  };"""
    return ""


def get_highlighter_js(runtime: str) -> str:
    """Syntax highlighter JS a megfelelo nyelvhez."""
    if runtime == "skulpt":
        return """
  var KW = new Set(['False','None','True','and','as','assert','async','await','break','class','continue','def','del','elif','else','except','finally','for','from','global','if','import','in','is','lambda','nonlocal','not','or','pass','raise','return','try','while','with','yield']);
  var BI = new Set(['print','len','range','int','str','float','list','dict','set','tuple','bool','input','open','type','isinstance','enumerate','zip','map','filter','sorted','reversed','sum','min','max','abs','round','any','all','super','property','staticmethod','classmethod','hasattr','getattr','setattr']);

  function hlCode(code) {
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
  }"""
    elif runtime == "jscpp":
        return """
  var KW = new Set(['auto','bool','break','case','char','class','const','constexpr','continue','default','delete','do','double','else','enum','explicit','extern','false','float','for','friend','goto','if','inline','int','long','mutable','namespace','new','noexcept','nullptr','operator','private','protected','public','register','return','short','signed','sizeof','static','static_cast','struct','switch','template','this','throw','true','try','typedef','typename','union','unsigned','using','virtual','void','volatile','while']);
  var BI = new Set(['cout','cin','endl','cerr','string','vector','map','set','pair','array','sort','push_back','pop_back','size','begin','end','empty','find','insert','erase','swap','getline','stoi','stod','to_string','abs','min','max','pow','sqrt']);

  function hlCode(code) {
    var r = '', i = 0;
    while (i < code.length) {
      // Preprocessor directives
      if (code[i]==='#' && (i===0||code[i-1]==='\\n')) { var e=code.indexOf('\\n',i); if(e===-1)e=code.length; r+='<span class="syn-dec">'+code.slice(i,e)+'</span>'; i=e; continue; }
      // Line comments
      if (code[i]==='/' && i+1<code.length && code[i+1]==='/') { var e=code.indexOf('\\n',i); if(e===-1)e=code.length; r+='<span class="syn-cmt">'+code.slice(i,e)+'</span>'; i=e; continue; }
      // Block comments
      if (code[i]==='/' && i+1<code.length && code[i+1]==='*') { var e=code.indexOf('*/',i+2); if(e===-1)e=code.length; else e+=2; r+='<span class="syn-cmt">'+code.slice(i,e)+'</span>'; i=e; continue; }
      // Strings
      if (code[i]==='"') { var j=i+1; while(j<code.length&&code[j]!=='"'&&code[j]!=='\\n'){if(code[j]==='\\\\')j++;j++;} if(j<code.length&&code[j]==='"')j++; r+='<span class="syn-str">'+code.slice(i,j)+'</span>'; i=j; continue; }
      // Char literals
      if (code[i]==="'") { var j=i+1; while(j<code.length&&code[j]!=="'"&&code[j]!=='\\n'){if(code[j]==='\\\\')j++;j++;} if(j<code.length&&code[j]==="'")j++; r+='<span class="syn-str">'+code.slice(i,j)+'</span>'; i=j; continue; }
      // Numbers
      if (/\\d/.test(code[i])&&(i===0||/[\\s(,=+\\-*/<>\\[\\]:;{}]/.test(code[i-1]))) { var j=i; while(j<code.length&&/[\\d.xXaAbBcCdDeEfFuUlL]/.test(code[j]))j++; r+='<span class="syn-num">'+code.slice(i,j)+'</span>'; i=j; continue; }
      // Identifiers
      if (/[a-zA-Z_]/.test(code[i])) { var j=i; while(j<code.length&&/[a-zA-Z0-9_]/.test(code[j]))j++; var w=code.slice(i,j);
        if(w==='std'||w==='this')r+='<span class="syn-self">'+w+'</span>';
        else if(KW.has(w))r+='<span class="syn-kw">'+w+'</span>';
        else if(BI.has(w))r+='<span class="syn-bi">'+w+'</span>';
        else r+=w; i=j; continue; }
      // << and >> operators (no special highlight)
      r+=code[i]; i++;
    }
    return r;
  }"""
    return ""


# ============================================================
# HTML TEMPLATE
# ============================================================

def get_html_template(tabs: str, panels: str, originals_js: str, config: dict) -> str:
    """Returns the complete HTML template with content inserted."""

    title = config["title"]
    runtime = config["runtime"]
    runtime_scripts = get_runtime_scripts(runtime)
    run_code_js = get_run_code_js(runtime)
    highlighter_js = get_highlighter_js(runtime)

    part1 = f"""<!DOCTYPE html>
<html lang="hu" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<title>{html.escape(title)}</title>
<style>
:root {{
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
}}

[data-theme="light"] {{
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
}}

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ font-size: var(--font-size); -webkit-text-size-adjust: 100%; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
  background: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.6;
  min-height: 100vh;
  padding-bottom: 70px;
}}

.topbar {{
  position: sticky; top: 0; z-index: 100;
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border);
  padding: 8px 16px;
  display: flex; align-items: center; justify-content: space-between; gap: 8px;
  -webkit-backdrop-filter: blur(10px); backdrop-filter: blur(10px);
}}
.topbar h1 {{ font-size: 1rem; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; flex: 1; }}
.topbar-controls {{ display: flex; gap: 4px; flex-shrink: 0; }}
.topbar-btn {{
  background: var(--bg-card); color: var(--text-primary);
  border: 1px solid var(--border); border-radius: 8px;
  padding: 6px 10px; font-size: 1rem; cursor: pointer;
  min-width: 40px; min-height: 40px;
  display: flex; align-items: center; justify-content: center;
  -webkit-tap-highlight-color: transparent;
}}
.topbar-btn:active {{ background: var(--bg-card-hover); }}

.content {{ max-width: 800px; margin: 0 auto; padding: 16px; }}
.file-content {{ animation: fadeIn 0.2s ease; }}
@keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}

.file-header {{ margin-bottom: 24px; padding-bottom: 16px; border-bottom: 2px solid var(--border); }}
.file-header h2 {{ font-size: 1.4rem; font-weight: 700; margin: 8px 0 4px; }}
.filename {{ font-family: 'SF Mono', 'Menlo', 'Monaco', 'Courier New', monospace; font-size: 0.8rem; color: var(--text-muted); }}

.badge {{ display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }}
.badge.lesson {{ background: var(--accent-green); color: #1e1e2e; }}
.badge.exercise {{ background: var(--accent-yellow); color: #1e1e2e; }}

.section {{ margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--border); }}
.section:last-child {{ border-bottom: none; }}
.section h3 {{ font-size: 1.1rem; font-weight: 700; color: var(--accent); margin: 16px 0 8px; }}
.section p {{ color: var(--text-secondary); margin-bottom: 12px; line-height: 1.7; }}
.section strong {{ color: var(--text-primary); }}

code.inline {{
  font-family: 'SF Mono', 'Menlo', 'Monaco', 'Courier New', monospace;
  background: var(--bg-card); padding: 2px 6px; border-radius: 4px;
  font-size: 0.9em; color: var(--accent-peach);
}}
pre.box {{
  font-family: 'SF Mono', 'Menlo', 'Monaco', 'Courier New', monospace;
  background: var(--bg-card); border: 1px solid var(--accent);
  border-radius: 8px; padding: 12px 16px; margin: 12px 0;
  font-size: 0.85rem; overflow-x: auto; line-height: 1.5; color: var(--accent);
}}
pre.code-block {{
  background: var(--bg-surface); border: 1px solid var(--border);
  border-radius: 10px; padding: 14px 16px; margin: 12px 0;
  overflow-x: auto; -webkit-overflow-scrolling: touch;
  font-size: 0.85rem; line-height: 1.6;
}}
pre.code-block code {{
  font-family: 'SF Mono', 'Menlo', 'Monaco', 'Courier New', monospace;
  color: var(--text-primary);
}}
.syn-kw {{ color: var(--syn-keyword); font-weight: 500; }}
.syn-str {{ color: var(--syn-string); }}
.syn-cmt {{ color: var(--syn-comment); font-style: italic; }}
.syn-num {{ color: var(--syn-number); }}
.syn-bi {{ color: var(--syn-builtin); }}
.syn-dec {{ color: var(--syn-decorator); }}
.syn-self {{ color: var(--syn-self); }}

/* ============ EXERCISE EDITOR ============ */
.exercise-editor {{ margin-top: 8px; }}

.editor-toolbar {{
  display: flex; gap: 8px; margin-bottom: 8px;
}}

.run-btn {{
  background: var(--accent-green); color: #1e1e2e;
  border: none; border-radius: 8px;
  padding: 10px 20px; font-size: 1rem; font-weight: 700;
  cursor: pointer; min-height: 44px;
  -webkit-tap-highlight-color: transparent;
  flex: 1;
}}
.run-btn:active {{ opacity: 0.8; }}
.run-btn.running {{ background: var(--accent-yellow); }}

.reset-btn {{
  background: var(--bg-card); color: var(--text-secondary);
  border: 1px solid var(--border); border-radius: 8px;
  padding: 10px 16px; font-size: 0.9rem;
  cursor: pointer; min-height: 44px;
  -webkit-tap-highlight-color: transparent;
}}
.reset-btn:active {{ background: var(--bg-card-hover); }}

.code-editor {{
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
}}
.code-editor:focus {{
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}}

.output-area {{
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
}}
.output-placeholder {{ color: var(--text-muted); font-style: italic; }}
.output-error {{ color: var(--accent-red); }}
.output-success {{ color: var(--accent-green); }}

/* ============ BOTTOM NAV ============ */
.bottom-nav {{
  position: fixed; bottom: 0; left: 0; right: 0; z-index: 100;
  background: var(--bg-secondary);
  border-top: 1px solid var(--border);
  display: flex; overflow-x: auto; -webkit-overflow-scrolling: touch;
  padding: 4px 4px calc(4px + env(safe-area-inset-bottom));
  gap: 2px; scrollbar-width: none;
}}
.bottom-nav::-webkit-scrollbar {{ display: none; }}

.tab {{
  flex-shrink: 0; background: transparent; color: var(--text-muted);
  border: none; border-radius: 8px;
  padding: 10px 14px; font-size: 0.8rem; font-weight: 500;
  cursor: pointer; white-space: nowrap; min-height: 44px;
  -webkit-tap-highlight-color: transparent; transition: all 0.15s ease;
}}
.tab.active {{ background: var(--accent); color: #1e1e2e; font-weight: 700; }}
.tab:not(.active):active {{ background: var(--bg-card); color: var(--text-primary); }}

/* ============ ACCORDION ============ */
.accordion {{
  margin-top: 24px;
  border: 2px solid var(--accent-yellow);
  border-radius: 12px;
  overflow: hidden;
}}
.accordion-toggle {{
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
}}
.accordion-toggle:active {{ background: var(--bg-card-hover); }}
.accordion-arrow {{ transition: transform 0.2s ease; font-size: 0.8rem; }}
.accordion-toggle.open .accordion-arrow {{ transform: rotate(180deg); }}
.accordion-content {{
  padding: 16px;
  border-top: 1px solid var(--border);
}}

/* ============ TASK CARDS ============ */
.task-card {{
  margin-bottom: 24px;
  padding: 16px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
}}
.task-card:last-child {{ margin-bottom: 0; }}
.task-header h3 {{
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--accent);
  margin-bottom: 8px;
}}
.task-desc {{
  color: var(--text-secondary);
  line-height: 1.7;
  margin-bottom: 12px;
}}
.task-desc strong {{ color: var(--text-primary); }}
.task-hint {{
  margin-bottom: 12px;
  background: var(--bg-surface);
  border-radius: 8px;
  padding: 2px 12px;
}}
.task-hint summary {{
  cursor: pointer;
  padding: 8px 0;
  color: var(--accent-yellow);
  font-weight: 600;
  font-size: 0.9rem;
  -webkit-tap-highlight-color: transparent;
}}
.task-hint p {{
  padding: 0 0 10px 0;
  color: var(--text-muted);
  font-size: 0.9rem;
  line-height: 1.6;
}}

.scroll-top {{
  position: fixed; bottom: 80px; right: 16px;
  background: var(--accent); color: #1e1e2e;
  border: none; border-radius: 50%;
  width: 44px; height: 44px; font-size: 1.2rem;
  cursor: pointer; display: none;
  align-items: center; justify-content: center;
  box-shadow: 0 2px 8px var(--shadow); z-index: 90;
  -webkit-tap-highlight-color: transparent;
}}
</style>
</head>
<body>

<div class="topbar">
  <h1 id="current-title">{html.escape(title)}</h1>
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

    part3 = f"""
</nav>

<button class="scroll-top" id="scroll-top" title="Fel">&uarr;</button>

{runtime_scripts}
<script>
(function() {{
"""

    js_code = originals_js + """

  // ---- Accordion toggle ----
  window.toggleAccordion = function(btn) {
    var content = btn.nextElementSibling;
    var isOpen = content.style.display !== 'none';
    content.style.display = isOpen ? 'none' : 'block';
    btn.classList.toggle('open', !isOpen);
  };

  // ---- Code runner ----
""" + run_code_js + """

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

    editor.addEventListener('input', function() {
      localStorage.setItem('code-' + this.id, this.value);
    });

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

  // ---- Syntax highlighting ----
""" + highlighter_js + """

  document.querySelectorAll('pre.code-block code').forEach(function(el) {
    el.innerHTML = hlCode(el.textContent);
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
"""

    part4 = """
})();
</script>
</body>
</html>"""

    return part1 + panels + part2 + tabs + part3 + js_code + part4


# ============================================================
# FUTTATAS
# ============================================================

def main():
    for config in MODULES:
        exercises_dir = config["dir"]
        if not exercises_dir.exists():
            print(f"\u26a0\ufe0f  Modul kihagyva (mappa nem letezik): {exercises_dir}")
            continue

        pairs = discover_files(exercises_dir, config["ext"], config["short_names"])
        if not pairs:
            print(f"\u26a0\ufe0f  Modul kihagyva (nincs {config['ext']} fajl): {exercises_dir}")
            continue

        print(f"\n\U0001f4da {config['title']} ({len(pairs)} lecke):")
        for pair in pairs:
            lesson = pair["lesson"]
            exercises = pair["exercises"]
            print(f"  \U0001f4d6 {lesson['filename']} \u2014 {lesson['title']}")
            for ex in exercises:
                print(f"    \u270f\ufe0f {ex['filename']}")

        html_content = generate_html(pairs, config)
        output_file = config["output"]
        output_file.write_text(html_content, encoding="utf-8")

        size_kb = output_file.stat().st_size / 1024
        print(f"  \u2705 Generalva: {output_file.name} ({size_kb:.0f} KB)")

    print(f"\n\U0001f4a1 Nyisd meg bongeszobben, vagy kuldd at a telefonodra.")


if __name__ == "__main__":
    main()
