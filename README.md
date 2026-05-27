# webtools

> **Zero-friction web → clean text pipeline for building AI tools and automation.**

A minimal Python toolkit for extracting and preparing clean text from the web.

---

## 💡 Why this exists

Working with web data is messy:

- HTML is noisy ..
- Content extraction is inconsistent ..
- Text is rarely usable out-of-the-box ..

This package solves that:

👉 **Fetch → Extract → Clean → Prepare → Chunk**

So you can focus on building real applications instead of fighting raw web data.

---

## ✨ Features

- Fetch raw HTML from URLs
- Extract readable content from web pages
- Clean text (normalize whitespace)
- Truncate text safely
- Chunk text for large inputs

---

## 🧠 Mental Model

```

URL
↓
fetch
↓
extract
↓
clean
↓
(optional) truncate
↓
(optional) chunk

```

---

## 🚀 Installation

### Local (development)

```bash
pip install -e .
```

### From Git

```bash
pip install git+https://github.com/jbakchr/webtools.git
```

---

## 📦 Usage

### 1. Fetch raw HTML

```python
from webtools import fetch_html

html = fetch_html("https://example.com")
print(html[:200])
```

---

### 2. Extract readable web text

```python
from webtools import fetch_web_text

text = fetch_web_text("https://example.com")
print(text)
```

---

### 3. Fetch + clean

```python
from webtools import fetch_and_clean

text = fetch_and_clean("https://example.com")
```

---

### 4. Fetch + prepare (LLM-ready)

```python
from webtools import fetch_and_prepare

text = fetch_and_prepare("https://example.com", max_chars=2000)
```

👉 Set `max_chars=None` to avoid truncation

---

### 5. Clean text

```python
from webtools import clean_text

cleaned = clean_text("This   is   messy   text")
# "This is messy text"
```

---

### 6. Truncate text

```python
from webtools import truncate_text

short_text = truncate_text(text, max_chars=500)
```

---

### 7. Chunk text (for large inputs)

#### Simple chunking

```python
from webtools import chunk_text

chunks = chunk_text(text, max_chars=1000)
```

#### Structure-aware chunking (recommended)

```python
chunks = chunk_text(
    text,
    max_chars=1000,
    preserve_sentences=True
)
```

✅ Keeps paragraphs intact when possible  
✅ Falls back to simple splitting when needed

---

### 8. Validate URLs

```python
from webtools import is_valid_url

is_valid_url("https://example.com")  # True
is_valid_url("invalid-url")          # False
```

---

## 🧩 When to use what?

| Task                         | Function            |
| ---------------------------- | ------------------- |
| Fetch webpage text           | `fetch_web_text`    |
| Clean + usable text          | `fetch_and_clean`   |
| Prepare for pipelines / LLMs | `fetch_and_prepare` |
| Handle large content safely  | `chunk_text`        |

---

## 🛠️ Real-world usage

Used across practical tools:

- Job summarizers
- News/article summarizers
- LLM pipelines
- Automation scripts

Example:

```python
from webtools import fetch_and_prepare, chunk_text

text = fetch_and_prepare(url)
chunks = chunk_text(text, preserve_sentences=True)

for chunk in chunks:
    process(chunk)
```

---

## 🧭 Design Principles

- ✅ Minimal and focused
- ✅ Explicit behavior (no hidden data loss)
- ✅ Composable functions
- ✅ Built from real usage

---

## 📁 Project Structure

```
src/webtools/
├── fetch.py      # Fetch + extract web content
├── clean.py      # Text cleaning, truncation, chunking
└── __init__.py   # Public API

Other files:
- README.md
- ROADMAP.md
- FEEDBACK.md
```

---

## 🔗 Part of a larger ecosystem

`webtools` is part of a growing set of personal tools:

- `webtools` → web → clean text
- future → LLM tooling, automation pipelines

---

## ⚠️ Notes

- `fetch_web_text` uses `trafilatura`
- `chunk_text(preserve_sentences=True)` uses paragraph-based splitting
- No data is truncated unless explicitly requested

---

## 🛣️ Philosophy

This package is intentionally:

- Small
- Predictable
- Explicit
- Focused

No LLM logic — just **data preparation**

---

## 📌 Roadmap

See `ROADMAP.md`

---

## 📝 Feedback

See `FEEDBACK.md`

## 📚 License

MIT
