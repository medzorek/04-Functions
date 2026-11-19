def f(number):
    s = str(number)
    total = 0
    for digit in set(s):
        cnt = s.count(digit)
        if cnt > 1:
            total += int(digit) * cnt
    return total

if __name__ == "__main__":
    print(f(1027))
    print(f(230335))
    print(f(513553007))
