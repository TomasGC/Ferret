"""
Workday job board API.

No single stable public endpoint like Greenhouse/Lever — each tenant exposes an
internal JSON API at a path like:
  POST https://{tenant}.wd{n}.myworkdayjobs.com/wday/cxs/{tenant}/{site}/jobs

Both `tenant`/`wd{n}`/`site` need to be found per-company by inspecting network
requests on their myworkdayjobs.com careers page (varies per company — there's no
single guessable pattern). Store whatever's needed to hit it in `ats_token`
(e.g. as a JSON blob or a "tenant/site" string — decide the shape when you build this).
"""


def fetch_offers(ats_token: str) -> list[dict]:
    # TODO: figure out the exact request shape per company, POST it, map the
    # response's job entries into the shared offer shape.
    raise NotImplementedError
