a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

squares = [i**2 for i in range(a+1, b)] if a < b else [i**2 for i in range(b+1, a)]
print(squares)
