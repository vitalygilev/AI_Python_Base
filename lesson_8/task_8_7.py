def get_num_pres(num, i_part=False):
    res = str(num) if num > 0 or num < 0 else ''
    if i_part:
        if num > 0:
            res = '+' + res + 'i'
        elif num < 0:
            res += 'i'
    return res


class MyComplex:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __str__(self):
        return "(" + get_num_pres(self.a) + get_num_pres(self.b, True) + ")"

    def __add__(self, other):
        res = "(" + get_num_pres(self.a + other.a) + get_num_pres(self.b + other.b, True) + ")"
        if res == '()':
            res = 0j
        return res

    def __mul__(self, other):
        res = "(" + get_num_pres(self.a * other.a - self.b * other.b) + \
              get_num_pres(self.b * other.a + self.a * other.b, True) + ")"
        if res == '()':
            res = 0j
        return res


z1 = MyComplex(1, 2)
z2 = MyComplex(-1, -2)
z3 = MyComplex(0)

z11 = complex(1, 2)
z12 = complex(-1, -2)
z13 = MyComplex(0)

print(f"My {z1} Standard {z11}")
print(f"My {z2} Standard {z12}")
print(f"My {z3} Standard {z13}")
print(f"My {z1 + z2} Standard {z11 + z12}")
print(f"My {z1 * z2} Standard {z11 * z12}")
