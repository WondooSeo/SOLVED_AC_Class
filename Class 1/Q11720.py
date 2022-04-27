import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    now_num = sys.stdin.readline().rstrip()
    print(sum(list(map(int, now_num))))
