# webtools — Roadmap

A lightweight personal toolkit for fetching, extracting, and preparing web content for AI workflows.

---

## 🎯 Vision

`webtools` is a minimal, composable "web ingestion layer" designed to:

- Reduce friction when working with web content
- Provide clean, ready-to-use inputs for AI tools
- Standardize how I fetch, clean, and process content across projects

Primary use cases:

- Job scraping (skim-job-ai)
- Article summarization (drdk-ai, docsum)
- Dataset creation and RAG pipelines (iso-ask)
- General automation and experimentation

---

## 🧱 Design Principles

- **Minimal first** — only add features when needed
- **Composable functions** — small building blocks over monolithic functions
- **No "utils dumping ground"** — organize by capability
- **Local-first friendly** — no unnecessary external dependencies
- **Fast iteration** — optimized for real-world usage, not theoretical completeness

---

## ✅ Current State (v0.1)

### fetch.py

- `fetch_web_text(url: str, output_format="markdown") -> str`

Core functionality:

- Fetch URL
- Extract main content via `trafilatura`
- Return clean text

---

## 🧭 Phase 1 — Foundation (Next Steps)

Goal: Build a minimal but flexible base

### fetch.py

- [ ] `fetch_html(url: str) -> str`
  - Raw HTML download

### clean.py

- [ ] `clean_text(text: str) -> str`
  - Normalize whitespace
  - Remove noise artifacts

- [ ] `truncate_text(text: str, max_chars: int) -> str`
  - Prepare text for LLM input

---

## 🧭 Phase 2 — Better Extraction

Goal: Improve usefulness for real-world data workflows

### extract.py (new)

- [ ] `extract_text(html: str, output_format="markdown") -> str`
- [ ] `extract_metadata(html: str) -> dict`
  - title, author, date, etc.

### fetch.py

- [ ] Refactor `fetch_web_text` to:
  - `fetch_html` → `extract_text`

---

## 🧭 Phase 3 — Data Workflows (RAG / pipelines)

Goal: Enable batch processing and dataset creation

### batch.py (new)

- [ ] `fetch_many(urls: list[str]) -> list[str]`
- [ ] `fetch_and_extract(urls: list[str]) -> list[str]`

Optional:

- [ ] `fetch_to_dataset(urls: list[str]) -> list[dict]`

---

## 🧭 Phase 4 — Reliability Layer

Goal: Make scraping more robust in real usage

### fetch.py

- [ ] `fetch_with_retry(url: str, retries=3)`
- [ ] Add error handling patterns

### (optional later)

- [ ] caching layer
  - disk or in-memory caching

---

## 🧭 Phase 5 — URL & Link Utilities

Goal: Support crawling / filtering workflows

### links.py (new)

- [ ] `is_valid_url(url: str) -> bool`
- [ ] `normalize_url(url: str) -> str`
- [ ] `extract_domain(url: str) -> str`
- [ ] `filter_links(links: list[str], domain: str) -> list[str]`

---

## 🧭 Phase 6 — Advanced (Only if needed)

Goal: Add sophistication without killing simplicity

### ideas

- [ ] language detection
- [ ] content deduplication
- [ ] HTML → Markdown normalization improvements
- [ ] streaming / async fetch (only if needed)

---

## 🚫 Non-Goals (Important)

To avoid scope creep:

- No general-purpose "utils" dumping
- No full crawler framework
- No database layer
- No overengineering early

---

## 🧠 Long-Term Direction

`webtools` becomes:

→ A stable internal dependency used across:

- microsteps-ai
- skim-job-ai
- drdk-ai
- iso-ask

→ A consistent way to:

- fetch → clean → prepare → feed into LLMs

---

## 🧪 Development Style

- Build → use → refine
- Add features only after real usage
- Track improvements via FEEDBACK.md (when relevant)

---

## ✅ Summary

This is not meant to be a "big library".

It is a **small, reliable, evolving toolkit** that reduces friction across projects and compounds in value over time.
