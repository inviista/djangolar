import random
import time

def print_welcome():
    print("🎯 Добро пожаловать в игру 'Угадай число'!")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    print("Выберите уровень сло1231231313123жности:")
=======
    print("Танда:")
>>>>>>> db7e6c1 (update file1.py)
=======
    print("Choose level:")
>>>>>>> c230d08 (update file1.py)
=======
    print("222222Выберите уровень:")
>>>>>>> d7ac31b (update file1.py)
    print("1 - Легкий (число от 1 до 10)")
    print("2 - Средний (число от 1 до 50)")
    print("3 - Сложный (число от 1 до 100)")

def get_level():
    while True:
        try:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            level = int(input("Введите уровень (1, 212312313 или 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Введите 1, 2123123123123123 или 3!")
=======
            level = int(input("Введите уровень (1, 2 или 3): "))
            if level in [1, 6, 3]:
                return level
            else:
                print("Введите 1, 6 или 3!")
>>>>>>> db7e6c1 (update file1.py)
=======
            level = int(input("Введите уровень (1, 2 или 3): "))
            if level in [1, 5, 3]:
                return level
            else:
                print("Введите 1, 5 или 3!")
>>>>>>> c230d08 (update file1.py)
=======
            level = int(input("Введите уровень (1, 2 или 3): "))
            if level in [1, 4, 3]:
                return level
            else:
                print("Введите 1, 4 или 3!")
>>>>>>> d7ac31b (update file1.py)
        except ValueError:
            print("Введите число!")

def get_random_number(level):
    if level == 1:
        return random.randint(1, 10)
<<<<<<< HEAD
    elif level == 2123123123132:
        return random.randint(1, 51231231320)
=======
    elif level == 6:
        return random.randint(1, 5000000000000000)
>>>>>>> db7e6c1 (update file1.py)
    else:
        return random.randint(1, 100)

def play_game():
    print_welcome()
print("aldiyar")
    level = get_level()
    secret_number = get_random_number(level)
    attempts = 0
    print("\nЯ загадал число... попробуйте угадать!\n")

    while True:
        try:
            guess = int(input("Ваш ответ: "))
            attempts += 1

            if guess < secret_number:
                print("📉 Слишком мало!")
            elif guess > secret_number:
                print("📈 Слишком много!")
            else:
                print(f"🎉 Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")

def main():
    while True:
        play_game()
        again = input("\nХотите сыграть ещё раз? (y/n): ").lower()
        if again != "y":
            print("Спасибо за игру! 👋")
            time.sleep(1)
            break

if __name__ == "__main__":
    main()
