import random
import time

CHOICES = ["камень", "ножницы", "бумага"]

def get_user_choice():
    while True:
        choice = input("\nВыберите (камень / ножницы / бумага): ").lower()
        if choice in CHOICES:
            return choice
        print("Неверный выбор!")

def get_computer_choice():
    return random.choice(CHOICES)

def determine_winner(user, computer):
    if user == computer:
        return "Ничья!"
    elif (user == "камень" and computer == "ножницы") \
        or (user == "ножницы" and computer == "бумага") \
        or (user == "бумага" and computer == "камень"):
        return "Вы выиграли! 🎉"
    else:
        return "Вы проиграли 💀"

def play_game():
    print("\nДобро пожаловать в игру 'Камень, Ножницы, Бумага'!")
    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        print(f"\nВы выбрали: {user}")
        time.sleep(0.5)
        print(f"Компьютер выбрал: {computer}")
        time.sleep(0.5)
        print(determine_winner(user, computer))

        again = input("\nСыграть ещё раз? (y/n): ").lower()
        if again != "y":
            print("Спасибо за игру! 👋")
            break

if __name__ == "__main__":
    play_game()
