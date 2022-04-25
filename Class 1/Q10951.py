if __name__ == '__main__':
    while True:
        try:
            # You should use input() on try-except clause
            # sys.stdin.readline().rstrip() will load last \n which causes ValueError
            # input() delete last \n
            A, B = map(int, input().split())
            print(A + B)

        except EOFError:
            break
