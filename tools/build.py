"""Build Maths and English practice as a web site or self-contained HTML."""
import argparse
import base64
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "generator"


def run(script):
    subprocess.run([sys.executable, "-X", "utf8", script], cwd=GEN, check=True,
                   env={**os.environ, "PYTHONUTF8": "1"})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--standalone", action="store_true",
                        help="Keep self-contained HTML in generator/out/{Toan5,TiengAnh5}; do not update site")
    parser.add_argument("--regenerate", action="store_true",
                        help="Regenerate available Python question sources (topics 4-6)")
    args = parser.parse_args()
    if args.regenerate:
        for script in sorted(GEN.glob("g[456]_de*.py")):
            run(script.name)
    for script in ("build_all.py", "gen_overview.py", "gen_index.py", "gen_english.py"):
        run(script)
    if args.standalone:
        print("Standalone:", GEN / "out", "(Toan5, TiengAnh5)")
        return
    site = ROOT / "site"
    assets = site / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    resources = {name: (GEN / name).read_text(encoding="utf-8")
                 for name in ("fonts.css", "engine.css", "engine.js", "overview.css", "overview.js")}
    for name, data in resources.items():
        (assets / name).write_text(data, encoding="utf-8", newline="\n")
    english_resources={name:(GEN/'english'/name).read_text(encoding='utf-8-sig') for name in ['theme.css','theme.js','speech.js']}
    for name,data in english_resources.items():
        target=assets/'english'/name
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(data,encoding='utf-8',newline='\n')
    illustrations = {}
    for source in sorted((GEN / "english" / "u01" / "images").glob("*.webp")):
        relative = Path("english") / "u01" / source.name
        target = assets / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        illustrations["data:image/webp;base64," + base64.b64encode(source.read_bytes()).decode("ascii")] = relative.as_posix()
    sources=[p for subject in ("Toan5", "TiengAnh5") for p in (GEN / "out" / subject).rglob("*.html")]
    for source in sources:
        relative = source.relative_to(GEN / "out")
        target = site / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        prefix = "../" * (len(relative.parts) - 1) + "assets/"
        html = source.read_text(encoding="utf-8")
        html = html.replace("<style>" + resources["fonts.css"] + "</style>",
                            f'<link rel="stylesheet" href="{prefix}fonts.css">')
        if source.name.startswith("De"):
            html = html.replace("<style>\n" + resources["engine.css"] + "\n</style>",
                                f'<link rel="stylesheet" href="{prefix}engine.css">')
            if html.count(resources["engine.js"]) != 1:
                raise ValueError(f"Engine extraction failed: {source}")
            html = html.replace(resources["engine.js"], "")
            html = html.replace("</script></body>",
                                f'</script><script src="{prefix}engine.js"></script></body>')
        elif source.name == "index.html":
            html = html.replace('<p class="eyebrow">',
                                '<a class="subject-back" href="../index.html">← Chọn môn học</a><p class="eyebrow">', 1)
        else:
            html = html.replace("<style>" + resources["overview.css"] + "</style>",
                                f'<link rel="stylesheet" href="{prefix}overview.css">')
            html = html.replace("<script>" + resources["overview.js"] + "</script>",
                                f'<script src="{prefix}overview.js"></script>')
        for name,data in english_resources.items():
            embedded=('<style>'+data+'</style>') if name.endswith('.css') else ('<script>'+data+'</script>')
            external=f'<link rel="stylesheet" href="{prefix}english/{name}">' if name.endswith('.css') else f'<script src="{prefix}english/{name}"></script>'
            html=html.replace(embedded,external)
        for embedded, image_path in illustrations.items():
            html = html.replace(embedded, prefix + image_path)
        if resources["fonts.css"] in html:
            raise ValueError(f"Font extraction failed: {source}")
        target.write_text(html, encoding="utf-8", newline="\n")
    # Keep PNGs for HTML-only builds; the Node entry point then regenerates them.
    for source in site.rglob("*.png"):
        target = GEN / "out" / source.relative_to(site)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    home = (ROOT / "tools" / "templates" / "home.html").read_text(encoding="utf-8")
    (site / "index.html").write_text(home, encoding="utf-8", newline="\n")
    import json
    sys.path.insert(0,str(GEN))
    from cfg import CDS
    from english.u01.content import TESTS
    tests=[dict(file=f"Toan5/{cd['dir']}/De{i}_{slug}.html",id=f"cd{cd['n']}-de{i}",subject='math')
           for cd in CDS for i,(slug,*_) in enumerate(cd['tests'],1)]
    tests += [dict(file=f"TiengAnh5/Unit1_AllAboutMe/De{i}_{slug}.html",id=f"en-u01-de{i}-v2",subject='en')
              for i,(slug,*_) in enumerate(TESTS,1)]
    (site / "catalog.json").write_text(json.dumps(dict(tests=tests),ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    (site / ".nojekyll").touch()
    print("Web:", site)
    print("HTML/assets ready. Use node tools/build.js for a complete build including PNG posters.")


if __name__ == "__main__":
    main()
