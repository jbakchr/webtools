# webtools — Roadmap

A lightweight toolkit for turning web pages into clean, usable text.

---

## 🎯 Vision

`webtools` is a minimal “web ingestion layer” designed to:

- Reduce friction when working with web content
- Provide clean, ready-to-use inputs for downstream processing
- Standardize how content is fetched and prepared across projects

---

## ✅ Current State (v0.2)

The package now provides a complete pipeline:

```

URL → fetch → extract → clean → prepare → chunk

```

### Core functions

#### Fetch + extract

- `fetch_html(url)` → raw HTML
- `fetch_web_text(url)` → extracted readable content

#### Composed helpers

- `fetch_and_clean(url)`
- `fetch_and_prepare(url, max_chars=None)`

#### Text processing

- `clean_text(text)`
- `truncate_text(text, max_chars)`

#### Chunking

- `chunk_text(text, max_chars, preserve_sentences=False)`
  - Simple chunking
  - Paragraph-aware chunking (when enabled)

#### Utilities

- `is_valid_url(url)`

---

## 🧭 Design Principles

- ✅ **Minimal first** — add features only when needed
- ✅ **Composable functions** — small building blocks
- ✅ **Explicit behavior** — no hidden data loss
- ✅ **No scope creep** — stay focused on web → text
- ✅ **Built from real usage** — evolve from actual needs

---

## 🛠️ Real Usage Context

This package is used in:

- Job scraping tools (skim-job-ai)
- Article summarization tools (drdk-ai, docsum)
- Data preparation for LLM workflows
- General automation scripts

---

## 🧠 How the project evolves

Instead of fixed phases, development follows:

> **Build → use → observe → refine**

New functionality is added only when:

- repeated friction appears
- something cannot be solved cleanly with existing functions

---

## 🔮 Possible future improvements (only if needed)

These are **optional directions**, not commitments:

### Better chunking

- Sentence-aware splitting (beyond paragraphs)
- Overlap between chunks

### Metadata extraction

- title, author, publish date

### URL utilities

- domain extraction
- URL normalization

### Reliability

- retry logic
- caching

---

## 🚫 Non-Goals (Important)

To avoid turning this into a “utils dump”:

- ❌ No full crawling framework
- ❌ No database layer
- ❌ No LLM-specific logic
- ❌ No premature abstraction

---

## 🧩 Long-term role

`webtools` is intended to become:

> ✅ **A stable, reusable dependency used across projects**

Providing a consistent way to:

```

fetch → clean → prepare → process

```

---

## 📝 Development Style

- Build small, test in real usage
- Prefer clarity over cleverness
- Add functionality only when necessary
- Track learnings in `FEEDBACK.md`

---

## ✅ Summary

This is not a “big library”.

It is a:

> **Small, reliable toolkit that removes friction and compounds in value over time.**
