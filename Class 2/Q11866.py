import sys
from collections import deque

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().rstrip().split())
    josephus_list = deque(list(range(1, N + 1)))
    print('<', end='')

    while len(josephus_list) > 1:
        josephus_list.rotate(-K + 1)
        print(f'{josephus_list.popleft()}, ', end='')

    print(f'{josephus_list.pop()}>', end='')
