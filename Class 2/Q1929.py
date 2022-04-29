import sys

def prime_sleve(m, n):
    sleve = [1] * (n+1)
    sleve[0], sleve[1] = 0, 0
    for i in range(2, int(n**0.5)+1):
        if sleve[i] == 1:
            temp = i*2
            while temp <= n:
                sleve[temp] = 0
                temp += i

    for j in range(m, n+1):
        if sleve[j] == 1:
            print(j)

if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().rstrip().split())
    prime_sleve(M, N)
