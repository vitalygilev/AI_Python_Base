class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Отрисовка карандашом.")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Отрисовка ручкой.")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Отрисовка маркером.")


pen = Pen('pen')
pen.draw()
pencil = Pencil('pencil')
pencil.draw()
handle = Handle('handle')
handle.draw()
