import sys

def print_sequence(n):
    num = - (n*n)
    add = 1
    for _ in range(n*3):
        print(num, end=" ")
        num += add
        add += 2
    print("")
    

if __name__ == "__main__":
    n = int(sys.argv[1])

    print_sequence(n)