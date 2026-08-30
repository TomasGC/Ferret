"""
TODO test cases for app.filters.offer_matches_criteria, mirroring
Engine/JobFilterEngine.kt's behavior:
  - offer kept when title matches an allowed_job_names entry and nothing forbidden
  - offer rejected when company has a forbidden domain
  - offer rejected when title doesn't match any allowed_job_names entry
  - offer rejected when title or description contains a forbidden language
    (case-insensitive, word-boundary — e.g. "GO" must not match "Golang" or "Django")
"""
