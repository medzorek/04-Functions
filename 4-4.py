def sum_digits(number):
    total = 0
    for ch in str(abs(number)):
        total += int(ch)
    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')
