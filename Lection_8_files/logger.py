from data_create import *

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
    index_str = int(copy_str) - 1

    if 1 > copy_str or copy_str > len(contacts_list):
        print("Данные некорректны")
        copy_str = int(input("Введите номер строки для копирования: "))
    
    with open("../copy_phonebook", "a", encoding="UTF-8") as file:
        file.write(contacts_list[index_str] + '\n\n')
    print('Данные успешно скопированы')
