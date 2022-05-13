import sys

def input_block(n):
    block_list = list()
    for _ in range(n):
        now_block = list(map(int, sys.stdin.readline().rstrip().split()))
        for block in now_block:
            block_list.append(block)

    return block_list

if __name__ == '__main__':
    N, M, B = map(int, sys.stdin.readline().rstrip().split())
    mc_block = input_block(N)
    min_time, max_height = sys.maxsize, -1

    min_height, max_height = min(mc_block), max(mc_block)
    for now_height in range(min_height, max_height + 1):
        stacked_block, dug_block = 0, 0
        for i in range(N*M):
            if mc_block[i] < now_height:
                stacked_block += now_height - mc_block[i]
            elif mc_block[i] > now_height:
                dug_block += mc_block[i] - now_height
            else:
                continue

        if stacked_block > dug_block + B:
            continue

        now_time = 2*dug_block + stacked_block
        if now_time <= min_time:
            min_time, max_height = now_time, now_height

    print(min_time, max_height)
