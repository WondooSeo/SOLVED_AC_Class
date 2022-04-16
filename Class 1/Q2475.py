import sys

if __name__ == '__main__':
    num_list = map(int, sys.stdin.readline().rstrip().split())
    vcn = 0

    for num in num_list:
        vcn += num**2

    print(vcn % 10)
