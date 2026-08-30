"""
Entrypoint called by .github/workflows/daily-scrape.yml.

TODO:
  1. Query companies that have at least one follower and ats_platform != NONE.
  2. Dispatch each to the matching module in app/scrapers/ (by ats_platform).
  3. Upsert results into `offers`, ON CONFLICT (company_id, url) DO UPDATE.
See ARCHITECTURE.md "Scraper" section.
"""

if __name__ == "__main__":
    raise NotImplementedError
