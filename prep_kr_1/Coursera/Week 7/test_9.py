import sys

d = dict()
lst = sys.stdin.read().split()

for element in lst:
    d[element] = d.get(element, 0) + 1

max_val = max(list(d.values()))

for key in sorted(d):
    if d[key] == max_val:
        print(key)
        break
