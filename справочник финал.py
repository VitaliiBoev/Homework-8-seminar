
import json
phone_book = []
phone_book_file = ".vscode/Python/test project/ДЗ тел справочник/phonebook.json" 
#адрес файла

def show_menu():
    
    print("\nВыберите необходимое действие:\n",
          "1. Отобразить весь справочник\n",
          "2. Найти абонента\n",
          "3. Добавить абонента в справочник\n",
          "4. Изменить абонента\n",
          "5. Удалить абонента\n",
          "6. Сохранить справочник в текстовом формате\n",
          "7. Закончить работу"),
    choice = int(input())
    return choice


def show_search_menu():
    
    print("\nВыберите вариант поиска:\n",
          "1. Поиск по имени\n",
          "2. Поиск по фамилии\n",
          "3. Поиск по телефону\n",
          "4. поиск по комментарию\n",
          "5. отмеить\n")
    search_mod = int(input())
    return search_mod


def load_phone_book(phone_book_file):
    
    with open(phone_book_file, "r") as f:
        return json.load(f)


def sort_data_by_name(data):
    #сортировка
    sorted_data = sorted(data, key=lambda x: (x["surname"], x["name"]))
    return sorted_data


def save_phone_book(phone_book, phone_book_file = ".vscode/Python/test project/ДЗ тел справочник/phonebook.json"):
    #сохраниние контактов
    phone_book = sort_data_by_name(phone_book)
    with open(phone_book_file, "w", encoding="utf-8") as f:
        json.dump(phone_book, f, indent=4, ensure_ascii=False)

    print("="*len("Контакт сохранен"))
    print("Контакт сохранен")
    print("="*len("Контакт сохранен"))


def show_contacts(contacts):
   #показать ввсю книгу

    if contacts == None:
        
        print("Контакт не найден")
        return
    # Вычисление ширины столбцов
    max_name_len = max(len(contact["name"]) for contact in contacts)
    max_surname_len = max(len(contact["surname"]) for contact in contacts)
    max_phone_len = max(len(contact["phone"]) for contact in contacts)
    max_description_len = max(len(contact["description"]) for contact in contacts)

    #? Вывод таблицы в консоль
    # Вывод заголовка
    print("| {:<{}} | {:<{}} | {:<{}} | {:<{}} |".format("Фамилия", max_surname_len, "Имя", max_name_len, "Телефон", max_phone_len, "Описание", max_description_len))
    print("-" * (max_surname_len + max_name_len + max_phone_len + max_description_len + 13))
    # Вывод контактов
    for contact in contacts:
        print("| {:<{}} | {:<{}} | {:<{}} | {:<{}} |".format(
            contact["surname"], max_surname_len, contact["name"], max_name_len, contact["phone"], max_phone_len, contact["description"], max_description_len
        ))


def find_contact(contacts):
    #поиск контактов
    if contacts == None: # Проверка на пустое значение
        print("Неправильный ввод")
    search_mod = show_search_menu() #модуль поиска
    search_str = None
    data = []
    while True:
        if search_mod == 1:
            search_mod = "name"
            search_str = input("Введите имя: ")
            break
        elif search_mod==2:
            search_mod = "surname"
            search_str = input("Введите фамилию: ")
            break
        elif search_mod==3:
            search_mod = "phone"
            search_str = input("Введите телефон: ")
            break
        elif search_mod==4:
            search_mod = "description"
            search_str = input("Введите описание: ")
            break
        elif search_mod==5:
            return None
        search_mod=show_search_menu()
            
    for contact in contacts: 
        if search_str.lower() in contact[search_mod].lower():
            data.append(contact)
    if len(data) > 0: 
        return data
    return None


def add_contact(contacts):
   #добавление контактов
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")
    description = input("Введите описание: ")
    new_contact = {"surname": surname, "name": name, "phone": phone, "description": description}
    contacts.append(new_contact)
    return contacts


def remove_contact(contacts, contact_to_del):
    #удаление контактов
    remove_index = None 
    if contact_to_del == None or len(contact_to_del) == 0:
        print("Контакта не найдено")
        return
    elif len(contact_to_del) == 1:
        remove_index = 0
    else:
        show_contacts(contact_to_del)
        print("Введите порядковый номер контакта")
        remove_index = int(input()) - 1
    contacts.remove(contact_to_del[remove_index])
    return contacts


def edit_contact(contacts):
    #редактирование
    contact = find_contact(contacts)
    choice = None
    if contact is None:
        print("Контакт не найден")
        return
    elif len(contact) > 1:
        show_contacts(contact)
        print("Введите номер контакта")
        choice = int(input()) - 1
    if choice != None and choice + 1 <= len(contact):
        contact = contact[choice]
    else:
        contact = contact[0]

    print("Введите данные для обновления или нажмите Enter :")
    name = input("Имя: ") or contact["name"]
    surname = input("Фамилия: ") or contact["surname"]
    phone = input("Номер телефона: ") or contact["phone"]
    description = input("Описание: ") or contact["description"]
    
    contact["surname"] = surname
    contact["name"] = name
    contact["phone"] = phone
    contact["description"] = description
    return contacts


def save_contacts_to_txt(contacts, file_name = ".vscode/Python/test project/ДЗ тел справочник/phonebook.txt"):
    #сохранение в txt
    if contacts == None:
        
        print("Неверный запрос")
        return
    # Вычисление ширины столбцов
    max_name_len = max(len(contact["name"]) for contact in contacts)
    max_surname_len = max(len(contact["surname"]) for contact in contacts)
    max_phone_len = max(len(contact["phone"]) for contact in contacts)
    max_description_len = max(len(contact["description"]) for contact in contacts)
    # Вывод таблицы в консоль
    with open(file_name, "w") as f:
        f.write("| {:<{}} | {:<{}} | {:<{}} | {:<{}} |\n".format("Фамилия", max_surname_len, "Имя", max_name_len, "Телефон", max_phone_len, "Описание", max_description_len))
        f.write("-" * (max_surname_len + max_name_len + max_phone_len + max_description_len + 13) + "\n")
        for contact in contacts:
            f.write("| {:<{}} | {:<{}} | {:<{}} | {:<{}} |\n".format(
                contact["surname"], max_surname_len, contact["name"], max_name_len, contact["phone"], max_phone_len, contact["description"], max_description_len
            ))


def work_with_phonebook(phone_book_file):
   
    # Запрос пункта меню у пользователя.
    choice = show_menu()
    
    while (choice!=7):
        phone_book = load_phone_book(phone_book_file)
        if choice==1: # Отобразить весь список
            
            show_contacts(phone_book)
        elif choice==2: # Найти абонента
            
            show_contacts(find_contact(phone_book))
        elif choice==3: # Добавить абонента в справочник
            
            add_contact(phone_book)
            save_phone_book(phone_book, phone_book_file)
        elif choice==4: # Изменить абонента
            
            edit_contact(phone_book)
            save_phone_book(phone_book, phone_book_file)
        elif choice==5: # Удалить абонента
            
            remove_contact(phone_book, find_contact(phone_book))
            save_phone_book(phone_book, phone_book_file)
        elif choice==6: # Сохранить справочник в текстовом формате
            
            save_contacts_to_txt(phone_book)
        choice = show_menu()
    
    print("Конец")


work_with_phonebook(phone_book_file)