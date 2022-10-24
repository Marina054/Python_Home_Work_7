from logging import write_log

def input_data():
    with open(r'C:\Users\79068\Desktop\Python\Python практика\Домашняя работа\tel_data.txt',encoding='utf - 8') as f:
        first_line = f.readlines()
        const_sur= first_line[0].strip()
        print(const_sur)
    surname =input ("Впишите фамилию: ") 
    with open(r'C:\Users\79068\Desktop\Python\Python практика\Домашняя работа\tel_data.txt',encoding='utf - 8') as f:
        thrid_line = f.readlines()
        const_name = thrid_line[2].strip()
        print(const_name)
    name = input("впишите имя:")
    with open(r'C:\Users\79068\Desktop\Python\Python практика\Домашняя работа\tel_data.txt',encoding='utf - 8') as f:
        fifth_line = f.readlines()
        const_tel = fifth_line[4].strip()
        print(const_tel)
    telephone = input("Впишите телефон:")
    with open(r'C:\Users\79068\Desktop\Python\Python практика\Домашняя работа\tel_data.txt',encoding='utf - 8') as f:
        seventh_line = f.readlines()
        const_dis = seventh_line[6].strip()
        print(const_dis)
    description = input("Впишите описание:")
    write_log(surname, name, telephone, description)
   