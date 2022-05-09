import sys

if __name__ == '__main__':
    K = int(sys.stdin.readline().rstrip())
    num_stack = list()

    for _ in range(K):
        now_num = int(sys.stdin.readline().rstrip())
        if now_num == 0:
            num_stack.pop()
        else:
            num_stack.append(now_num)

    print(sum(num_stack))
