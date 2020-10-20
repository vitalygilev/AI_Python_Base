from abc import abstractmethod, ABC


class Clothes:
    @abstractmethod
    def calculate(self):
        pass


class Coat(ABC, Clothes):
    def __init__(self, v):
        self._v = v

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, v):
        if v < 38 or v > 76:
            self._v = 38
        elif v > 76:
            self._v = 76
        else:
            self._v = v

    def calculate(self):
        return round(self.v / 6.5 + 0.5, 3)


class Suit(ABC, Clothes):
    def __init__(self, h):
        self._h = h

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h):
        if h < 0.5:
            self._h = 0.5
        elif h > 2.5:
            self._h = 2.5
        else:
            self._h = h

    def calculate(self):
        return round(2 * self.h + 0.3, 3)


coat = Coat(50)
print(f"Coat's fabric consumption: {coat.calculate()} (v = {coat.v})")
suit = Suit(1.7)
print(f"Suit's fabric consumption: {suit.calculate()} (h = {suit.h})")
