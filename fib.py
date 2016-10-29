import numpy as np

def fib(n):
    if n < 0:
        return 0
    fib_matrix = np.matrix([[1,1],
                            [1,0]])
    fib_init = np.matrix([[1],
                          [1]])
    fib_matrix_for_n = fib_matrix ** (n-1)
    fib_vector_for_n = fib_matrix_for_n * fib_init
    fib_n = fib_vector_for_n[0][0]
    return int(fib_n)

def fib_rec(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

memo = {0: 1, 1: 1}
def fib_memo(n):
    if n < 0:
        return 0
    if n in memo:
        return memo[n]
    fib_n = fib_memo(n-1) + fib_memo(n-2)
    memo[n] = fib_n
    return fib_n


def fib_sum(N, fibf):
    last = 1
    index = 0
    result_sum = 0
    while last <= N:
        result_sum += last
        index += 1
        last = fibf(index)

    return result_sum

def fib_even_sum(N, fibf):
    last = 0
    index = 0
    result_sum = 0
    while last <= N:
        if last % 2 == 0:
            result_sum += last
        index += 1
        last = fibf(index)

    return result_sum

N = 4000000
print(fib_sum(N, fib))
#print(fib_sum(N, fib_memo))
print(fib_even_sum(N, fib))
#print(fib_even_sum(N, fib_memo))























def test_fib_neg():
    for i in range(-1, -100, -1):
        assert fib(i) == 0

def test_fib_sums():
    for i in range(0, 4000000, +10000):
        assert fib_sum(i, fib) == fib_sum(i, fib_memo)

def test_fib():
    for i in range(0, 80):
        assert fib(i) == fib_memo(i)

