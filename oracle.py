#!/usr/bin/env python3
# Bracket Math oracle - mirrors engine.js.
import json, math

def _int(x, lo, msg):
    if not math.isfinite(x) or x % 1 != 0 or x < lo:
        raise ValueError(msg)

def _teams(n):
    _int(n, 2, "teams must be a whole number, 2 or more")
    if n > 1024:
        raise ValueError("keep teams at 1024 or fewer")

def _s(n, one, many):
    return one if n == 1 else many

def _dur(m):
    if m < 60:
        return f"{m} min"
    h, r = divmod(m, 60)
    return f"{h} h" if r == 0 else f"{h} h {r:02d} min"

def bracket_truth(teams):
    _teams(teams)
    size, rounds = 1, 0
    while size < teams:
        size *= 2
        rounds += 1
    byes = size - teams
    first = teams - size // 2
    return (f"{teams} teams: bracket of {size}, {byes} {_s(byes, 'bye', 'byes')}, "
            f"{first} first-round {_s(first, 'game', 'games')}, {rounds} {_s(rounds, 'round', 'rounds')}, "
            f"{teams - 1} {_s(teams - 1, 'game', 'games')} in all.")

def league_truth(teams, times):
    _teams(teams)
    _int(times, 1, "times played must be a whole number, 1 or more")
    if times > 6:
        raise ValueError("keep times played at 6 or fewer")
    games = times * (teams * (teams - 1) // 2)
    per_round = teams // 2
    odd = teams % 2 == 1
    rounds = times * (teams if odd else teams - 1)
    each = times * (teams - 1)
    how = "once" if times == 1 else "twice" if times == 2 else f"{times} times"
    if odd:
        tail = f"each team plays {each} and sits out {times} {_s(times, 'round', 'rounds')}"
    else:
        tail = f"every team plays {each}"
    return (f"{teams} teams, played {how}: {games} {_s(games, 'game', 'games')} over {rounds} "
            f"{_s(rounds, 'round', 'rounds')}, {per_round} {_s(per_round, 'game', 'games')} per round, {tail}.")

def clock_truth(games, courts, minutes):
    _int(games, 1, "games must be a whole number, 1 or more")
    _int(courts, 1, "courts must be a whole number, 1 or more")
    _int(minutes, 1, "minutes per game must be a whole number, 1 or more")
    slots = math.ceil(games / courts)
    return (f"{games} {_s(games, 'game', 'games')} on {courts} {_s(courts, 'court', 'courts')} at "
            f"{minutes} min each: {slots} {_s(slots, 'time slot', 'time slots')}, {_dur(slots * minutes)} of play.")

FNS = {"bracketTruth": bracket_truth, "leagueTruth": league_truth, "clockTruth": clock_truth}

CASES = [
    ("bracketTruth", [11]), ("bracketTruth", [2]), ("bracketTruth", [8]), ("bracketTruth", [9]),
    ("bracketTruth", [1]), ("bracketTruth", [1025]), ("bracketTruth", [6.5]),
    ("leagueTruth", [6, 1]), ("leagueTruth", [5, 1]), ("leagueTruth", [6, 2]), ("leagueTruth", [2, 1]),
    ("leagueTruth", [3, 3]), ("leagueTruth", [6, 0]), ("leagueTruth", [6, 7]),
    ("clockTruth", [10, 2, 45]), ("clockTruth", [1, 1, 30]), ("clockTruth", [7, 3, 60]),
    ("clockTruth", [30, 4, 25]), ("clockTruth", [0, 2, 45]), ("clockTruth", [10, 0, 45]),
]

out = []
for fn, args in CASES:
    try:
        exp = FNS[fn](*args)
    except ValueError as e:
        exp = "ERR:" + str(e)
    out.append({"fn": fn, "args": args, "expected": exp})
with open("expected.json", "w") as f:
    json.dump(out, f, indent=1)
    f.write("\n")
print(len(out), "cases")
