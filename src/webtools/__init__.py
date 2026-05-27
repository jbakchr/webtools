from .fetch import fetch_html, fetch_web_text, fetch_and_clean
from .clean import clean_text, truncate_text

__all__ = [
    "fetch_html",
    "fetch_web_text",
    "fetch_and_clean",   # ✅ add this
    "clean_text",
    "truncate_text",
]