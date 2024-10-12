numbers = [int(n) for n in input().split()]
if numbers:  # Проверяем, что список не пустой
    numbers = [numbers[-1]] + numbers[:-1]

print(numbers)
