import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    now_stack = list()

    for _ in range(N):
        now_cmd = list(sys.stdin.readline().rstrip().split())
        if now_cmd[0] == 'push':
            now_stack.append(int(now_cmd[1]))
        elif now_cmd[0] == 'pop':
            print(-1) if len(now_stack) == 0 else print(now_stack.pop())
        elif now_cmd[0] == 'size':
            print(len(now_stack))
        elif now_cmd[0] == 'empty':
            print(1) if len(now_stack) == 0 else print(0)
        else:
            print(-1) if len(now_stack) == 0 else print(now_stack[-1])
