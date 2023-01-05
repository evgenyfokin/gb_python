# task_1
from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    @staticmethod
    def switch_colors():
        timing = [7, 2, 7]
        i = 0
        while i < 3:
            print(TrafficLight.__color[i])
            sleep(timing[i])
            i += 1


switcher = TrafficLight()
switcher.switch_colors()
