import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    min_decom = -1

    for i in range(1, N+1):
        if i + sum(list(map(int, str(i)))) == N:
            min_decom = i
            break

    print(min_decom) if min_decom != -1 else print(0)
