import sys

def gcd(a, b):
    while a != 0:
        a, b = b%a, a

    return b

if __name__ == '__main__':
    num1, num2 = map(int, sys.stdin.readline().rstrip().split())
    now_gcd = gcd(num1, num2)
    now_lcm = num1*num2//now_gcd
    print(now_gcd, now_lcm, sep='\n')
