raw = input("Введите цифру:")
# Вариант с циклом
i = 1
result = 0
temp = ""
while i < 4:
    temp = temp + raw
    result = result + int(temp)
    i += 1
print("Результат = ", result)

# Вариант без цикла
print("Результат = ", int(raw) + int(raw + raw) + int(raw + raw + raw))
