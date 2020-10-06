def my_div(num_1_val, num_2_val):
    return num_1_val / num_2_val


result_achieved = False
while not result_achieved:
    try:
        num_1 = input("Enter 1st number:")
        num_1 = float(num_1)
        num_2 = input("Enter 2nd number:")
        num_2 = float(num_2)
        print(f"Division result is ", my_div(num_1, num_2))
        result_achieved = True
    except Exception as e:
        print(f"Error during division: ", str(e))
