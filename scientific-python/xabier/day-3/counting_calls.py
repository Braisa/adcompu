from functools import wraps, lru_cache

def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, "calls"):
            setattr(wrapper, "calls", 0)
        else:
            setattr(wrapper, "calls", 1 + getattr(wrapper, "calls"))
        return func(*args, **kwargs)
    return wrapper

@count_calls
def naive_fib_rec(n):
    if n < 2:
        return n
    return naive_fib_rec(n-1) + naive_fib_rec(n-2)

@count_calls
@lru_cache
def cached_naive_fib_rec(n):
    if n < 2:
        return n
    return cached_naive_fib_rec(n-1) + cached_naive_fib_rec(n-2)

@lru_cache
@count_calls
def inv_cached_naive_fib_rec(n):
    if n < 2:
        return n
    return inv_cached_naive_fib_rec(n-1) + inv_cached_naive_fib_rec(n-2)

print_ns = (10, 20, 25)
for print_n in print_ns:
    naive_fib_rec.calls, cached_naive_fib_rec.calls, inv_cached_naive_fib_rec.calls = 0, 0, 0
    
    naive_fib_rec(print_n)
    cached_naive_fib_rec(print_n)
    inv_cached_naive_fib_rec(print_n)

    print(f"Fibonacci({print_n})")
    print(f"Naive calls: {naive_fib_rec.calls}")
    print(f"Cached calls: {cached_naive_fib_rec.calls}")
    print(f"Inverted calls: {inv_cached_naive_fib_rec.calls}")
    print(25*"-")
