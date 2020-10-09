from functools import reduce


def ex_mul(x, y):
    return x * y


print("Result: ", reduce(ex_mul, [i for i in range(100, 1001) if i % 2 == 0]))
