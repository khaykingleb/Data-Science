n = int(input())
lst = list()

for i in range(n):
    person = input().split()
    lst.append([person[0], int(person[1])])

lst.sort(key=lambda x: x[1], reverse=True)

for person in lst:
    print(person[0])
