class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = input("Enter dividend: ")
divider = input("Enter divider: ")

try:
    divider = float(divider)
    if divider == 0:
        raise OwnError("Division by zero!")
    res = inp_data = float(dividend) / divider
except ValueError:
    print("Dividend or divider isn't a number!")
except OwnError as err:
    print(err)
else:
    print(f"Result is: {inp_data}")
