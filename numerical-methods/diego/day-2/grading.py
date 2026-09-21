grades = [8.5, 7.0, 5.5, 9.0, 4.0, 10.0, 9.5, 7.5]

mean = lambda l : sum(l)/len(l)

def lowest(l, highest_instead=False):
    ordered = l.sort()
    extreme = l[-int(highest_instead)]
    return extreme

def passing(l, failing_instead=False):
    passing_tally = 0
    for grade in l:
        passing_tally += int(grade >= 5) + (int(grade < 5) - int(grade >= 5)) * int(failing_instead)
    passing_ratio = passing_tally / len(l)
    return passing_tally, passing_ratio

print(mean(grades))
print(lowest(grades, highest_instead=True))
print(lowest(grades))
print(passing(grades))
print(passing(grades, failing_instead=True))
