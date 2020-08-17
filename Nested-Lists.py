# frankencode....
# v2 cleaner with a set
if __name__ == '__main__':
    roster = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())

        roster[name] = score

    second_last_score = sorted(set(roster.values()))[1]
    second_last_name = sorted([k for k, v in roster.items() if v == second_last_score])

    for i in second_last_name:
        print(i)
