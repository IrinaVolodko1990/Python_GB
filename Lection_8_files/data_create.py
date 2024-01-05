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

