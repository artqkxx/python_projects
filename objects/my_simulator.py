from random import *


class CoffeeShop:
    def __init__(self):
        self.money = 0
        self.reputation = 0
        self.coffee_quality = 1
        self.energy = 10

    def make_coffee(self):
        if self.energy <= 0:
            print("У вас недостатньо енергії, щоб готувати каву! Відпочиньте.")
            return

        self.money += 10 + self.coffee_quality
        self.reputation += 1
        self.energy -= 2
        print("Ви приготували каву! +Гроші, +Репутація, -Енергія")

    def buy_supplies(self):
        cost = 15
        self.money -= cost
        self.coffee_quality += 1
        print("Ви купили нові запаси! -Гроші, +Якість кави")

    def rest(self):
        self.energy += 3
        print("Ви відпочили! +Енергія")

    def marketing(self):
        self.reputation += 2
        print("Ви провели маркетингову кампанію! +Репутація")

    def status(self):
        print("\n=== СТАТУС КАВ'ЯРНІ ===")
        print(f"Гроші: {self.money}")
        print(f"Репутація: {self.reputation}")
        print(f"Якість кави: {self.coffee_quality}")
        print(f"Енергія: {self.energy}")
        print("========================\n")

    def is_game_over(self):
        if self.money < -100:
            print("Ви стали банкрутом. Гру закінчено.")
            return True
        if self.reputation > 50:
            print("Кав'ярня стала популярною! Вітаємо з перемогою!")
            return True
        return False


def game_loop():
    cafe = CoffeeShop()

    print("Вітаємо у симуляторі власника кав'ярні!\n")

    while True:
        cafe.status()
        print("Що хочете зробити?")
        print("1 – Приготувати каву")
        print("2 – Купити запаси")
        print("3 – Відпочити")
        print("4 – Маркетинг")
        print("0 – Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            cafe.make_coffee()
        elif choice == "2":
            cafe.buy_supplies()
        elif choice == "3":
            cafe.rest()
        elif choice == "4":
            cafe.marketing()
        elif choice == "0":
            print("Вихід з гри. До зустрічі!")
            break
        else:
            print("Невірна команда!")

        if cafe.is_game_over():
            break



if __name__ == "__main__":
    game_loop()



