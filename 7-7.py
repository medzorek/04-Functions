def f(binary_number):
    if not binary_number:
        return False
    return all(ch in "01" for ch in binary_number)

if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100"))
