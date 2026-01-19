from db_manager import init_db
from clients import *
from memberships import *
from utils import *


def clients_menu():
    while True:
        print("\n--- КЛІЄНТИ ---")
        print("1. Додати клієнта")
        print("2. Переглянути клієнтів")
        print("3. Оновити клієнта")
        print("4. Видалити клієнта")
        print("0. Назад")

        choice = input(">>> ")

        if choice == "1":
            fn = input("Ім'я: ")
            ln = input("Прізвище: ")
            add_client(fn, ln)
            print("✅ Клієнта додано")

        elif choice == "2":
            for c in get_all_clients():
                print(c)

        elif choice == "3":
            cid = input_int("ID клієнта: ")
            fn = input("Нове ім'я: ")
            ln = input("Нове прізвище: ")
            update_client(cid, fn, ln)
            print("✅ Дані оновлено")

        elif choice == "4":
            cid = input_int("ID клієнта: ")
            delete_client(cid)
            print("🗑️ Клієнта видалено")

        elif choice == "0":
            break


def memberships_menu():
    while True:
        print("\n--- АБОНЕМЕНТИ ---")
        print("1. Додати абонемент")
        print("2. Переглянути абонементи")
        print("3. Оновити абонемент")
        print("4. Видалити абонемент")
        print("0. Назад")

        choice = input(">>> ")

        if choice == "1":
            t = input("Тип: ")
            p = input_float("Ціна: ")
            d = input_int("Тривалість (днів): ")
            add_membership(t, p, d)
            print("✅ Абонемент додано")

        elif choice == "2":
            for m in get_all_memberships():
                print(m)

        elif choice == "3":
            mid = input_int("ID абонемента: ")
            t = input("Новий тип: ")
            p = input_float("Нова ціна: ")
            d = input_int("Нова тривалість: ")
            update_membership(mid, t, p, d)
            print("✅ Абонемент оновлено")

        elif choice == "4":
            mid = input_int("ID абонемента: ")
            delete_membership(mid)
            print("🗑️ Абонемент видалено")

        elif choice == "0":
            break


def buy_membership():
    clients = get_all_clients()
    memberships = get_all_memberships()

    if not clients or not memberships:
        print("❌ Немає клієнтів або абонементів")
        return

    print("\nКлієнти:")
    for c in clients:
        print(c)

    cid = input_int("ID клієнта: ")

    print("\nАбонементи:")
    for m in memberships:
        print(m)

    mid = input_int("ID абонемента: ")

    client = next(c for c in clients if c[0] == cid)
    membership = next(m for m in memberships if m[0] == mid)

    print(f"\n🎉 Клієнт {client[1]} придбав абонемент {membership[1]}")


def main():
    init_db()

    while True:
        print("\n=== ФІТНЕС-КЛУБ ===")
        print("1. Клієнти")
        print("2. Абонементи")
        print("3. Придбати абонемент")
        print("0. Вийти")

        choice = input(">>> ")

        if choice == "1":
            clients_menu()
        elif choice == "2":
            memberships_menu()
        elif choice == "3":
            buy_membership()
        elif choice == "0":
            break


if __name__ == "__main__":
    main()
