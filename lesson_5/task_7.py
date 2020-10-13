import json

raw_data = ['']
res_list = [{}]
avg_profit = 0
count = 0
try:
    with open("text_7.txt", "r", encoding="utf-8") as read_f:
        raw_data = read_f.readlines()
    for cur_firm in raw_data:
        raw_lines = cur_firm.split()
        profit = int(raw_lines[2]) - int(raw_lines[3])
        if profit > 0:
            avg_profit += profit
            count += 1
        res_list[0][raw_lines[0]] = profit
    avg_profit /= (1 if count == 0 else count)
except FileNotFoundError as e:
    print("Unable to read json: ", str(e))
res_list.append({'average_profit': avg_profit})

with open("text_77_out.json", "w", encoding="utf-8") as write_f:
    json.dump(res_list, write_f, ensure_ascii=False)
