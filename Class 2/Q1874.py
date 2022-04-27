import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    stack, op_list, count = list(), list(), 1
    for _ in range(n):
        now_num = int(sys.stdin.readline().rstrip())
        while count <= now_num:
            stack.append(count)
            op_list.append('+')
            count += 1

        if stack[-1] == now_num:
            stack.pop()
            op_list.append('-')

        else:
            op_list.append('x')
            break

    if op_list[-1] == 'x':
        print('NO')
    else:
        print(*op_list, sep='\n')
