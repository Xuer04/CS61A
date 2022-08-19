d = {'one': 1, 'two': 2, 'three': 3}

for x, y in iter(d.items()):
    print(f"x:{x}, y:{y}")

lst = [1, 2, 3, 4, 5]

for x, y in enumerate(lst):
    print(f"x:{x}, y:{y}")
