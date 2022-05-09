import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    member_info = list()
    for _ in range(N):
        now_age, now_name = sys.stdin.readline().rstrip().split()
        member_info.append([int(now_age), now_name])

    member_info.sort(key=lambda x: x[0])
    for now_member_info in member_info:
        print(*now_member_info)
        