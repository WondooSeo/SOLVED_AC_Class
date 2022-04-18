import sys

if __name__ == '__main__':
    result = 1
    for _ in range(3):
        result *= int(sys.stdin.readline().rstrip())

    result_list = list(map(int, str(result)))
    for i in range(10):
        print(result_list.count(i))
