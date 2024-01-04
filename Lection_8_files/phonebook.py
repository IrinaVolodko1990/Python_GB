# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# Этапы работы:
# 1. Создать телефонный справочник:             +
#     - открыть файл в режиме добавления (a)    +
# 2. Добавить контакт:
#     - запросить информацию о пользователя      +
#     - перевести информацию в нужный формате    +
#     - открыть файл в режиме добавления (a)
#     - добавить созданный контакт в файл
# 3. Вывод данных из файла на экран:
#     - открыть файл в режиме чтения (r)
#     - вывести данные на экран
# 4. Поиск данных:
#     - запросить варианта поиска
#     - запросить данные для поиска
#     - открыть файл в режиме чтения (r)
#     - осуществить поиск по файлу
#     - вывести нужную информацию на экран
# 5. Реализовать UI:
#     - вывести варианты меню                   +
#     - получение запроса от пользователя       +
#     - реализация запроса пользователя         +
#     - выход из программы                      +

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

    return f'{surname} {name} {patronymic} {phone}\n{adress}\n\n'


def add_contact():
    contact = create_contact()
    with open ('../phonebook.txt', 'a', encoding="UTF-8") as file:
        file.write(contact)
    


def show_info():
    pass


def search_contact():
    pass


def user_interface():
    with open("../phonebook.txt", "a", encoding='UTF-8'):
        pass
    command = '-1'
    while command != '4':
        print("Меню телефонного справочника\n1. Добавить контакт\n2. Вывести на экран\n3. Поиск контакта\n4. Выход из программы")
        command = input("Введите номер выбранного действия: ")

        while command not in ("1", "2", "3", "4"):
            print("Некорректные данные")
            command = input("Введите номер выбранного действия: ")

        if command == "1":
            add_contact()
        elif command == "2":
            show_info()
        elif command == "3":
            search_contact()
        elif command == "4":
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
