def odd(n, d):
    if n % d == 0:
        return True


for num in range(1, 101):
    out = ''
    if odd(num, 3):
        out += 'Fizz'

    if odd(num, 5):
        out += 'Buzz'

    if num % 3 != 0 and num % 5 != 0:
        out = num

    print(out)
