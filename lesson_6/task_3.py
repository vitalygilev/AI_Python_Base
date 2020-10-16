class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return self.surname + " " + self.name

    def get_total_income(self):
        return sum(self._income.values())


john_smith = Position('John', 'Smith', 'baker', {"wage": 10000, "bonus": 5000})
jane_doe = Position('Jane', 'Doe', 'actress', {"wage": 100000, "bonus": 500000})
print(f"Person {john_smith.get_full_name()}, income {john_smith.get_total_income()}")
print(f"Person {jane_doe.get_full_name()}, income {jane_doe.get_total_income()}")
