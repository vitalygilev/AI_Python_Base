source_str = input("Enter a string:")
for ind, el in enumerate(source_str.split()):
    print(ind + 1, el[:10])
