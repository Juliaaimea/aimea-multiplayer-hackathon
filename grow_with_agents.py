"""Grow with Agents: three agents run a first-round interview together.

Mea (interviewer) asks, Sam (synthetic candidate) answers, Coach scores and gives
feedback that quotes the candidate and ties every score to a turn id.
Every decision is written to data/decision_log.csv, which Bruin queries.
LLM calls go through the Claude Code CLI (`claude -p`). Synthetic data only.
"""
import csv, json, subprocess, sys, pathlib

ROLE = "Customer Support Agent (retail, San Francisco)"
PERSONA = sys.argv[1] if len(sys.argv) > 1 else "Sam, 2 years in a call center, calm, sometimes vague about numbers"
TURNS = 3
OUT = pathlib.Path(__file__).parent / "data"

def ask(system, prompt):
    system = "Always answer in English. " + system
    r = subprocess.run(["claude", "-p", "--model", "haiku", f"{system}\n\n{prompt}"],
                       capture_output=True, text=True, timeout=120)
    return r.stdout.strip()

log, transcript = [], []
def decide(turn, agent, decision, reason):
    log.append({"turn": turn, "agent": agent, "decision": decision, "reason": reason})
    print(f"[{turn}] {agent:9} -> {decision} | {reason}")

for t in range(1, TURNS + 1):
    hist = "\n".join(f"{x['turn']} {x['who']}: {x['text']}" for x in transcript)
    q = ask(f"You are Mea, a warm AI interviewer for the role {ROLE}. Ask ONE short behavioral question. "
            "If the last answer was vague, ask a follow-up for a concrete example instead. Output only the question.",
            f"Conversation so far:\n{hist or '(start)'}")
    decide(t, "Mea", "follow-up" if t > 1 and "example" in q.lower() else "new question", q[:90])
    transcript.append({"turn": f"T{t}a", "who": "Mea", "text": q})
    a = ask(f"You are a job candidate: {PERSONA}. Answer in 2-3 sentences, in character.", f"Question: {q}")
    transcript.append({"turn": f"T{t}b", "who": "Candidate", "text": a})
    decide(t, "Candidate", "answered", a[:90])

hist = "\n".join(f"{x['turn']} {x['who']}: {x['text']}" for x in transcript)
fb = ask("You are Coach. Score communication and problem_solving 1-5. Every score MUST quote the candidate "
         "verbatim and cite the turn id. Then give 2 growth tips. Return JSON: "
         '{"communication":{"score":n,"quote":"","turn":""},"problem_solving":{...},"tips":["",""]}. JSON only.',
         hist)
try:
    j = json.loads(fb[fb.find("{"):fb.rfind("}") + 1])
except Exception:
    j = {"raw": fb}
for k in ("communication", "problem_solving"):
    if k in j:
        decide("final", "Coach", f"{k}={j[k]['score']}", f"{j[k]['turn']}: \"{j[k]['quote'][:70]}\"")

OUT.mkdir(exist_ok=True)
with open(OUT / "decision_log.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["turn", "agent", "decision", "reason"]); w.writeheader(); w.writerows(log)
with open(OUT / "transcript.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["turn", "who", "text"]); w.writeheader(); w.writerows(transcript)
(OUT / "feedback.json").write_text(json.dumps(j, indent=2))
print("\nCoach feedback:\n" + json.dumps(j, indent=2))
