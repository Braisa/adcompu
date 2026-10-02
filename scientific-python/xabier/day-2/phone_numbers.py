def get_phone_pairs(names, numbers, dict=False):
    if not dict:
        return tuple((name, number) for name, number in zip(names, numbers))
    else:
        return {name: number for name, number in zip(names, numbers)}

names = ["Jose Angel", "Diego", "Xabier", "Aaron", "Juan", "Thomas"]
numbers = [102030, 405060, 708090, 302010, 605040, 908070]

print(f"Phonebook as tuple: {get_phone_pairs(names, numbers)}")
print(f"Phonebook as dict: {get_phone_pairs(names, numbers, dict=True)}")
