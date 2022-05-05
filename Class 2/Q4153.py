import sys

if __name__ == '__main__':
    while True:
        now_case = list(map(int, sys.stdin.readline().rstrip().split()))
        if now_case[0] == now_case[1] == now_case[2] == 0:
            break
        now_case.sort()

        if now_case[2]**2 == now_case[0]**2 + now_case[1]**2:
            print('right')
        else:
            print('wrong')
