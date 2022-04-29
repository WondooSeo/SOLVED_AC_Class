import sys
from collections import deque

if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().rstrip().split())
        now_queue = deque(list(map(int, sys.stdin.readline().rstrip().split())))
        now_queue.insert(M+1, 0)
        count = 0

        while True:
            if now_queue[0] == max(now_queue):
                now_queue.popleft()
                count += 1
                if now_queue[0] == 0:
                    break
            else:
                now_queue.rotate(-1)
                if now_queue[0] == 0:
                    now_queue.rotate(-1)

        print(count)
