import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\n📭 Список задач пуст!")
    else:
        print("\n📋 Ваши задачи:")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['title']} {status}")

def add_task(tasks):
    title = input("\nВведите название задачи: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Задача добавлена!")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("\nВведите номер задачи для отметки: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Задача выполнена!")
    except (ValueError, IndexError):
        print("Некорректный номер!")

def main():
    tasks = load_tasks()
    while True:
        print("\nМеню:")
        print("1 - Показать задачи")
        print("2 - Добавить задачу")
        print("3 - Отметить выполненной")
        print("4 - Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            print("👋 До свидания!")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
