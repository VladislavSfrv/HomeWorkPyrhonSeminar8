# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

import sqlite3 as sq

with sq.connect('phonenumbers.db') as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone INTEGER NOT NULL   
                )""")

    #cur.execute("INSERT INTO users(name, phone) VALUES('Михаил', 84325328512)")

    print("Выберите действие с таблицей: ")
    print("1 - Добавить контакт")
    print("2 - Найти контакт ")
    print("3 - Посмотреть все контакты")
    input_number = int(input("Ваше число: "))

    #Добавление контакта
    if input_number == 1:
        name = input("Введите имя контакта: ")
        phone = int(input("Введите номер телефона контакта: "))
        cur.execute(f"INSERT INTO users(name, phone) VALUES('{name}', {phone})")
    
    # Поиск контакта по одному из параметров
    elif input_number == 2:
        print("Выберите по какому параметру искать контакт:")
        print("1 - Имя")
        print("2 - Номер телефона")
        print("3 - Уникальный номер контакта")
        find = int(input("Ваше число: "))
        
        #Поиск по имени
        if find == 1:
            print("Вы выбрали поиск по Имени.")
            find_name = input("Введите точное имя контакта: ")
            cur.execute(f"SELECT * FROM users WHERE name == '{find_name}'")
            result = cur.fetchall()
            print(result)
            
            #Изменение номера телефона
            print("Изменить номер телефона?")
            update_phone = int(input("Введите 1, если хотите изменить номер телефона или введите 2 если хотите удалить контакт, или любое значение чтобы выйти: "))
            if update_phone == 1:
                phone = int(input("Введите новый номер телефона: "))
                cur.execute(f"UPDATE users SET phone = {phone} WHERE name == '{find_name}'")
                print("Контакт успешно изменен.")
                
                #Изменение имени
            elif update_phone >= 3:
                print("Изменить Имя контакта?")
                update_name = int(input("Введите 1, если хотите изменить Имя контакта или любое значение чтобы выйти: "))
                if update_name == 1:
                    name = input("Введите новое имя контакта: ")
                    cur.execute(f"UPDATE users SET name = '{name}' WHERE name == '{find_name}'")
                    print("Контакт успешно изменен.")
            
            #Удаление контакта
            elif update_phone == 2:
                cur.execute(f"DELETE FROM users WHERE name == '{find_name}'")
                print("Контакт успешно удален")
        
        # поиск по номеру телефона
        elif find == 2:
            print("Вы выбрали поиск по номеру телефона.")
            find_phonenumber = int(input("Введите полный номер телефона, без ошибок: "))
            cur.execute(f"SELECT * FROM users WHERE phone == {find_phonenumber}")
            result = cur.fetchall()
            print(result)

            #Изменение номера телефона
            print("Изменить номер телефона?")
            update_phone = int(input("Введите 1, если хотите изменить номер телефона или введите 2 если хотите удалить контакт, или любое значение чтобы выйти: "))
            if update_phone == 1:
                phone = int(input("Введите новый номер телефона: "))
                cur.execute(f"UPDATE users SET phone = {phone} WHERE phone == '{find_phonenumber}'")
                print("Контакт успешно изменен.")
                
                #Изменение имени
            elif update_phone >= 3:
                print("Изменить Имя контакта?")
                update_name = int(input("Введите 1, если хотите изменить Имя контакта или любое значение чтобы выйти: "))
                if update_name == 1:
                    name = input("Введите новое имя контакта: ")
                    cur.execute(f"UPDATE users SET name = '{name}' WHERE phone == {find_phonenumber}")
                    print("Контакт успешно изменен.")
            
            #Удаление контакта
            elif update_phone == 2:
                cur.execute(f"DELETE FROM users WHERE phone == {find_phonenumber}")
                print("Контакт успешно удален")

        #поиск по уникальному номеру
        elif find == 3:
            print("Вы выбрали поиск по id.")
            find_id = int(input("Введите id контакта: "))
            cur.execute(f"SELECT * FROM users WHERE id == {find_id}")
            result = cur.fetchall()
            print(result)

            #Изменение номера телефона
            print("Изменить номер телефона?")
            update_phone = int(input("Введите 1, если хотите изменить номер телефона или введите 2 если хотите удалить контакт, или любое значение чтобы выйти: "))
            if update_phone == 1:
                phone = int(input("Введите новый номер телефона: "))
                cur.execute(f"UPDATE users SET phone = {phone} WHERE id == {find_id}")
                print("Контакт успешно изменен.")
                
                #Изменение имени
            elif update_phone >= 3:
                print("Изменить Имя контакта?")
                update_name = int(input("Введите 1, если хотите изменить Имя контакта или любое значение чтобы выйти: "))
                if update_name == 1:
                    name = input("Введите новое имя контакта: ")
                    cur.execute(f"UPDATE users SET name = '{name}' WHERE id == {find_id}")
                    print("Контакт успешно изменен.")
            
            #Удаление контакта
            elif update_phone == 2:
                cur.execute(f"DELETE FROM users WHERE name == {find_id}")
                print("Контакт успешно удален")
    
    #Просмотр всех контактов
    elif input_number == 3:
        cur.execute("SELECT * FROM users")
        result = cur.fetchall()
        for result in result:
            print(result)
    
    #Обработка исключения
    else:
        print("Введено неверное число.")       