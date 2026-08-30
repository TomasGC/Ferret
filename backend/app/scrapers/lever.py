"""
Lever job board API.

Public JSON endpoint, no auth needed:
  GET https://api.lever.co/v0/postings/{ats_token}?mode=json

`ats_token` is the company's Lever slug (find it in their careers URL,
e.g. jobs.lever.co/<token>).
"""


def fetch_offers(ats_token: str) -> list[dict]:
    # TODO: httpx.get the endpoint above, map each posting's `text` (title),
    # `descriptionPlain`, `hostedUrl`, `createdAt` into the shared offer shape.
    raise NotImplementedError
