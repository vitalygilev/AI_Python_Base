incomes = float(input("Ввыдите выручку фирмы:"))
expenses = float(input("Ввыдите издержки фирмы:"))
balance = incomes - expenses
if balance < 0:
    print("Ваш бизнес не так уж успешен, но не стоит унывать!")
elif balance == 0:
    print("Гораздо лучше, чем убытки, но Вам есть, куда расти!")
else:
    print("Рентабельность вашей фирмы: %.2f" % (balance / incomes))
    staff = int(input("Введите количество сотрудников: "))
    print("Прибыль в рассчете на одного сотрудника: %.2f" % (balance / staff))
