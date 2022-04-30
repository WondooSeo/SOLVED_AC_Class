import sys
from collections import deque

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    card_queue = deque(list(range(1, N+1)))

    while len(card_queue) > 1:
        card_queue.popleft()
        card_queue.rotate(-1)

    print(card_queue[0])
