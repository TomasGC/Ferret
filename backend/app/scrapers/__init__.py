from typing import Protocol


class ScrapedOffer(Protocol):
    title: str
    description: str
    url: str
    posted_at: str | None


class AtsScraper(Protocol):
    """Common interface every per-ATS scraper module implements."""

    def fetch_offers(self, ats_token: str) -> list[ScrapedOffer]:
        ...
