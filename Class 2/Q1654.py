import sys

if __name__ == '__main__':
    K, N = map(int, sys.stdin.readline().rstrip().split())
    lan_list = list()
    for _ in range(K):
        lan_list.append(int(sys.stdin.readline().rstrip()))

    bi_left, bi_right = 1, max(lan_list)
    while bi_left <= bi_right:
        bi_mid = (bi_left + bi_right)//2
        lan_num = 0
        for lan in lan_list:
            lan_num += lan//bi_mid

        if lan_num >= N:
            bi_left = bi_mid + 1
        else:
            bi_right = bi_mid - 1

    print(bi_right)
