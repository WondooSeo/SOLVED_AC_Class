import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    point_list = list()
    for _ in range(N):
        point_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

    point_list.sort(key=lambda x: (x[1], x[0]))
    for point in point_list:
        print(*point)
