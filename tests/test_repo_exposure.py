"""B1: every root-level folder/file must be in .assetsignore unless it is an intended public asset."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = {"assets", "demo", "privacidade", "termos", "404.html", "config.js", "favicon.svg", "index.html",
          "robots.txt", "sitemap.xml", "_headers"}


def test_no_unlisted_root_entries_are_served():
    ignored = {l.strip().rstrip("/") for l in (ROOT / ".assetsignore").read_text(encoding="utf-8-sig").splitlines() if l.strip()}
    exposed = [p.name for p in ROOT.iterdir() if p.name not in ignored and p.name not in PUBLIC]
    assert exposed == [], f"served publicly but not declared public: {exposed}"


def test_env_is_gitignored_and_ignored_by_assets():
    gi = (ROOT / ".gitignore").read_text(encoding="utf-8-sig").split()
    ai = (ROOT / ".assetsignore").read_text(encoding="utf-8-sig").split()
    assert ".env" in gi and ".env" in ai
