lst = list(map(int, input().split()))


def max_product(A):
    max_prod = A[0] * A[1]
    k = A[0]
    m = A[1]
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] * A[j] > max_prod:
                k = A[i]
                m = A[j]
    return k, m


print(*sorted(max_product(lst)))