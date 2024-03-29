# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# Этапы работы:
# 1. Создать телефонный справочник:             +
#     - открыть файл в режиме добавления (a)    +
# 2. Добавить контакт:                          +
#     - запросить информацию о пользователя      +
#     - перевести информацию в нужный формате    +
#     - открыть файл в режиме добавления (a)     +
#     - добавить созданный контакт в файл        +
# 3. Вывод данных из файла на экран:             +
#     - открыть файл в режиме чтения (r)         +
#     - вывести данные на экран                  +
# 4. Поиск данных:                                         +
#     - запросить варианта поиска                          +
#     - запросить данные для поиска                        +
#     - открыть файл в режиме чтения (r)                   +
#     - сохранить данные в переменную                      +
#     - осуществить поиск по файлу, используя переменную   +
#     - вывести нужную информацию на экран                 +
# 5. Реализовать UI:                            +
#     - вывести варианты меню                   +
#     - получение запроса от пользователя       +
#     - реализация запроса пользователя         +
#     - выход из программы                      +
# 6. Дополнить справочник возможностью копирования данных из одного файла в другой. 
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

def input_name():
    return input("Введите имя: ")


def input_surname():
    return input("Введите фамилию: ")


def input_patronymic():
    return input("Введите отчество: ")


def input_phone():
    return input("Введите номер телефона: ")


def input_adress():
    return input("Введите адрес: ")


def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    adress = input_adress()

    return f"{surname} {name} {patronymic} {phone}\n{adress}\n\n"


def add_contact(contact):
    with open("../phonebook.txt", "a", encoding="UTF-8") as file:
        file.write(contact)


def show_info():
    with open("../phonebook.txt", "r", encoding="UTF-8") as file:
        print(file.read().rstrip())


def search_contact():
    search_num = input(
        "Выберите вариант поиска\n"
        "1. По фамилии\n"
        "2. По имени\n"
        "3. По отчеству\n"
        "4. По номеру телефона\n"
        "5. По городу проживания\n"
        "Ввод: "
    )

    while search_num not in ("1", "2", "3", "4", "5"):
        print("Данные некорректны, введите число из списка выше")
        search_num = input("Введите вариант поиска: ")

    index_var = int(search_num) - 1
    search = input("Введите данные для поиска: ")
    with open("../phonebook.txt", "r", encoding="UTF-8") as file:
        contacts_list = file.read().rstrip().split("\n\n")
    for contact_str in contacts_list:
        contact_el = contact_str.replace("\n", " ").split()
        if search in contact_el[index_var]:
            print(contact_str)


def copy_contact():
    with open("../phonebook.txt", "r", encoding="UTF-8") as file:
        contacts_list = file.read().rstrip().split("\n\n")

    for contact in enumerate(contacts_list, 1):
        print(*contact)

    copy_str = int(input("Введите номер строки для копирования: "))
    index_str = copy_str - 1

    if 1 > copy_str or copy_str > len(contacts_list):
        print("Данные некорректны")
        copy_str = int(input("Введите номер строки для копирования: "))
    
    with open("../copy_phonebook", "a", encoding="UTF-8") as file:
        file.write(contacts_list[index_str] + '\n\n')
    print('Данные успешно скопированы')


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


user_interface()
