def f(x, y):
    total = 0
    for n in range(x, y + 1):
        if n % 2 == 0 and n % 3 == 0 and n % 4 != 0:
            total += n
    return total

if __name__ == "__main__":
    print(f(1, 20))
    print(f(10, 30))
