from itertools import islice
from numpy import where

def create_lcg(seed, mod, a, c):
    def new_lcg():
        num = seed
        while True:
            yield num
            num = (a * num + c) % mod
    return new_lcg

lcg_parameters = (
    [1, 9, 2, 0],
    [3, 9, 2, 0],
    [0, 9, 4, 1]
)

for params in lcg_parameters:
    lcg = create_lcg(*params)
    numbers = list(islice(lcg(), params[1]+1))

    print(f"\nLCG with seed {params[0]}, modulus {params[1]}, a = {params[2]}, c = {params[3]}:")
    print(f"Generated sequence: {numbers}")
    print(f"Period is then {where([n == params[0] for n in numbers])[0][1]}.")
