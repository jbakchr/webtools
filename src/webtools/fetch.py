import trafilatura

from .clean import clean_text, truncate_text

def fetch_html(url: str) -> str:
    """
    Fetch raw HTML from a URL.

    Args:
        url: URL to fetch

    Returns:
        Raw HTML as string

    Raises:
        ValueError: If download fails
    """
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        raise ValueError(f"Failed to download content from {url}")

    return downloaded


def fetch_web_text(url: str, output_format: str = "markdown") -> str:
    """
    Fetch and extract main content from a web page.

    Args:
        url: URL to fetch
        output_format: Output format (e.g. 'markdown', 'txt')

    Returns:
        Extracted text

    Raises:
        ValueError: If extraction fails
    """
    html = fetch_html(url)

    extracted = trafilatura.extract(html, output_format=output_format)
    if not extracted:
        raise ValueError(f"Failed to extract content from {url}")

    return extracted



def fetch_and_clean(url: str, output_format: str = "markdown") -> str:
    """
    Fetch, extract, and clean web content in one step.

    Args:
        url: URL to fetch
        output_format: Output format for extraction

    Returns:
        Cleaned extracted text
    """
    text = fetch_web_text(url, output_format=output_format)
    return clean_text(text)


def fetch_and_prepare(
    url: str,
    output_format: str = "markdown",
    max_chars: int | None = None,
) -> str:
    """
    Full pipeline: fetch → extract → clean → optional truncate

    Args:
        url: URL to fetch
        output_format: Output format for extraction
        max_chars: If set, truncate to this length. If None, no truncation.

    Returns:
        Cleaned (and optionally truncated) text
    """
    text = fetch_web_text(url, output_format=output_format)
    text = clean_text(text)

    if max_chars is not None:
        text = truncate_text(text, max_chars=max_chars)

    return text
