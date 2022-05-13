import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    counting_sort = [0] * 10000

    for _ in range(N):
        counting_sort[int(sys.stdin.readline().rstrip())-1] += 1

    for i in range(10000):
        for j in range(counting_sort[i]):
            print(i+1, end='\n')
