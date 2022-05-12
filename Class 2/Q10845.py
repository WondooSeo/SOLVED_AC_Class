import sys
from collections import deque

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    now_queue = deque(list())

    for _ in range(N):
        now_cmd = list(sys.stdin.readline().rstrip().split())
        if now_cmd[0] == 'push':
            now_queue.append(int(now_cmd[1]))
        elif now_cmd[0] == 'pop':
            print(-1) if len(now_queue) == 0 else print(now_queue.popleft())
        elif now_cmd[0] == 'size':
            print(len(now_queue))
        elif now_cmd[0] == 'empty':
            print(1) if len(now_queue) == 0 else print(0)
        elif now_cmd[0] == 'front':
            print(-1) if len(now_queue) == 0 else print(now_queue[0])
        else:
            print(-1) if len(now_queue) == 0 else print(now_queue[-1])
