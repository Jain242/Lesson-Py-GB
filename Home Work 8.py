# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

def print_file(file_path):
    with open(file_path, "r", encoding = "utf-8") as f:
        print(f.read())

def import_contacts(file_path, people):
    with open(file_path, "r", encoding = "utf-8") as f:
        for line in f:
            people.append(line.strip().split(" "))

def export_contacts(file_path, people):
    with open(file_path, "w", encoding = "utf-8") as f:
        for contact in people:
            f.write(f"{contact[0]} {contact[1]} {contact[2]} {contact[3]}\n")    

def delete_contact(file_path, people):
    key = input("Введите имя, фамилию, отчество: ")
    find_contact =[]
    for contact in people:
        if (key.lower() in contact[0].lower() or 
            key.lower() in contact[1].lower() or
            key.lower() in contact[2].lower() or
            key.lower() in contact[3].lower()):
            find_contact.append(contact)
    if find_contact:
        print("Найдены следующие контакты:")
        j = 1
        for i in find_contact:
            print(f"{j}. {i[0]} {i[1]} {i[2]} {i[3]}")
            j +=1   
        number = int(input("Введите номер контакта:"))
        if number <= len(find_contact) and number >= 1:
            contact_to_delete = find_contact[number - 1]
            print(f"Вы выбрали контак: {contact_to_delete[0]} {contact_to_delete[1]} {contact_to_delete[2]} {contact_to_delete[3]}")
            choice = input('Если действительно хотите его удалить нажмите y, если нет n:  ')
            if choice.lower() == 'y':
                people.remove(contact_to_delete)
                print("Контакт успешно удален!")                
            else:
                print("Удаление отменено")
                    
        else:
            print("Не верно выбрали контакт!")
    else:
        print("Контакты не найдены!")



        
def change_contact(file_path, people):
    key = input("Введите имя, фамилию, отчество или номер контакта: ")
    find_contact =[]
    for contact in people:
        if (key.lower() in contact[0].lower() or 
            key.lower() in contact[1].lower() or
            key.lower() in contact[2].lower() or
            key.lower() in contact[3].lower()):
            find_contact.append(contact)
    if find_contact:
        print("Найдены следующие контакты:")
        j = 1
        for i in find_contact:
            print(f"{j}. {i[0]} {i[1]} {i[2]} {i[3]}")
            j +=1   
        number = int(input("Введите номер контакта, который хотите изменить:"))
        if number <= len(find_contact) and number >= 1:
            contact_change = find_contact[number - 1]
            print(f"Вы выбрали контакт: {contact_change[0]} {contact_change[1]} {contact_change[2]} {contact_change[3]}")
            print("Введите новые данные для контакта:")
            name = input("Введите новое имя: ")
            patronymic = input("Введите новое отчество: ")
            surname = input("Введите новую фамилию: ") 
            phone_number = input("Введите новый номер телефона: ")
            people.remove(contact_change)
            contact_change[1] = surname
            contact_change[0] = name
            contact_change[2] = patronymic
            contact_change[3] = phone_number
            people.append(contact_change)        
        else:
            print("Не верно выбрали контакт!")
    else:
        print("Контакты не найдены!")
    pass       



def write_contact(file_path):
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    surname = input("Введите фамилию: ")
    phone_number = input("Введите номер телефона: ")
    with open(file_path, "a", encoding = "utf-8") as f:
        f.write (f"{name} {patronymic} {surname} {phone_number}\n" )
     

def search_contact(file_path):
    key = input("Введите значение для поиска: ")
    with open(file_path, "r", encoding = "utf-8") as f:
        for i in f.readlines():
            if key in i:
                print(i)

#main

def main():
    contacts =[]
    file_path = "text.txt"
     
    
    while True:
        print("__________Инсрукция____________")
        print("1. Записать номер")
        print("2. Вывести данные")
        print("3. Поиск по справочнику")
        print("4. Удалить контакт")
        print("5. Изменить контакт")
        print("6. Выход")
        choice = input("Введите номер действия: ")       
        match choice:
            case "1":
                write_contact(file_path)
            case "2":
                print_file(file_path)
            case "3":
                search_contact(file_path)
            case "4":
                import_contacts(file_path, contacts)
                delete_contact(file_path, contacts)
                export_contacts(file_path, contacts)
            case "5":
                import_contacts(file_path, contacts)
                change_contact(file_path, contacts)
                export_contacts(file_path, contacts)
            case "6":
                break



if __name__ == '__main__':
    main()