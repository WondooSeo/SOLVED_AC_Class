import sys

if __name__ == '__main__':
    while True:
        now_num = int(sys.stdin.readline().rstrip())
        if now_num == 0:
            break

        now_num = list(map(int, str(now_num)))
        if now_num == list(reversed(now_num)):
            print('yes')
        else:
            print('no')
