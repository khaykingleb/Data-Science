n = int(input())
lst = [i for i in range(int('1' + '0' * (n - 1)), int('1' + '0' * n)) if i % 2 != 0]
print(*list(reversed(lst)))