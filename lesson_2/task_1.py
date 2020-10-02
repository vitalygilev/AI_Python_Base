type_list = [12,
             12.3,
             (5+3j),
             'string',
             [1, 2, 3],
             (1, 2, 3),
             {1, 2, 3},
             {1: 'one', 2: 'two'},
             False,
             b'text',
             bytearray(b'text'),
             None,
             ZeroDivisionError]
for cur_type in type_list:
    print(type(cur_type))
