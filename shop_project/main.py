print("=== CONSOLE SHOP ===")
print("1 - Реєстрація")
print("2 - Вхід")
print("3 - Показати товар")
print("4 - Купити товар")
print("5 - Пошук товару за назвою")

choice = input("Оберіть дію: ")

if choice == "1":
    import services.auth.register

elif choice == "2":
    import services.auth.login

elif choice == "3":
    import services.show_products

elif choice == "4":
    import services.buy_product



