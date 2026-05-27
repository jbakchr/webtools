import trafilatura


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