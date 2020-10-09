def fact_of(n):
    result = 1
    if n == 0:
        yield result
    for i in range(1, n + 1):
        result *= i
        yield result


try:
    bound = int(input("Enter bound:"))
    if bound < 0:
        raise Exception('Wrong bound! Bound must be >= 0')
    for el in fact_of(bound):
        print(el)

except Exception as e:
    print(f"Error: ", str(e))
