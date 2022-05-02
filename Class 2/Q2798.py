import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().rstrip().split())
    card_list = list(map(int, sys.stdin.readline().rstrip().split()))
    max_card_sum = -1

    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                now_card_sum = card_list[i] + card_list[j] + card_list[k]
                if max_card_sum < now_card_sum <= M:
                    max_card_sum = now_card_sum

    print(max_card_sum)
