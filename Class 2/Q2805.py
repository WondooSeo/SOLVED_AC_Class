import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().rstrip().split())
    log_list = list(map(int, sys.stdin.readline().rstrip().split()))
    bi_left, bi_right = 1, max(log_list)

    while bi_left <= bi_right:
        bi_mid = (bi_left + bi_right)//2
        now_cut_log = 0
        for log in log_list:
            if log > bi_mid:
                now_cut_log += log - bi_mid

        if now_cut_log < M:
            bi_right = bi_mid - 1
        else:
            bi_left = bi_mid + 1

    print(bi_right)
