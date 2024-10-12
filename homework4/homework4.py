numbers = [int(n) for n in iter(input, 'end')]
evens = sum(1 for x in numbers if x % 2 == 0)
odds = len(numbers) - evens

print(numbers)
print(f"Четных: {evens}, Нечетных: {odds}")
