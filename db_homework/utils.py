def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Введіть число!")


def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Введіть число!")
