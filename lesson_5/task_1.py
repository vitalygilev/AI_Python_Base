write_str = "111"
with open("dump.txt", "w", encoding="utf-8") as f_obj:
    while write_str != "":
        write_str = input("Enter string to remember or empty string to exit:")
        print(write_str, file=(f_obj if write_str != "" else None))

with open("dump.txt", "r", encoding="utf-8") as f_obj:
    print("You've typed:")
    print(f_obj.read())
