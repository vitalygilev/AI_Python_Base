from random import randrange

# def_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
def_list = [randrange(100) for i in range(1, randrange(10))]
print("Default list is:", def_list)
print("Result is:", [def_list[i] for i in range(1, len(def_list)) if def_list[i] > def_list[i - 1]])
