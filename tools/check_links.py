"""Check local HTML/CSS references with exact case, including on Windows."""
from html.parser import HTMLParser
from pathlib import Path
import posixpath
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        self.urls.extend(value for name, value in attrs if name in ("href", "src") and value)


def validate(site):
    files = {p.relative_to(site).as_posix() for p in site.rglob("*") if p.is_file()}
    errors = []
    checked = 0
    for source in sorted(site.rglob("*")):
        if source.suffix not in (".html", ".css"):
            continue
        text = source.read_text(encoding="utf-8")
        if source.suffix == ".html":
            parser = References()
            parser.feed(text)
            urls = parser.urls
        else:
            urls = re.findall(r"url\(['\"]?([^)'\"]+)", text)
        for url in urls:
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            checked += 1
            if parsed.path.startswith("/") or "\\" in parsed.path:
                errors.append(f"{source.relative_to(site)}: non-relative URL {url}")
                continue
            target = posixpath.normpath((source.parent.relative_to(site) / unquote(parsed.path)).as_posix())
            if (site / target).is_dir():
                target = target.rstrip("/") + "/index.html"
            if target not in files:
                errors.append(f"{source.relative_to(site)}: missing or wrong case: {url}")
    errors.extend(f"Forbidden book file: {p}" for p in site.rglob("*.pdf"))
    print(f"Links: {checked} references; {len(errors)} issues")
    for error in errors:
        print(error)
    return errors


if __name__ == "__main__":
    sys.exit(bool(validate(Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT / "site")))
