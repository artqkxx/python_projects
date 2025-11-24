# 1
import doctest

for i in range(1, 6):
    print(str(i) * i)

# 2
passwords = ["qwerty", "12345678", "strongPass", "abc", "mysecurepassword"]

for password in passwords:
    if len(password) >= 8:
        print(f"Пароль '{password}' — сильний ✅")
    else:
        print(f"Пароль '{password}' — слабкий ❌")

# 3
days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Нд"]
plan = ["кардіо", "прес", "біг", "відпочинок", "спина", "ноги", "йога"]

for i in range(len(days)):
    print(f"{i + 1}. {days[i]} — {plan[i]}")


for i in range(1, 6):
    print(i)




    likes = [120, 80, 150, 200, 90]


    average = sum(likes) / len(likes)
    print(f"Середня кількість лайків: {average}")


    print("Пости з результатом вище середнього:")
    for i in range(len(likes)):
        if likes[i] > average:
            print(f"Пост {i + 1}: {likes[i]} лайків")




#1 v2
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for n in numbers:
    if n % 2 == 0:
        print(n)
# 2
words = ["a", "b", "c", "d", "e", "f"]
for w in words:
    if len(w) >= 5:
        print(w)

# 3
nums = [-5, 0, 3, -1, 8, 10, -7]
for n in nums:
    if n > 0:
        print(n)
# 4
words = ["автомобіль", "комп'ютер", "олівець", "океан", "аудіо"]
vowels = ['а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я']

for w in words:
    count = sum(1 for ch in w if ch.lower() in vowels)
    if count > 3:
        print(w)
# 5
numbers = [3, 5, 6, 9, 12, 15, 17]
for n in numbers:
    if n % 3 == 0:
        print(n)
# 6
words = ["кіт", "калина", "яблуко", "ліс", "банан"]
for w in words:
    if "а" in w.lower():
        print(w)
# 7
nums = [-10, 5, -3, 0, 8, -1]
for n in nums:
    if n < 0:
        print(n)
# 8
grades = [5, 8, 10, 12, 7, 11]
for g in grades:
    if g >= 10:
        print(g)
# 9
words = ["Кіт", "собака", "Море", "дерево", "Сонце"]
for w in words:
    if w[0].isupper():
        print(w)
# 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for n in numbers:
    if n < 10:
        print(n)


grades = [5, 8, 10, 12, 7, 11]
for g in grades:
    if g >= 10:
        print(g)



for i in range(1, 6):
    print(str(i) * i)
    print(i)
    print(i | i)
    print(i & i)
    print(i ^ i)

    doctest
    doctest.testmod(verbose=False)
    doctest.testmod(verbose=True)
    quit()
