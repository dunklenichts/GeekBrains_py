n = input('Enter n: ')
if n.isdigit():
    n = int(n)
    sum = n + (n * 10 + n) + (n * 100 + n * 10 + n)
    print(f"{n} + {(n * 10 + n)} + {(n * 100 + n * 10 + n)} = {sum}")
else:
    print('Enter an integer n')