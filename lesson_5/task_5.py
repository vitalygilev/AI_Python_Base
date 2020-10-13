from random import randrange


gen_str = ""
for _ in range(randrange(100)):
    gen_str += str(randrange(100)) + " "
print("Source string: ", gen_str)

with open("text_5.txt", "w", encoding="utf-8") as f_obj:
    f_obj.write(gen_str[:len(gen_str) - 1])

with open("text_5.txt", "r", encoding="utf-8") as f_obj:
    try:
        print("Sum numbers in file: ", sum(map(int, f_obj.read().split())))
    except Exception as e:
        print("Unable to sum numbers in file: ", str(e))
