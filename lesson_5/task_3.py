with open("text_3.txt", "r", encoding="utf-8") as f_obj:
    avg_salary = 0
    lines = 0
    for cur_line in f_obj:
        try:
            cur_pair = cur_line.split()
            cur_salary = float(cur_pair[1])
            if cur_salary < 20000:
                print(f"Employee {cur_pair[0]} earns less than 20000: ({cur_salary})")
            avg_salary += cur_salary
            lines += 1
        except Exception as e:
            print("Unable to recognize person/salary: ", str(e))

print("Average salary is ", avg_salary/lines)
