test = set()
all = set()
at_least_one = set()

n = int(input())

for i in range(n):
    m = int(input())

    for j in range(m):
        test.add(input())

    if len(all) == len(at_least_one) == 0:
        all = test.copy()
        at_least_one = test.copy()

    else:
        all &= test
        at_least_one |= test

    test = set()

print(len(all))
for language in all:
    print(language)

print(len(at_least_one))
for language in at_least_one:
    print(language)
