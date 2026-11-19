def f(amount_to_pay):
    coins = 0
    for denom in [5, 2, 1]:
        coins += amount_to_pay // denom
        amount_to_pay %= denom
    return coins

if __name__ == "__main__":
    print(f(23))
    print(f(8))
    print(f(2))
    print(f(0))
