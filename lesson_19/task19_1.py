def with_index(iterable, start=0):
    count = start
    for elem in iterable:
        yield count, elem
        count += 1

for i, c in with_index('Python'):
    print(i, c)