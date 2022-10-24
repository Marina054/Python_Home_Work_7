from meaning import input_data
from logging import read_log

def menu():
    flag = True
    while flag:
        print("приветствуем в программе *телефонный справичник*: ")
        while True:
            print("1 - Ввести данные")
            print("2 - Посмотреть лог")
            print("3 - Выход")
            choice = input()
            if choice not in ["1", "2", "3"]:
                print("Выбран неверный пунк меню")
                continue
            if choice == "1":
                input_data()
                break
            elif choice == "2":
                read_log()
                break
            else:
                flag = False
                break

if __name__=="__main__":
    menu()
    