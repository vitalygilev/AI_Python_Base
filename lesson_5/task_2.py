with open("dump.txt", "r", encoding="utf-8") as f_obj:
    content = f_obj.readlines()
    print("Lines count for file is:", len(content))
    for cur_line in range(len(content)):
        print(f"Words in line {cur_line + 1}:", len(content[cur_line].split()))
