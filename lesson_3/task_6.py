def int_func(word):
    return str(word).title()


source_str = input("Enter text:")
print("Source string:", source_str)
print("Result string:", " ".join(list(map(int_func, source_str.split()))))
