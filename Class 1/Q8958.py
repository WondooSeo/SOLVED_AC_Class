import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())

    for _ in range(N):
        now_case = list(sys.stdin.readline().rstrip())
        now_streak, now_score = 0, 0

        for now_answer in now_case:
            if now_answer == 'O':
                now_streak += 1
                now_score += now_streak
            else:
                now_streak = 0

        print(now_score)
