# Chess for Everyone — a free offline chess tutor

**ACE Builders 48h sprint (21–22 Nov 2026) · Theme: AI for Good · Solo · Registration #1148**

## Concept

Chess for Everyone is a free, fully offline chess tutor that runs in any browser with zero accounts, zero cost, and zero data collection. It is built on our own 4 KB chess engine (practice ~1393 Elo, deterministic, verified legal by perft), wrapped in a teaching layer: adaptive lessons and puzzles that explain *why* a move is good, not just what to play.

It helps kids in under-resourced schools who have no coach, seniors keeping their minds sharp, and blind and low-vision players — full keyboard play and screen-reader announcements, no mouse required. It fits "AI for Good" because the AI is the teacher: it adapts difficulty to the learner, explains in plain language, and works on any old device with no internet. Chess education as digital inclusion, not a game for its own sake.

## Why this base

Three existing bases were verified on 19 Nov 2026:

| Base | Verdict | Fit for "AI for Good" |
| --- | --- | --- |
| **Tiny Chess** (4 KB engine) | ✅ PASS — perft 20/400/8902 exact | **Best.** Chess = education, cognitive health, accessibility. The engine is already strong; the sprint adds teaching, not a new engine. |
| PRISM SWARM (arena survival) | ✅ PASS — serves HTTP 200, all 8 JS modules parse | Weak. An arena survival game needs a forced reskin to fit the theme. |
| EMBERLINE (tactical FPS) | ✅ PASS — serves HTTP 200, all 13 src modules parse, three.js vendored | Worst. A shooter theme fights the "AI for Good" brief. |

## Sprint plan (21–22 Nov, 48h)

**Day 1 — Sat 21/11 (11:30 start)**
1. Tutor shell: static page, board UI, engine wired in via Web Worker (no server).
2. Adaptive difficulty: scale engine strength by capping the node budget per level.
3. Lesson mode: first 3 lessons (how pieces move, check/checkmate, one tactic).

**Day 2 — Sun 22/11**
4. Puzzle set: mate-in-1 / mate-in-2 / fork / pin, with plain-language explanations.
5. Accessibility pass: full keyboard play, ARIA live regions, high-contrast board, screen-reader move announcements.
6. Polish + demo video (≤3 min) + final README + submit.

## Setup

```sh
# Engine smoke test (needs Python 3 only — no dependencies)
python3 tests/smoke_perft.py
# Expected: perft1 20, perft2 400, perft3 8902
```

The tutor itself is a static site: open `web/index.html` in a browser, or serve the folder with any static server. No build step, no backend, no accounts, no network calls at runtime.

## Structure

- `engine/` — the Tiny Chess engine: readable source (`tiny-chess-src.py`), packed 4 KB entry (`main.py`), engine README.
- `web/` — tutor UI (built during the sprint).
- `tests/` — smoke tests (perft legality check).

## License

MIT. Engine originally built for the make.fun tiny-chess-01 bounty; reused here under the same MIT license.
