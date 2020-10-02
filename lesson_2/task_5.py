rating_list = []
cur_enter = ''
while cur_enter != '***':
    cur_enter = input("Enter current number:")
    if not cur_enter.isdigit():
        print("Enter numeric value!")
    elif cur_enter == '***':
        break
    else:
        cur_num = int(cur_enter)
        ins_index = 0
        for cur_index, cur_elem in enumerate(rating_list):
            if cur_elem < cur_num:
                ins_index = cur_index
                break
        rating_list.insert(ins_index, cur_num)
        print("Rating structure now is: ", rating_list)
