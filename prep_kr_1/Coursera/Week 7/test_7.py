import sys

d = dict()
itr = sys.stdin.read().split()

for element in itr:
    d[element] = d.get(element, 0) + 1
    print(d[element] - 1, end=" ")
