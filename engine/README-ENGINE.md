# Tiny Chess Engine (4 KB)

A strong chess engine in a single 4,096-byte `main.py`: an LZMA+base85 packed
payload (the readable source is ~7.7 KB) that unpacks at import and plays
through the env at `MAKEFUN_ENV_URL`.

Engine: 0x88 board, pseudo-legal movegen with make/unmake legality filter,
alpha-beta + transposition table + killer moves + history heuristic + MVV-LVA
ordering, quiescence (captures, promotions, all evasions in check), check
extension, iterative deepening to a fixed 25,000-node budget, tapered
piece-square evaluation (middlegame/endgame, bishop pair, tempo).
Deterministic: fixed node count, no clock, no unseeded randomness; Zobrist
keys from a fixed-seed LCG. Legal per perft (startpos, kiwipete, pos3-5).

License: MIT.
