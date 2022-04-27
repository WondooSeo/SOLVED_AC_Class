import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().rstrip().split())
    chess_pan = list()
    for _ in range(N):
        chess_pan.append(list(sys.stdin.readline().rstrip()))
    paint_count = list()

    for i in range(N-7):
        for j in range(M-7):
            count1, count2 = 0, 0
            for k in range(i, i+8):
                for l in range(j, j+8):
                    if (k+l)%2 == 0:
                        if chess_pan[k][l] == 'W':
                            count1 += 1
                        else:
                            count2 += 1
                    else:
                        if chess_pan[k][l] == 'W':
                            count2 += 1
                        else:
                            count1 += 1

            paint_count.append(min(count1, count2))

    print(min(paint_count))
