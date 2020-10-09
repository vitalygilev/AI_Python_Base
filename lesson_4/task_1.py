from sys import argv


# Arguments example: hours=5 rate=10 bonus=10
try:
    param = {el.split("=")[0]: int(el.split("=")[1]) for el in argv if el.find("=") != -1}
    print("Total paycheck is:", param['hours'] * param['rate'] + param['bonus'])

except Exception as e:
    print(f"Error! Arguments example: hours=5 rate=10 bonus=10 ", str(e))
