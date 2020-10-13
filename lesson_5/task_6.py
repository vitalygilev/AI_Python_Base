def get_hours(raw_line):
    cur_hours = "0"
    for i in range(len(raw_line)):
        cur_char = raw_line[i:i + 1]
        if '0' <= cur_char <= '9':
            cur_hours += cur_char
        elif cur_char == "(":
            break
    try:
        hours = int(cur_hours)
    except ValueError:
        hours = 0
    return hours


with open("text_6.txt", "r", encoding="utf-8") as f_obj:
    res_dict = {}
    for cur_line in f_obj:
        try:
            cur_pair = cur_line.split(":")
            all_subj_hours = cur_pair[1].split()
            res_dict[cur_pair[0]] = 0
            for cur_raw_hours in all_subj_hours:
                res_dict[cur_pair[0]] += get_hours(cur_raw_hours)
        except Exception as e:
            print("Unable to parse: ", str(e))
print("Result is: ", res_dict)
