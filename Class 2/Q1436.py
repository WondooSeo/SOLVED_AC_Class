import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    now_num, count = 666, 1

    while count < N:
        now_num += 1
        if '666' in str(now_num):
            count += 1

    print(now_num)
