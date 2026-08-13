# FutureSkill AI --- Submission Documentation

## Architecture

See `architecture_diagram.png`.

### System flow

1.  Workforce/sample data is loaded from `data/`.
2.  `data_analysis.py` performs workforce skill analysis.
3.  `model.py` performs skill-gap analysis.
4.  `database.py` stores persistent skill records in SQLite.
5.  `main.py` exposes Flask pages and JSON API endpoints.
6.  The dashboard consumes the APIs and displays future skills,
    declining skills, reskilling roles and skill-gap results.

## Database / Data Model

The main table is `skill_records`.

  Field            Purpose
  ---------------- --------------------------
  id               Unique record ID
  industry         Industry/category
  process          Business process
  activity         Workforce activity
  role             Job role
  current_skill    Existing skill
  ai_impact        AI impact classification
  future_skill     Suggested future skill
  skill_gap        Skill-gap score
  priority         Reskilling priority
  recommendation   Recommended action

## Scaling: 100 → 1,000 Processes

-   Add database indexes for frequently queried fields.
-   Add pagination to record APIs.
-   Cache repeated analysis results.
-   Move expensive analysis to background jobs if needed.
-   Use a production WSGI server rather than Flask's development server.
-   Move from SQLite to PostgreSQL when concurrent production workloads
    require it.
-   Add validation, logging, monitoring and error handling.
