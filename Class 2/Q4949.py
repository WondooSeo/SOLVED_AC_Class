import sys

if __name__ == '__main__':
    while True:
        now_str = sys.stdin.readline().rstrip()
        if now_str == '.':
            break
        bracket_list = list()
        is_balanced = True

        for now_chr in now_str:
            if now_chr == '(' or now_chr == '[':
                bracket_list.append(now_chr)
            elif now_chr == ')':
                if len(bracket_list) != 0 and bracket_list[-1] == '(':
                    bracket_list.pop()
                else:
                    is_balanced = False
                    break
            elif now_chr == ']':
                if len(bracket_list) != 0 and bracket_list[-1] == '[':
                    bracket_list.pop()
                else:
                    is_balanced = False
                    break
            else:
                continue

        print('yes') if is_balanced and len(bracket_list) == 0 else print('no')
