import sys

def prime_sleve(n):
    sleve = [1]*(n+1)
    sleve[0], sleve[1] = 0, 0
    for i in range(2, int(n**0.5)+1):
        if sleve[i] == 1:
            temp = i*2
            while temp <= n:
                sleve[temp] = 0
                temp += i

    return sleve

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    is_prime = list(map(int, sys.stdin.readline().rstrip().split()))
    now_sleve = prime_sleve(max(is_prime))
    count = 0

    for now_num in is_prime:
        if now_sleve[now_num] == 1:
            count += 1

    print(count)
