import random

class DLA:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        field = [[0] * X for i in range(Y)]
        self.field = field

    def generator(self,d_min, d_max):
        self.r = random.randrange(d_min, d_max,2)


    def circle(self):
        min = self.r
        Xmax = self.X-self.r-1
        Ymax = self.Y-self.r-1
        X0=random.randint(min,Xmax)
        Y0=random.randint(min,Ymax)
        for i in range(self.Y):
            for j in range(self.X):
                if abs((i - X0) ** 2 + (j - Y0) ** 2) <= (self.r) ** 2:
                    self.field[i][j] = 1

def display(field):
    for i in range(0, len(field)):
        for j in range(0, len(field[i])):
            print(field[i][j], end=' ')
        print()
    print()



def main():
    dla1 = DLA(25, 25)
    dla1.generator(0,6)
    dla1.circle()
    display(dla1.field)

main()