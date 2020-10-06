# Only for Numbers
def my_func(val_1, va_2, val_3):
    tmp_list = [val_1, va_2, val_3]
    return sum(tmp_list) - min(tmp_list)


# Universal
def my_func_u(val_1_u, va_2_u, val_3_u):
    tmp_list = sorted([val_1_u, va_2_u, val_3_u])
    return tmp_list[1] + tmp_list[2]


try:
    args_val = []
    for i in range(1, 4):
        args_val.append(int(input(f"Enter {i} number:")))
    print("Result is ", my_func(args_val[0], args_val[1], args_val[2]))
except Exception as e:
    print(f"Error during calculation: ", str(e))
