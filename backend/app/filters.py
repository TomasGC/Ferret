"""
Criteria filtering logic, ported from Engine/JobFilterEngine.kt.

Original Kotlin version filtered on a single global criteria.json (allowed_job_names,
forbidden_languages, forbidden_domains). Here it's per-user: same three rules, but
sourced from a user's `Criteria` row + their `CriteriaForbiddenDomain` links instead
of one shared file. See .claude/contexts/architecture.md "Data model" for the schema.
"""

from app.models.criteria import Criteria
from app.models.offer import Offer


def offer_matches_criteria(offer: Offer, criteria: Criteria) -> bool:
    """Returns True if `offer` should be kept for a user with these criteria.

    TODO: port the 3-step pipeline from JobFilterEngine.kt:
      1. Reject if the offer's company has any of the user's forbidden domains.
      2. Reject if the offer title doesn't match any of criteria.allowed_job_names
         (word-boundary, case-insensitive — see the Kotlin regex construction).
      3. Reject if title or description mentions any of criteria.forbidden_languages
         (word-boundary, case-insensitive).
    """
    raise NotImplementedError
