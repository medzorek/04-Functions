def f(n):
    return "/".join("*" for _ in range(n))

if __name__ == "__main__":
    print(f(4))
    print(f(1))
