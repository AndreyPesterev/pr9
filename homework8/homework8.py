import random

# Лотерейный билет
ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

# Пользовательский выбор
user_numbers = []
for row in ticket:
    num = int(input(f"Выберите число из {row}: "))
    while num not in row:
        num = int(input(f"Некорректный ввод. Выберите число из {row}: "))
    user_numbers.append(num)

# Случайный выбор
random_numbers = [random.choice(row) for row in ticket]

# Вывод результатов
print(f"Ваши числа: {user_numbers}")
print(f"Случайно выбранные числа: {random_numbers}")

# Подсчет совпадений
matches = set(user_numbers) & set(random_numbers)
if matches:
    print(f"Совпадения: {matches} (Всего: {len(matches)})")
else:
    print("Совпадений нет.")
