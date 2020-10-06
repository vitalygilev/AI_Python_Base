def multi_sum(terms):
    global glob_sum
    finish_work = False
    for i in terms:
        try:
            if i == '***':
                finish_work = True
                break
            cur_term = int(i)
            glob_sum += cur_term
        except Exception as e:
            print(f"Error during calculation: ", str(e))
    return finish_work


glob_sum = 0
finish = False
while not finish:
    finish = multi_sum(input("Enter next numeric string (to exit type '***' after numbers):").split())
    print("Current global sum is ", glob_sum)
