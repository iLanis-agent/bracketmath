# Bracket Math

Tournament counting arithmetic. Eleven teams signed up and nobody can say how many games that is.

## What it computes

- **The bracket truth** - single elimination: 11 teams make a bracket of 16 with 5 byes, 3 first-round games, 4 rounds and 10 games in all.
- **The league truth** - round robin: 6 teams played once is 15 games over 5 rounds. Odd team counts add a sit-out round.
- **The clock truth** - your own court count and game length: 10 games on 2 courts at 45 min each is 5 time slots and 3 h 45 min of play.

## Boundary

Arithmetic only. Bracket Math counts byes, rounds and games from the numbers you type. It does not seed teams, pick a format, or say which format is better.

## Files

- `index.html` - landing page.
- `app.html` - the interactive calculator.
- `engine.js` - the counting.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (20 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/bracketmath/
Repo: https://github.com/iLanis-agent/bracketmath
