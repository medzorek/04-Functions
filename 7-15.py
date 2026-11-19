def f(detector):
    people = 0
    for ch in detector:
        if ch == "+":
            people += 1
        elif ch == "-":
            people -= 1
        if people >= 3:
            return True
    return False

if __name__ == "__main__":
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))
    print(f("+-++-++-+---"))
