import sys

class Rectangle:
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
    
    def intersection(self, other):
        xr = max(self.x, other.x)
        yr = max(self.y, other.y)
    
        x_dash = min(self.x + self.w, other.x + other.w)
        y_dash = min(self.y + self.h, other.y + other.h)

        if xr > x_dash or yr > y_dash:
            return False, None

        wr = x_dash - xr
        hr = y_dash - yr

        return True, Rectangle(xr, yr, wr, hr, "31")


class Space:
    def __init__(self, size):
        self.size = size
        self.grid = [["\033[00m {}\033[00m" .format("\u25A0") for _ in range(self.size)] for _ in range(self.size)]
        self.rectangles = []

    def add_rectangle(self, rectangle):
        self.rectangles.append(rectangle)

    def add_rectangles(self, rectangles):
        self.rectangles += rectangles
    
    def draw_rectangles(self):
        for rectangle in self.rectangles:
            y = rectangle.y
            x = rectangle.x
            w = rectangle.w
            h = rectangle.h
            for j in range(y, y+h):
                for i in range(x, x+w):
                    self.grid[i][j] = "\033[{}m {}\033[00m" .format(rectangle.c, "\u25A0")

    def __repr__(self):
        for j in range(s-1, -1, -1):
            for i in range(0, s, 1):
                print(self.grid[i][j], end="")
            print("")

    def __str__(self):
        x = ""
        for j in range(s-1, -1, -1):
            for i in range(0, s, 1):
                x += self.grid[i][j]
            x+="\n"
        return x


if __name__ == "__main__":
    s = int(sys.argv[1])

    x1 = int(sys.argv[2])
    y1 = int(sys.argv[3])
    w1 = int(sys.argv[4])
    h1 = int(sys.argv[5])

    x2 = int(sys.argv[6])
    y2 = int(sys.argv[7])
    w2 = int(sys.argv[8])
    h2 = int(sys.argv[9])

    if (x1 + w1 > s or x2 + w2 > s or y1 + h1 > s or y2 + h2 > s):
        raise ValueError("one of The Rectangels or both get out of the boundry")

    r1 = Rectangle(x1, y1, w1, h1, "34")
    r2 = Rectangle(x2, y2, w2, h2, "33")
    my_space = Space(s)
    my_space.add_rectangles([r1,r2])

    is_inter, r = r1.intersection(r2)

    if is_inter :
        print("The two rectangels intersect")
        my_space.add_rectangle(r)
    else : 
        print("The two rectangels don't intersect")

    my_space.draw_rectangles()
    print(my_space)
    



