import sys
from bisect import bisect_left, bisect_right

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    card_list = list(map(int, sys.stdin.readline().rstrip().split()))
    M = int(sys.stdin.readline().rstrip())
    want_list = list(map(int, sys.stdin.readline().rstrip().split()))
    card_list.sort()

    for want_num in want_list:
        b_right = bisect_right(card_list, want_num)
        b_left = bisect_left(card_list, want_num)
        print(b_right - b_left, end=' ')
