import json
import os

class ManagePass:
    @staticmethod
    def get_to_menu():
        choise = input("[+] Вернуться в меню: ")
        if choise == "+":
            os.system('cls' if os.name == "nt" else 'clear')
            menu()

    def add_password(self, website, username, password):
        try:
            with open("password.json", "r") as f:
                passwords = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            passwords = []

        passwords.append({"website": website, "username": username, "password": password})

        with open("password.json", "w") as f:
            json.dump(passwords, f, indent=4)

        os.system("cls" if os.name == "nt" else "clear")
        print("\nПароли успешно добавленны")
        get_password()

def get_password():
    try:
        with open("password.json", "r") as f:
            passwords = json.load(f)
        if not passwords:
            print("Пароли не найдены.")
            return
        print("\nСписок паролей: ")
        for i, pwd in enumerate(passwords, 1):
            print(f"{i}. Сайт: {pwd['website']}, Пользователь: {pwd['username']}, Пароль: {pwd['password']}")
        ManagePass.get_to_menu()  # Вызываем функцию только после вывода всех паролей
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

def menu(): 
    manager = ManagePass()  # Создаем объект класса ManagePass

    while True:  # Сделаем меню цикличным
        os.system('cls' if os.name == "nt" else 'clear')
        action = input("\n\nВыберите действие:\n[1] Посмотреть список паролей\n[2] Добавить новый пароль\n[3] Выйти\n\n")
        
        if action == "1":
            os.system('cls' if os.name == "nt" else 'clear')
            get_password()
        elif action == "2":
            os.system('cls' if os.name == "nt" else 'clear')
            website = input("Введите название сайта: ")
            username = input("Введите ник на сайте: ")
            password = input("Введите пароль: ")
            manager.add_password(website, username, password)  # Добавление пароля
        elif action == "3":
            print("Выход из программы")
            break  # Выход из цикла и завершение программы
        else:
            os.system('cls' if os.name == "nt" else 'clear')
            print("Неверное действие. Пожалуйста, попробуйте снова")

if __name__ == "__main__":
    menu()
