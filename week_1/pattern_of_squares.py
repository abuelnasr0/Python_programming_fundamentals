import sys 

def draw_pattern_0(n):
# my algorithm
	for row in range(n+1, 0, -1):
		x = abs( row%3 - 2)
		for col in range(1, row+1):
			if col%3 == x:
				print("\033[34m {}\033[00m" .format("\u25A0"), end="")
			else:
				print("\033[31m {}\033[00m" .format("\u25A0"), end="")
		print("")


def draw_pattern_1(n):
# course Algoritm
        for row in range(n, -1, -1):
                for col in range(0, row+1):
                        if (row + col) % 3 == 0:
                                print("\033[34m {}\033[00m" .format("\u25A0"), end="")
                        else:
                                print("\033[31m {}\033[00m" .format("\u25A0"), end="")
                print("")


if __name__ == "__main__":
	N = int(sys.argv[1])
	alg = int(sys.argv[2])
	if alg == 0:
		draw_pattern_0(N)
	elif alg == 1:
		draw_pattern_1(N)
