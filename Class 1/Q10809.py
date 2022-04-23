import sys

if __name__ == '__main__':
    alp_list = [-1] * 26
    S = list(sys.stdin.readline().rstrip())
    for i in range(len(S)):
        now_loc = ord(S[i]) - ord('a')
        if alp_list[now_loc] == -1:
            alp_list[now_loc] = i

    print(*alp_list)
