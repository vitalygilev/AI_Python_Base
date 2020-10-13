import json

raw_data = ['']
res_list = []
avg_profit = 0
try:
    with open("text_77.json", "r", encoding="utf-8") as read_f:
        raw_data = json.load(read_f)
    for cur_firm in raw_data[0]:
        if raw_data[0][cur_firm] > 0:
            res_list.append({cur_firm: raw_data[0][cur_firm]})
            avg_profit += raw_data[0][cur_firm]
    avg_profit /= len(res_list)
except FileNotFoundError as e:
    print("Unable to read json: ", str(e))
res_list.append({'average_profit': avg_profit})

with open("text_77_out.json", "w", encoding="utf-8") as write_f:
    json.dump(res_list, write_f)
