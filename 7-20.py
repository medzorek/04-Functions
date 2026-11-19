def is_prime(num):
    if num < 2:
        return False
    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            return False
    return True

def f(n):
    count = 0
    candidate = 2
    while True:
        if is_prime(candidate):
            count += 1
            if count == n:
                return candidate
        candidate += 1

if __name__ == "__main__":
    print(f(1))
    print(f(5))
