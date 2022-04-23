import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    int_list = list(map(int, sys.stdin.readline().rstrip().split()))
    print(min(int_list), max(int_list))
