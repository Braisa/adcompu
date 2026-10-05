methods = []
for list_method in dir(list):
    if not list_method in dir(tuple):
        methods.append(list_method)
print(f"The following methods are in class list but not in class tuple:\n{methods}")
print("Note that they are the ones relative to adding or removing elements, or changing the order, since tuples are immutable!")