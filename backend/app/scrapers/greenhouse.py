"""
Greenhouse job board API.

Public JSON endpoint, no auth needed:
  GET https://boards-api.greenhouse.io/v1/boards/{ats_token}/jobs?content=true

`ats_token` is the company's Greenhouse board slug (find it in their careers URL,
e.g. boards.greenhouse.io/<token>).
"""


def fetch_offers(ats_token: str) -> list[dict]:
    # TODO: httpx.get the endpoint above, map each job's `title`, `content` (HTML
    # description), `absolute_url`, `updated_at` into the shared offer shape.
    raise NotImplementedError
