import sys

def fib(n):
    f0, f1 = [1, 0], [0, 1]
    if n > 1:
        for i in range(2, n+1):
            f0.append(f0[i-1] + f0[i-2])
            f1.append(f1[i-1] + f1[i-2])

    print(f0[n], f1[n])

if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())
        fib(N)
