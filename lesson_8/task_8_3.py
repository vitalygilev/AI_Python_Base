class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


res_list = []
cur_elem = ''
while True:
    cur_elem = input("Enter next element: ")
    if cur_elem == 'stop':
        break
    try:
        if not cur_elem.isnumeric():
            raise OwnError("You've entered not a number!")
        res_list.append(int(cur_elem))
    except OwnError as e:
        print(e)
    except ValueError as e:
        print('Some else exception ', e)

print('Result is ', res_list)
