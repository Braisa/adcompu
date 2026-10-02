from random import random
from itertools import islice

def random_walk(start=0, cap=.5):
    position = start
    while True:
        yield position
        position += -1 + 2 * (random() < cap)

M = 1000
N = 100

walks = [list(islice(random_walk(), N)) for _ in range(M)]
walks_msq = 1/M * sum(walk[-1]**2 for walk in walks)

print(f"Simulated {M} walks of {N} steps, and obtained a msq of {walks_msq}")
