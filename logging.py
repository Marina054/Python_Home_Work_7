from datetime import datetime



FILE_NAME = "tel_spr.csv"

def write_log(surname, name, telephone, description):
    with open(FILE_NAME, "a", encoding="UTF-8") as f:
        f.write(f"{datetime.now().strftime('%d.%m.%Y %H:%M')}\n Введены данные:\n Фамилия: {surname} Имя: {name} Телефон: {telephone} Описание: {description}\n")


def read_log():
    with open(FILE_NAME, "r", encoding="UTF_8") as f:
        print(f.read())
