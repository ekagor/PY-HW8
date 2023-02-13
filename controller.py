import user_interface as ui
import employee_base as wd
import logger as lg
import time
import shutil

base_workers = {}
base_department = {}

def program_start():
    lg.write_log('Запуск: ' + time.strftime('%d.%m.%y %H:%M:%S') + ';')
    global base_workers
    global base_department
    user = ui.user()  
    if user == '9': 
        print('Завершение')
        lg.write_log('Завершение: ' + time.strftime('%d.%m.%y %H:%M:%S') + ';')
        exit()
    with open('employee_base.txt', encoding='utf=8') as dw_file:  
        for line in dw_file:
            base_workers[line[0]] = [el.rstrip('\n') for el in line[1:].split('*') if len(el) > 0]
    lg.write_log('База сотрудников выгружена из файла employee_base.txt')
    shutil.copy('employee_base.txt', 'employee_base_backup.txt')  
    lg.write_log('Резервная копия базы сотрудников employee_base_backup.txt')
    with open('base_department.txt', encoding='utf=8') as dd_file:  
        for line in dd_file:
            base_department[line[0]] = [el.rstrip('\n') for el in line[1:].split('*') if len(el) > 0]
            base_department[line[0]].append(base_department[line[0]].pop().split('%'))
    lg.write_log('База отделов выгружена base_department.txt')
    shutil.copy('base_department.txt', 'base_department_backup.txt')  
    lg.write_log('Резервная копия базы отделов base_department_backup.txt')
    while True:  
        if user == '1':  
            base_workers, base_department = wd.add_worker(base_workers, base_department)
            lg.write_log('Запись сотрудника добавлена')
        elif user == '2':  
            base_department = wd.add_department(base_department)
            lg.write_log('Запись отдела добавлена')
        elif user == '3':  
            base_workers, base_department = wd.edit_worker(base_workers, base_department)
            lg.write_log('Запись сотрудника изменена')
        elif user == '4':  
            base_department = wd.edit_department(base_department)
            lg.write_log('Запись отдела изменена')
        elif user == '5':  
            base_workers, base_department = wd.del_worker(base_workers, base_department)
            lg.write_log('Запись сотрудника удалена')
        elif user == '6':  
            base_workers, base_department = wd.del_department(base_workers, base_department)
            lg.write_log('Запись отдела удалена')
        elif user == '7':  
            print('Сотрудники:')
            for key in base_workers:
                print(key + ' - ', end='')
                print(*base_workers[key], sep='; ', end=';\n')
            print('\nОтделы')
            for key in base_department:
                print(key + ' - ', end='')
                print(*base_department[key], sep='; ', end=';\n')
            print()
            lg.write_log('Вывод в консоль выполнен')
        elif user == '8':  
            print('Выберите вариант экспорта:\n'
                  '1. Данные на одной строке.\n'
                  '2. Данные построчно')
            choice = input('Введите цифру: ')
            while choice not in ('1', '2'):
                print('Такого варианта нет')
                choice = input('Введите цифру: ')
            if choice == '1':  
                with open('export_one_line.csv', 'w', encoding='utf=8') as export_one_line:
                    export_one_line.write('База сотрудников:\n\n')
                    for key_base in base_workers:
                        export_one_line.write('; '.join(base_workers[key_base]) + '\n')
                    export_one_line.write('\n\n')
                    export_one_line.write('База отделов:\n\n')
                    for key_base in base_department:
                        export_one_line.write('; '.join(el if type(el) != list else '; '.join(el)
                                                 for el in base_department[key_base]) + '\n')
                    export_one_line.write('\n')
                print('Экспорт на одной строке выполнен.\n')
                lg.write_log('Данные сохранены export_one_line.csv')
            elif choice == '2':  
                with open('export_multi_line.csv', 'w', encoding='utf=8') as export_multi_line:
                    export_multi_line.write('База сотрудников:\n\n')
                    for key_base in base_workers:
                        export_multi_line.write(';\n'.join(base_workers[key_base]) + '\n')
                        export_multi_line.write('\n')
                    export_multi_line.write('\n\n')
                    export_multi_line.write('База отделов:\n\n')
                    for key_base in base_department:
                        export_multi_line.write(';\n'.join(el if type(el) != list else ';\n'.join(el)
                                                  for el in base_department[key_base]) + '\n')
                        export_multi_line.write('\n')
                    export_multi_line.write('\n')
                print('Экспорт построчно выполнен.\n')
                lg.write_log('Данные сохранены файл export_multi_line.csv')
        elif user == '9':  
            with open('employee_base.txt', 'w', encoding='utf=8') as file_w:
                for key in base_workers:
                    file_w.write(str(key) + '*' + '*'.join(base_workers[key]) + '\n')
            lg.write_log('База сотрудников сохранена employee_base.txt')
            with open('base_department.txt', 'w', encoding='utf=8') as file_d:
                for key in base_department:
                    file_d.write(str(key) + '*' + '*'.join(el if type(el) != list else '%'.join(el)
                                                           for el in base_department[key]) + '\n')
            lg.write_log('База отделов сохранена base_department.txt')
            print('Работа программы завершена')
            lg.write_log('Завершение работы: ' + time.strftime('%d.%m.%y %H:%M:%S') + ';')
            exit()
        user = ui.user()