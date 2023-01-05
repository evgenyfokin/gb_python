# task_5

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start drawing...")


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"{self.title} drawing...")


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"{self.title} drawing...")


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"{self.title} drawing...")


pen = Pen('Pen')
pen.draw()
print()

pencil = Pencil('Pencil')
pencil.draw()
print()

handle = Handle('Handle')
handle.draw()
