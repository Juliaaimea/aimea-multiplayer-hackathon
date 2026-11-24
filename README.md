# aimea: AI first-round interviews (Multiplayer AI Hackathon, SF, Nov 23 2026)

Demo video, made with AdaL: https://youtu.be/4qPz6YgsWxk

Product walkthrough (aimea live interview): https://youtu.be/Vz6OBdX7GWo

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

## Sponsor tools used
- **Bruin**: data pipeline over the agents' decision log (`pipeline.yml`, `assets/`), audit table `mart.agent_decisions`
- **AdaL**: the demo video above was made with AdaL
- **Teamily**: team coordination and submission during the event

## Team
Julia Kurkowski, CEO aimea.ai (Hamburg / San Francisco)
