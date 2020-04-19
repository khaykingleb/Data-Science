memory, n = map(int, input().split())
memory_each = list()

for i in range(n):
    memory_each.append([int(input()), i])

memory_each.sort()

cnt = 0
for memory_i in memory_each:
    memory -= memory_i[0]
    if memory >= 0:
        cnt += 1
    else:
        break

print(cnt)
