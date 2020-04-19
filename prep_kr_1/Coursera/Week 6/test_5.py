lst = [0] * 101
values = list(map(int, input().split()))

for value in values:
    lst[value] += 1

for i in range(len(lst)):
    for j in range(lst[i]):
        print(i, end=" ")
