"""Serve the site at the same /Lop_5_Mia/ prefix as GitHub Pages."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse

ROOT = Path(__file__).resolve().parents[1] / "site"


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path == "/":
            self.send_response(302)
            self.send_header("Location", "/Lop_5_Mia/")
            self.end_headers()
            return
        if not self.path.startswith("/Lop_5_Mia/"):
            self.send_error(404)
            return
        self.path = self.path[len("/Lop_5_Mia"):]
        current = ROOT
        for part in unquote(urlsplit(self.path).path).strip("/").split("/"):
            if not part:
                continue
            if part in (".", "..") or not current.is_dir() or part not in {p.name for p in current.iterdir()}:
                self.send_error(404)
                return
            current /= part
        super().do_GET()


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port",type=int,default=8765)
    args=parser.parse_args()
    print(f"Local: http://127.0.0.1:{args.port}/Lop_5_Mia/",flush=True)
    ThreadingHTTPServer(("127.0.0.1",args.port),Handler).serve_forever()
