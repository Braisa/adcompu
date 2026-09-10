def greater_of_three(a, b, c):
    if a > b and a > c:
        print(a)
        return a
    elif b > c:
        print(b)
        return b
    else:
        print(c)
        return c

def another_way(a, b, c):
    ordered = [a,b,c].sort()
    greatest = ordered[-1]
    print(greatest)
    return greatest
