from logger import *

def user_interface():
    with open("../phonebook.txt", "a", encoding="UTF-8"):
        pass
    command = "-1"
    while command != "5":
        print(
            "Меню телефонного справочника\n"
            "1. Добавить контакт\n"
            "2. Вывести на экран\n"
            "3. Поиск контакта\n"
            "4. Копирование контакта в новый файл\n"
            "5. Выход из программы"
        )
        command = input("Введите номер выбранного действия: ")

        while command not in ("1", "2", "3", "4", "5"):
            print("Некорректные данные")
            command = input("Введите номер выбранного действия: ")

        if command == "1":
            add_contact(create_contact())
        elif command == "2":
            show_info()
        elif command == "3":
            search_contact()
        elif command == "4":
            copy_contact()
        elif command == "5":
            print("Всего хорошего!")

        # match command:      ##### не работает
        #     case '1':
        #         add_conact()
        #     case '2':
        #         show_info()
        #     case '3':
        #         search_contact()
        #     case '4':
        #         print('Bye-bye-bye')