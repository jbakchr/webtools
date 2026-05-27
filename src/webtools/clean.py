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
        max_chars: Maximum number of characters

    Returns:
        Truncated text
    """
    if not text:
        return ""

    return text[:max_chars]