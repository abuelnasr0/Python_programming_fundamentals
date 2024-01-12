import sys
def draw_rectangle_0(s, x, y, w, h):
    # my algorithm
    if x+w > s :
        raise ValueError(f"The rectangle gets out of the boundry {x}+{w} > {s}")
    if y+h > s :
        raise ValueError(f"The rectangle gets out of the boundry {y}+{h} > {s}")

    for j in range(s-1, -1, -1):
        for i in range(0, s, 1):
            in_vertically = j >= y and j < y+h
            in_horizintally = i >= x and i < x+w
            if in_horizintally and in_vertically:
                print("\033[34m {}\033[00m" .format("\u25A0"), end="")
            else:
                print("\033[31m {}\033[00m" .format("\u25A0"), end="")
        print("")


def draw_rectangle_1(s, x, y, w, h):
    # course algorithm
    if x+w > s :
        raise ValueError(f"The rectangle gets out of the boundry {x}+{w} > {s}")
    if y+h > s :
        raise ValueError(f"The rectangle gets out of the boundry {y}+{h} > {s}")

    # create first a grid with default values (undrawn pixels)
    grid = [["\033[31m {}\033[00m" .format("\u25A0") for _ in range(s)] for _ in range(s)]

    # modify it
    for j in range(y, y+h):
        for i in range(x, x+w):
            grid[i][j] = "\033[34m {}\033[00m" .format("\u25A0")

    # print
    for j in range(s-1, -1, -1):
        for i in range(0, s, 1):
            print(grid[i][j], end="")
        print("")


if __name__ == "__main__":
    s = int(sys.argv[1])
    x = int(sys.argv[2])
    y = int(sys.argv[3])
    w = int(sys.argv[4])
    h = int(sys.argv[5])
    alg = int(sys.argv[6]) 
    if alg == 0:
        draw_rectangle_0(s, x, y, w, h)
    else:
        draw_rectangle_1(s, x, y, w, h)