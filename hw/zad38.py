# # Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# # Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# # 1. Программа должна выводить данные
# # 2. Программа должна сохранять данные в текстовом файле
# # 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# from re import split


# def pull_contacts():
#     result = {}
#     with open("contacts.txt", "r", encoding="utf8") as file:
#         for line in file:
#             k, v = line.strip().split(':')
#             result[k] = v
#     return result


# def push_contact(result):
#     with open('contacts.txt', 'w', encoding="utf8") as file:
#         tmp = ''
#         for k, v in result.items():
#             tmp += k + ':' + v + '\n'
#         file.write(tmp)


# def search_contact(n, rslt):
#     if n.isdigit():
#         flag = True
#         for k, v in rslt.items():
#             if v == n or n in v:
#                 print(f'Телефон {v} принадлежит абоненту {k}')
#                 flag = False
#         else:
#             if flag:
#                 print(f'Не найдено ни одного абонента с номером {n}')
#     else:
#         flag = True
#         for i in rslt:
#             if n.lower() in i.lower():
#                 print(f'Абонент {i} и его номер {rslt[i]}')
#                 flag = False
#         else:
#             if flag:
#                 print(f'Нет такого абонента {n}')


# def main():
#     result = pull_contacts()
#     print("Orange book: ", *result.items(), sep='\n')
#     result['Краснова Петра Петровна'] = "22434432"
#     push_contact(result)
#     search_contact(input('Введите имя/фамилию/отчество/телефон: '), result)


# if __name__ == '__main__':
#     main()


# # Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# # Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# # 1. Программа должна выводить данные
# # 2. Программа должна сохранять данные в текстовом файле
# # 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)


# def pull_contacts():
#     result = {}
#     with open("contacts.txt", "r", encoding="utf8") as file:
#         for line in file:
#             k, v = line.strip().split(':')
#             result[k] = v
#     return result


# def push_contact(result):
#     with open('contacts.txt', 'w', encoding="utf8") as file:
#         tmp = ''
#         for k, v in result.items():
#             tmp += k + ':' + v + '\n'
#         file.write(tmp)


# def search_contact(n, rslt):
#     if n.isdigit():
#         flag = True
#         for k, v in rslt.items():
#             if v == n or n in v:
#                 print(f'Телефон {v} принадлежит абоненту {k}')
#                 flag = False
#         else:
#             if flag:
#                 print(f'Не найдено ни одного абонента с номером {n}')
#     else:
#         flag = True
#         for i in rslt:
#             if n.lower() in i.lower():
#                 print(f'Абонент {i} и его номер {rslt[i]}')
#                 flag = False
#         else:
#             if flag:
#                 print(f'Нет такого абонента {n}')


# def main():
#     result = pull_contacts()
#     print("Orange book: ", *result.items(), sep='\n')
#     result['Краснова Петра Петровна'] = "22434432"
#     push_contact(result)
#     search_contact(input('Введите имя/фамилию/отчество/телефон: '), result)


# if __name__ == '__main__':
#     main()


# # Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# # Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# # 1. Программа должна выводить данные
# # 2. Программа должна сохранять данные в текстовом файле
# # 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)


# def pull_contacts():
#     result = {}
#     with open("contacts.txt", "r", encoding="utf8") as file:
#         for line in file:
#             k, v = line.strip().split(':')
#             result[k] = v
#     return result


# def push_contact(result):
#     with open('contacts.txt', 'w', encoding="utf8") as file:
#         tmp = ''
#         for k, v in result.items():
#             tmp += k + ':' + v + '\n'
#         file.write(tmp)


# def search_contact(n, rslt):
#     if n.isdigit():
#         flag = True
#         for k, v in rslt.items():
#             if v == n or n in v:
#                 print(f'Телефон {v} принадлежит абоненту {k}')
#                 flag = False
#         else:
#             if flag:
#                 print(f'Не найдено ни одного абонента с номером {n}')
#     else:
#         flag = True
#         for i in rslt:
#             if n.lower() in i.lower():
#                 print(f'Абонент {i} и его номер {rslt[i]}')
#                 flag = False
#         else:
#             if flag:
#                 print(f'Нет такого абонента {n}')


# def main():
#     while 1:
#         result = pull_contacts()
#         print("""Меню опций:
#         * 1 - посмотреть контакты
#         * 2 - найти контакт по ФИО или телефону
#         * 3 - добавить контакт
#         * 4 - удалить контакт
#         * 5 - изменить контакт
#         * 6 - выход из программы""")

#         if (choice := input()) not in '123456':
#             continue

#         match choice:
#             case '1': print("\nСписок контактов: ", *result.items(), sep='\n')
#             case '2': search_contact(input('Введите имя/фамилию/отчество/телефон: '), result)
#             case '3':
#                 input_items = input(
#                     'Введите "фамилию имя отчество:телефон": ').split(':')
#                 result[input_items[0]] = input_items[1]
#                 push_contact(result)
#             case '4':
#                 del_item = input(
#                     'Введите "фамилию имя отчество" для удаления: ')
#                 del result[del_item]
#                 push_contact(result)
#             case '5':
#                 del_item = input(
#                     'Введите "фамилию имя отчество:телефон" для изменения: ')
#                 input_items = input('Введите "фамилию имя отчество:телефон": ')
#             case '6': break

#     result['Краснова Петра Петровна'] = "22434432"
#     push_contact(result)


# if __name__ == '__main__':
#     main()



