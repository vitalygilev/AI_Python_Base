time_in_seconds = int(input("Введите время в секундах:"))
time_sec = time_in_seconds % 60
time_min = time_in_seconds // 60 % 60
time_hours = time_in_seconds // 60 // 60
print(f"Время в формате чч:мм:сс : {time_hours}:{time_min}:{time_sec}")
