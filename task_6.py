a = int(input("Введите начальное значение километража спортсмена:"))
b = int(input("Введите конечное значение километража спортсмена:"))
days_counter = 1
while True:
    print(f"{days_counter}-й день %.2f" % a)
    days_counter += 1
    if a >= b:
        break
    a = a + a / 10
