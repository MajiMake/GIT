class Canvas:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.massive = []
        self.local_massive = self.massive_creator()
        self.count = 0

    def draw(self):
        for q in range(self.y):

            for g in self.local_massive[q]:
                self.count += 1

                if self.count == self.x:
                    self.count = 0
                    print(g[0])
                else:
                    print(g[0], end='')

    def massive_creator(self):
        for _ in range(self.y):
            self.massive.append([' ' for _ in range(self.x)])
        return self.massive

    def put_pixel(self, x_coordinate, y_coordinate,symbol):
        self.local_massive[y_coordinate][x_coordinate] = symbol
        self.draw()


Reate = Canvas(12,12)
Reate.put_pixel(5,5,'ж')


