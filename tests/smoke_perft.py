"""Smoke test: Tiny Chess engine movegen is legal (perft, startpos).

Runs the readable engine source (engine/tiny-chess-src.py) without the
network loop and checks perft(1..3) == 20 / 400 / 8902.
Usage: python3 tests/smoke_perft.py   (run from the repo root)
"""
import os
import sys

os.environ.setdefault('MAKEFUN_ENV_URL', 'http://127.0.0.1:9/')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'engine', 'tiny-chess-src.py')

src = open(SRC).read().split('while 1:')[0]
ns = {}
exec(src, ns)
pf, gen, make, unmake, legal = ns['pf'], ns['gen'], ns['make'], ns['unmake'], ns['legal']


def perft(d):
    if d == 0:
        return 1
    n = 0
    for m in gen():
        if legal(m):
            make(m)
            n += perft(d - 1)
            unmake()
    return n


pf('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
got = (perft(1), perft(2), perft(3))
want = (20, 400, 8902)
print('perft1', got[0], 'perft2', got[1], 'perft3', got[2])
assert got == want, f'perft mismatch: {got} != {want}'
print('OK: engine movegen legal')
