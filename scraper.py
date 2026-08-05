"""
Unified Scraper
Faculty & Research Vacancy Tracker
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from config import SOURCES, REQUEST_TIMEOUT, USER_AGENT


HEADERS = {
    "User-Agent": USER_AGENT
}


CAREER_KEYWORDS = [
    "career",
    "careers",
    "job",
    "jobs",
    "vacancy",
    "vacancies",
    "recruitment",
    "faculty",
    "teaching",
    "employment",
    "opportunities",
    "position",
    "positions"
]


def download_page(url):
    """
    Download webpage.
    """

    try:

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        return response.text

    except Exception as e:

        print(f"Failed: {url}")

        print(e)

        return None


def find_career_pages(base_url, html):
    """
    Discover recruitment pages automatically.
    """

    soup = BeautifulSoup(html, "lxml")

    pages = set()

    for link in soup.find_all("a", href=True):

        href = link["href"]

        text = link.get_text(" ", strip=True).lower()

        full_url = urljoin(base_url, href)

        combined = f"{href.lower()} {text}"

        if any(word in combined for word in CAREER_KEYWORDS):

            pages.add(full_url)

    return sorted(list(pages))


def scan_source(source):

    print(f"Scanning {source['name']}")

    html = download_page(source["url"])

    if html is None:

        return []

    career_pages = find_career_pages(
        source["url"],
        html
    )

    return career_pages