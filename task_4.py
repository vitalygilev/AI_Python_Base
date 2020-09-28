number = int(input("Введите число:"))
max_digit = -1
while number > 0:
    current_digit = number % 10
    if max_digit < current_digit:
        max_digit = current_digit
    number = number // 10
print("Самая большая цифра в числе:", max_digit)
