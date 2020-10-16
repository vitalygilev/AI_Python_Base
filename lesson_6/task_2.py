class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, depth_loc):
        return round(self._length * self._width * 25 * depth_loc / 1000, 3)


depth = int(input("Enter the road's depth:"))
road = Road(5000, 20)
print(f"The result is {road.asphalt_mass(depth)} tonnes.")
