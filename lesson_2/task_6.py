goods = [(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
         (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
         (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})]
analytics_list = {}
for cur_good in goods:
    for cur_key in cur_good[1].keys():
        cur_values = analytics_list.get(cur_key)
        if cur_values is None:
            cur_values = []
        add_val = cur_good[1][cur_key]
        if not (add_val in cur_values):
            cur_values.append(add_val)
        analytics_list[cur_key] = cur_values
print(analytics_list)
