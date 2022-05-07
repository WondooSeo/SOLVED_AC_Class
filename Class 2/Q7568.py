import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    dungchi = list()
    for _ in range(N):
        dungchi.append(list(map(int, sys.stdin.readline().rstrip().split())))

    dungchi_rank = list()
    for i in range(N):
        now_rank = 1
        for j in range(N):
            if i == j:
                continue
            else:
                if dungchi[i][0] < dungchi[j][0] and dungchi[i][1] < dungchi[j][1]:
                    now_rank += 1
        dungchi_rank.append(now_rank)

    print(*dungchi_rank)
