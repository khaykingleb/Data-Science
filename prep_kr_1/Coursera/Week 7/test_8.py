d = dict()
n = int(input())

for i in range(n):
    s = input().split()
    d[s[0]] = s[1]
    d[s[1]] = s[0]

print(d[input()])
