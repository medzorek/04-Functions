def f(dice):
    if not dice:
        return None
    best_digit = dice[0]
    best_streak = 1
    cur_digit = dice[0]
    cur_streak = 1

    for ch in dice[1:]:
        if ch == cur_digit:
            cur_streak += 1
        else:
            cur_digit = ch
            cur_streak = 1
        if cur_streak > best_streak:
            best_streak = cur_streak
            best_digit = cur_digit

    return int(best_digit)

if __name__ == "__main__":
    print(f("5233165554211"))
    print(f("2133"))
