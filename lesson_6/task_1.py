from itertools import cycle
import time


class TrafficLight:
    def __init__(self):
        self._color = ''

    def running(self):
        print(f"{time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime())} : traffic light started.")
        for it in cycle([('red', 7), ('yellow', 2), ('green', 5), ('yellow', 2)]):
            self._color = it[0]
            print(f"{time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime())} : color is {self._color}")
            time.sleep(it[1])


tl = TrafficLight()
tl.running()
