print("=== CONSOLE SHOP ===")
print("1 - Показати всіх клієнтів")
print("2 - Перевірити баланс клієнта")
print("3 - Збільшити баланс")
print("4 - Зменшити баланс")
print("5 - Пошук товару за назвою")
print("6 - Показ всіх замовлень")
print("7 - Показ всіх послуг")

choice = input("Оберіть дію: ")

if choice == "1":
    exec(open("../services/show_clients.py", encoding="utf-8").read())

elif choice == "2":
    exec(open("../services/balance_checker.py", encoding="utf-8").read())

elif choice == "3":
    exec(open("../services/upper_balance.py", encoding="utf-8").read())

elif choice == "4":
    exec(open("../services/lower_balance.py", encoding="utf-8").read())

elif choice == "5":
    exec(open("../services/find_services.py", encoding="utf-8").read())

elif choice == "6":
    exec(open("../services/show_order.py", encoding="utf-8").read())

elif choice == "7":
    exec(open("../services/show_services.py", encoding="utf-8").read())

else:
    print("Невірний вибір")