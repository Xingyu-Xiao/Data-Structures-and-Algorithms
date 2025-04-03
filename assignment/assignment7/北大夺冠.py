m = int(input())
pass_num = {}
sub_num = {}
for i in range(m):
    team, problem, score = input().split(',')
    if score == 'yes':
        if team in pass_num:
            pass_num[team].add(problem)
        else:
            pass_num[team] = {problem}
    sub_num[team] = sub_num.get(team, 0) + 1
s = [(team, len(pass_num.get(team, [])), sub_num[team]) for team in sub_num]
s.sort(key=lambda x: (-x[1], x[2], x[0]))
for i, (team, pass_n, sub_n) in enumerate(s):
    if i == 12:
        break
    print(f'{i+1} {team} {pass_n} {sub_n}')
