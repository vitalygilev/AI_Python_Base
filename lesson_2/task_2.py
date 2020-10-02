list_to_process = []
element = input("Input 1 list value or '***' to exit:")
list_counter = 2
while element != '***':
    list_to_process.append(element)
    element = input(f"Input {list_counter} list value or '***' to exit:")
    list_counter += 1
for cur_ind in range(len(list_to_process) - 1, 2):
    list_to_process[cur_ind], list_to_process[cur_ind + 1] = list_to_process[cur_ind + 1], list_to_process[cur_ind]
for cur_ind, cur_el in enumerate(list_to_process):
    print(f"{cur_ind} element = ", cur_el)
