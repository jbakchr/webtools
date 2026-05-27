from typing import List


def clean_text(text: str) -> str:
    """
    Normalize text for downstream usage (LLMs, storage, etc.)

    - Removes excessive whitespace
    - Normalizes line breaks

    Args:
        text: Raw text

    Returns:
        Cleaned text
    """
    if not text:
        return ""

    # Collapse all whitespace into single spaces
    cleaned = " ".join(text.split())

    return cleaned


def truncate_text(text: str, max_chars: int = 2000) -> str:
    """
    Truncate text to a maximum length.

    Useful for LLM inputs and quick previews.

    Args:
        text: Input text
        max_chars: Maximum number of characters (default: 2000)

    Returns:
        Truncated text
    """
    if not text:
        return ""

    return text[:max_chars]


def chunk_text(
    text: str,
    max_chars: int = 1000,
    preserve_sentences: bool = False,
) -> List[str]:
    """
    Split text into chunks of a maximum character size.

    Args:
        text: Input text
        max_chars: Maximum characters per chunk
        preserve_sentences: If True, try to split on paragraph boundaries

    Returns:
        List of text chunks
    """
    if not text:
        return []

    # ✅ SIMPLE VERSION (V1)
    if not preserve_sentences:
        return [
            text[i : i + max_chars]
            for i in range(0, len(text), max_chars)
        ]

    # ✅ SENTENCE-AWARE VERSION (V2)
    paragraphs = text.split("\n\n")

    chunks: List[str] = []
    current_chunk = ""

    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:
            continue

        # If paragraph alone is too big → fallback to simple split
        if len(paragraph) > max_chars:
            if current_chunk:
                chunks.append(current_chunk.strip())
                current_chunk = ""

            chunks.extend(
                [
                    paragraph[i : i + max_chars]
                    for i in range(0, len(paragraph), max_chars)
                ]
            )
            continue

        # Try to add paragraph to current chunk
        if len(current_chunk) + len(paragraph) + 2 <= max_chars:
            if current_chunk:
                current_chunk += "\n\n"
            current_chunk += paragraph
        else:
            # Save current chunk and start new
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = paragraph

    # Add last chunk
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks



def is_valid_url(url: str) -> bool:
    """
    Basic URL validation.

    Args:
        url: URL string

    Returns:
        True if valid HTTP(S) URL
    """
    return isinstance(url, str) and url.startswith(("http://", "https://"))