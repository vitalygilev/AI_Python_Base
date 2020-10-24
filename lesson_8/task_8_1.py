import datetime


class MyDate:

    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def cast_date(cls, str_date):  # 01-01-2020
        cur_str_date = cls(str_date).str_date
        return (int(cur_str_date[0:2]), int(cur_str_date[3:5]), int(cur_str_date[6:])) if len(cur_str_date) == 10 else \
            (int(cur_str_date[0:2]), int(cur_str_date[2:4]), int(cur_str_date[4:])) if len(cur_str_date) == 8 else \
                (int(cur_str_date[0:2]), int(cur_str_date[2:4]), int('20' + cur_str_date[4:]))

    @staticmethod
    def validate(casted_date):
        days_num = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        res = None
        if 0 < casted_date[0] <= days_num[casted_date[1]] + 1 if casted_date[2] % 4 == 0 else 0\
                and 0 < casted_date[1] <= 12\
                and 1900 < casted_date[2] < 2100:
            res = datetime.date(casted_date[2], casted_date[1], casted_date[0])
        return res


print(MyDate.validate(MyDate.cast_date('29-02-2021')))
print(MyDate.validate(MyDate.cast_date('29-02-2020')))
print(MyDate.validate(MyDate.cast_date('01012020')))
print(MyDate.validate(MyDate.cast_date('010120')))
