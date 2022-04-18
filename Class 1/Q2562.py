import sys

if __name__ == '__main__':
    num_list = list()

    for _ in range(9):
        num_list.append(int(sys.stdin.readline().rstrip()))

    print(max(num_list), num_list.index(max(num_list)) + 1, sep='\n')
