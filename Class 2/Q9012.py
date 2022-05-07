import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        now_str = sys.stdin.readline().rstrip()
        now_stack = list()
        for now_chr in now_str:
            if now_chr == ')':
                if len(now_stack) > 0 and now_stack[-1] == '(':
                    now_stack.pop()
                else:
                    now_stack.append(now_chr)
                    break
            else:
                now_stack.append(now_chr)

        print('YES') if len(now_stack) == 0 else print('NO')
