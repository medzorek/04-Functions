def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False
    check = (int(product_code[0]) + int(product_code[1]) + int(product_code[2])) % 7
    return check == int(product_code[3])

if __name__ == "__main__":
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))
