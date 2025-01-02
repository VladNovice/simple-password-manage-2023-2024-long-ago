import json
import os


def add_password(website, username, password):
    with open("password.json", "a") as f:
        f.write(f"{website}:{username}:{password}")
    print("\nПароль успешно добавлен!\n")


def get_password():
    try:
        with open("password.json", "r") as f:
            print("\nПароли:")
            for li in f:
                website, username, password = li.strip().split(":")
                print(f"{website}: {username} пароль: {password}")
    except Exception:
        print("Неизвестная ошибка")

if __name__ == "__main__":
    while True:
        action = input("Выберите действие:\n[1] Посмотреть список паролей\n[2] Добавить новый пароль\n[3] Выйти\n")
        if action == "1":
            get_password()
        elif action == "2":
            website = input("Введите название сайта: ")
            username = input("Введите ник на сайте: ")
            password = input("Введите пароль: ")
            add_password(website, username, password)
        elif action == "3":
            print("Выход из прогрммы")
            break
        else:
            print("Неверное действие. Пожалусйта, попробуйте снова")