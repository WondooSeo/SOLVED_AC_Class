import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    A = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    M = int(sys.stdin.readline().rstrip())
    is_in_A = list(map(int, sys.stdin.readline().rstrip().split()))

    for find_num in is_in_A:
        bi_left, bi_right = 0, N - 1
        while bi_left <= bi_right:
            bi_mid = (bi_left + bi_right)//2
            if A[bi_mid] <= find_num:
                bi_left = bi_mid + 1
            else:
                bi_right = bi_mid - 1

        if A[bi_right] != find_num:
            print(0)
        else:
            print(1)
