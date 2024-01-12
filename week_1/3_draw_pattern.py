import sys

def darw_grid(n, s):
    # create first a grid with default values (undrawn pixels)
    grid = [["\033[00m {}\033[00m" .format("\u25A0") for _ in range(s)] for _ in range(s)]
    for i in range(n+1):
        j = n - i
        grid[i][j] = "\033[31m {}\033[00m" .format("\u25A0")

    for i in range(n+2):
        j = n + 1 - i

        if (i % 2 == n % 2):
            grid[i][j] = "\033[34m {}\033[00m" .format("\u25A0")
        else:
            grid[i][j] = "\033[32m {}\033[00m" .format("\u25A0")

    for j in range(s-1, -1, -1):
        for i in range(0, s, 1):
            print(grid[i][j], end="")
        print("")

if __name__ == "__main__":
    n = int(sys.argv[1])
    s = int(sys.argv[2])

    darw_grid(n, s)