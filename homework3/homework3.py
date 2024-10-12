numbers = []
while True:
    n = input()
    if n == 'end':
        break
    numbers.append(int(n))

print([x for x in numbers if x % 2 != 0])
