class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name}, Go, Zor'ka!")

    def stop(self):
        print(f"{self.name}, Tpruuuu!")

    def turn(self, direction):
        print(f"{self.name}, Turn ", direction)

    def show_speed(self):
        print(f"{self.name}, Current speed is: ", self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        if speed > 60:
            print(f"{self.name}, You've exceeded a speed limit!")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        if speed > 40:
            print(f"{self.name}, You've exceeded speed limit!")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


zaz = TownCar(120, 'rusty', 'Zaporozhec Ushastiy')
bolide = SportCar(400, 'red', 'McLaren')
gazelle = WorkCar(50, 'white', 'GAZ')
party_ven = PoliceCar(150, 'white-blue', 'UAZ')

print(f"Something about town car: name {zaz.name}, color {zaz.color}, speed {zaz.speed} (Suddenly!), is police "
      f"{zaz.is_police} (Who could imagine this?!)")
zaz.go()
zaz.turn('rigth')
zaz.stop()

party_ven.turn('left')
