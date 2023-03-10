import logger as lg

def user():
    command = input('Команды справочника:\n'
                   '1. Добавить сотрудника;\n'
                   '2. Добавить отдел;\n'
                   '3. Редактировать сотрудника;\n'
                   '4. Редактировать отдел;\n'
                   '5. Удалить сотрудника;\n'
                   '6. Удалить отдел;\n'
                   '7. Вывести в консоль;\n'
                   '8. Экспорт;\n'
                   '9. Выход;\n'
                   'Введите команду: ')
    while command not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'): 
        print('Такой команды нет')
        command = input('Введите номер команды: ')
    lg.write_log('Пользователь ввел: ' + command + ';')
    return command