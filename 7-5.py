import range_check

num = int(input("A number: "))
res = "yes" if range_check.in_range(num, 2, 15) else "no"
print(f"Number {num} in the range <2,15>: {res}")
