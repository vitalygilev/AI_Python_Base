import tkinter as tk
from PIL import ImageTk, Image
from itertools import cycle


class TrafficLight:
    def __init__(self, working_algorithm):
        self.sec_count = 0
        self.working_algorithm = working_algorithm
        self.img_dict = {'red': Image.open('pic/tl_red.jpg').resize((350, 400)),
                         'yellow': Image.open('pic/tl_yellow.jpg').resize((350, 400)),
                         'green': Image.open('pic/tl_green.jpg').resize((350, 400)),
                         'red+yellow': Image.open('pic/tl_red_yellow.jpg').resize((350, 400)),
                         'off': Image.open('pic/tl_off.jpg').resize((350, 400))}
        self.iterator = cycle(self.working_algorithm)
        self.cur_state = next(self.iterator)

        self.root = tk.Tk()
        self.root.attributes("-topmost", True)
        self.root.geometry('300x400')
        image = ImageTk.PhotoImage(self.img_dict[self.cur_state[0]])
        self.label = tk.Label(image=image)
        self.label.pack(side="top", fill="both", expand="yes")
        self.running()
        self.root.mainloop()

    def running(self):
        self.sec_count += 1
        if self.sec_count == self.cur_state[1]:
            self.cur_state = next(self.iterator)
            self.sec_count = 0
            cur_img = ImageTk.PhotoImage(self.img_dict[self.cur_state[0]])
            self.label.configure(image=cur_img)
            self.label.photo_ref = cur_img
            self.label.pack()
        self.root.after(100, self.running)


mode = input("Enter traffic-light mode (0 - simple, 1-advanced):")
if mode == '0':
    app = TrafficLight([('red', 70), ('yellow', 20), ('green', 50), ('yellow', 20)])
elif mode == '1':
    app = TrafficLight([('red', 70),
                        ('red+yellow', 20),
                        ('green', 50),
                        ('off', 5),
                        ('green', 5),
                        ('off', 5),
                        ('green', 5),
                        ('off', 5),
                        ('green', 5),
                        ('yellow', 20)])
else:
    print('Wrong choice!')
