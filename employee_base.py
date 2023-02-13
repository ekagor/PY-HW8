def find_department(department_base):  
    print('База отделов:')
    for key in department_base:
        print(key + ' - ', end='')
        print(*department_base[key], sep='; ', end=';\n')
    print()
    find_key = input('Введите ключ отдела: ')
    while find_key not in department_base.keys(): 
        print('Не корректный ввод!')
        find_key = input('Введите ключ отдела: ')
    return find_key

def find_worker(workers_base):  
    print('База сотрудников:')
    for key in workers_base:
        print(key + ' - ', end='')
        print(*workers_base[key], sep='; ', end=';\n')
    print()
    find_key = input('Введите ключ сотрудника: ')
    while find_key not in workers_base.keys():
        print('Не корректный ввод!')
        find_key = input('Введите ключ отдела: ')
    return find_key

def del_department(workers_base: dict, department_base): 
    edit_key = find_department(department_base)  
    for key in workers_base:
        if edit_key in workers_base[key][-1]:
            workers_base[key][-1] = 'нет назначения'
    del department_base[edit_key]
    print('Запись отдела удалена.\n')
    return workers_base, department_base

def del_worker(base_workers, base_department):
    edit_key = find_worker(base_workers)  
    for key in base_department:
        if edit_key in base_department[key][2]:
            base_department[key][2].remove(edit_key)
            base_department[key][1] = str(len(base_department[key][2]))
    del base_workers[edit_key]
    print('Сотрудник удален из базы.\n')
    return base_workers, base_department

def edit_department(department_base):  
    edit_key = find_department(department_base)  
    edit_name = input('Введите новое название отдела: ').strip().capitalize()
    department_base[edit_key][0] = edit_name
    print('Отдел переименован.\n')
    return department_base

def edit_worker(base_workers, base_department):  
    edit_key = find_worker(base_workers)
    surname = input('Введите фамилию сотрудника: ').strip().capitalize()
    name = input('Введите имя сотрудника: ').strip().capitalize()
    patronymic = input('Введите отчество сотрудника: ').strip().capitalize()
    telephone = input('Введите телефон сотрудника: ').strip()
    address = input('Введите адрес проживания сотрудника: ').strip()
    position = input('Введите должность сотрудника: ').strip()
    print('Выберите отдел из списка и введите ключ, что-бы создать новый отдел - введите "n".')
    for key in base_department:  
        print(f'{key} - {base_department[key][0]}')
    department = input('Введите отдел: ').strip().lower()
    while department not in [el for el in base_department.keys()] + ['n']:  
        print('Не корректный ввод!')
        department = input('Введите отдел: ')
    if department == 'n':  
        base_department = add_department(base_department)
        department = str(len(base_department))
    if department != base_workers[edit_key][-1]:  
        base_department[base_workers[edit_key][-1]][2].remove(edit_key)
        base_department[base_workers[edit_key][-1]][1] = str(len(base_department[base_workers[edit_key][-1]][2]))
        base_department[department][2].append(edit_key)
        base_department[department][1] = str(len(base_department[department][2]))
    base_workers[edit_key] = [surname, name, patronymic, telephone, address, position, department]
    print('Запись сотрудника изменена.\n')
    return base_workers, base_department

def add_department(department_base: dict): 
    name_department = input('Введите название отдела: ').strip().capitalize()
    department_base[str(len(department_base) + 1)] = [name_department, '', []]
    print('Отдел создан.\n')
    return department_base

def add_worker(base_workers: dict, base_department: dict):  
    surname = input('Введите фамилию сотрудника: ').strip().capitalize()
    name = input('Введите имя сотрудника: ').strip().capitalize()
    patronymic = input('Введите отчество сотрудника: ').strip().capitalize()
    telephone = input('Введите телефон сотрудника: ').strip()
    address = input('Введите адрес проживания сотрудника: ').strip()
    position = input('Введите должность сотрудника: ').strip()
    print('Выберите отдел из списка и введите ключ, что-бы создать новый отдел - введите "n".')
    for key in base_department:  
        print(f'{key} - {base_department[key][0]}')
    department = input('Введите ключ отдела: ').strip().lower()
    while department not in [el for el in base_department.keys()] + ['n']:  
        print('Не корректный ввод!')
        department = input('Введите ключ отдела: ').strip().lower()
    if department == 'n':  #
        base_department = add_department(base_department)  
        department = str(len(base_department))  
    base_workers[str(len(base_workers) + 1)] = [surname, name, patronymic, telephone, address, position, department]
    base_department[department][2].append(str(len(base_workers)))
    base_department[department][1] = str(len(base_department[department][2]))
    print('Сотрудник внесен в базу.\n')
    return base_workers, base_department