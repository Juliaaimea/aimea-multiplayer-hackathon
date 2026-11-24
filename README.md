# aimea: AI first-round interviews (Multiplayer AI Hackathon, SF, Nov 23 2026)

Demo video (EN): https://www.youtube.com/watch?v=PTSh6aeMNKE

**aimea** runs the first-round job interview as a live voice conversation between an AI interviewer (Mea) and the candidate, then hands the recruiting team a structured, evidence-based report. Multiplayer by design: candidate, AI interviewer and hiring team work on one shared interview record.

## What this repo contains
This is a public showcase repo. The aimea product code is proprietary and not included.
It contains a small **Bruin** pipeline that turns interview results into a hiring-team dashboard table, built on **synthetic data only** (no real candidates).

- `pipeline.yml`: Bruin pipeline definition
- `assets/raw_interviews.asset.yml`: synthetic seed data (`data/interviews.csv`)
- `assets/team_summary.sql`: per-role summary for the hiring team

## Run
```
bruin validate .
bruin run .
```

## Team
Julia Kurkowski, CEO aimea.ai (Hamburg / San Francisco)
