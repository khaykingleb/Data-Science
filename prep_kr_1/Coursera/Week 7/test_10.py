import sys
s = sys.stdin.read().split()
d = dict()

for element in s:
    if element not in d:
        d[element] = (1, element)
    else:
        d[element] = (d[element][0] + 1, element)

lst = list(sorted(d.values()))
lst.sort(key=lambda x: x[0], reverse=True)

for element in lst:
    print(element[1])
