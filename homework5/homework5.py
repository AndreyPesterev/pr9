numbers = [int(n) for n in input().split()]
print([numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i-1]])
