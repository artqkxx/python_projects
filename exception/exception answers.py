# 8
try:
    number = int(input("Введіть число: "))

    if number % 2 == 0:
        print("Число парне.")
    else:
        print("Число непарне.")

except ValueError:
    print("Помилка: введене значення не є числом!")




