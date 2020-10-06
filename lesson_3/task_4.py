def my_pow(x_val, y_val):
    result = 1
    for ind in range(0, y_val, -1):
        result /= x_val
    return result


try:
    x = float(input("Enter x (number):"))
    y = int(input(f"Enter y (negative integer):"))
    if y >= 0:
        raise Exception("y is greater or equal 0!")
    print("Result of my_pow is ", my_pow(x, y))
    print("Result of ** is ", x ** y)
except Exception as e:
    print(f"Error during calculation: ", str(e))
