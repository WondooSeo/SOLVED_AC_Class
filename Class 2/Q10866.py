import sys
from collections import deque

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    now_deque = deque(list())

    for _ in range(N):
        now_cmd = list(sys.stdin.readline().rstrip().split())
        if now_cmd[0] == 'push_front':
            now_deque.appendleft(int(now_cmd[1]))
        elif now_cmd[0] == 'push_back':
            now_deque.append(int(now_cmd[1]))
        elif now_cmd[0] == 'pop_front':
            print(-1) if len(now_deque) == 0 else print(now_deque.popleft())
        elif now_cmd[0] == 'pop_back':
            print(-1) if len(now_deque) == 0 else print(now_deque.pop())
        elif now_cmd[0] == 'size':
            print(len(now_deque))
        elif now_cmd[0] == 'empty':
            print(1) if len(now_deque) == 0 else print(0)
        elif now_cmd[0] == 'front':
            print(-1) if len(now_deque) == 0 else print(now_deque[0])
        else:
            print(-1) if len(now_deque) == 0 else print(now_deque[-1])
