tasks = []


def add_task():
    global tasks
    new_tasks = input('Введите список задач через запятую: ')
    if ', ' in new_tasks:
        print(f'    Задачи {new_tasks} добавлены в список')
        new_tasks = new_tasks.split(', ')
        tasks += new_tasks
    else:
        tasks.append(new_tasks)
        print(f'    Задача «{new_tasks}» добавлена в список')


def list_tasks():
    if not tasks:
        print("    Пока список дел пуст.")
    else:
        print('    Список дел:')
        for index, task in enumerate(tasks):
            print(f'    Задача №{index+1}: {task}')


def delete_task():
    if not tasks:
        print("    Пока список дел пуст.")
    else:
        list_tasks()
        task_to_delete = int(input('Введите номер задачи, которая будет удалена: '))
        try:
            if 1 <= task_to_delete < len(tasks) + 1:
                del tasks[task_to_delete - 1]
                print(f'    Задача под номером {task_to_delete} была удалена.')
            else:
                print(f'    Задачи под номером {task_to_delete} не существует.')
        except:
            print('    Введенное значение некорректно. Попробуйте снова.')


if __name__ == '__main__':
    print('Добро пожаловать в приложение «Список дел»')
    while True:
        print('\n')
        print('Выберите одну из следующих опций:')
        print('1) создать новую задачу;')
        print('2) удалить задачу;')
        print('3) посмотреть список задач;')
        print('4) выйти.')

        choice = input('Введите число: ')

        if choice == '1':
            add_task()

        elif choice == '2':
            delete_task()

        elif choice == '3':
            list_tasks()

        elif choice == '4':
            break

        else:
            print('    Некорректный запрос. Попробуйте снова.')

    print('    До свидания! Надеюсь увидеть Вас снова.')
