import sys

def return_alp_dict():
    alp_dict = dict()
    for i in range(ord('a'), ord('z')+1):
        alp_dict[chr(i)] = i - ord('a') + 1

    return alp_dict

if __name__ == '__main__':
    L = int(sys.stdin.readline().rstrip())
    now_str = sys.stdin.readline().rstrip()
    alp_hash = return_alp_dict()
    total_hash = 0
    r, M = 31, 1234567891

    for i in range(len(now_str)):
        total_hash += alp_hash[now_str[i]] * r**i

    print(total_hash % M)
