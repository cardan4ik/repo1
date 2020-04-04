# -*- coding: utf-8 -*-


class InvalidCommand(Exception):
    # создаем новый объект типа эксепшен
    pass  # Оператор-заглушка, равноценный отсутствию операции.


def parse_input():
    raw_input = input('Type command:\n')
    cmd, *args = raw_input.split(" ")  # получаем данные из введенных, отделяем первое слово, пробел и остаток если есть
    # Раскрытие в *args поддерживается только в питоне 3, для неименованных
    # аргументов, * - говорит о том что мы принимаем несколько аргументов в это имя
    cmd = cmd.upper()  # получаем "CMD"
    try:  # делаем проверку на получение верной команды
        if cmd not in AVAILABLE_COMMANDS.keys() and cmd not in EXIT_COMMANDS:  # если нигде нет нашей команды то..
            raise InvalidCommand("Err Type command: {} this command is not available".format(cmd))
            #  ..запускаем собственный тип исключения
    except InvalidCommand as e:  # обрабатываем исключение
        print(e)
    return cmd, args  # .. иначе возвращвем полученные данные


def namein(args):
    try:
        name = args[0].upper()  # делим полученные данные на имя и информацию
        return name
    except Exception as err:
        print('Ошибка ввода данных:', err)
        return


def handle_set(args, storage):  # Обработчик запроса
    name = namein(args)
    data = 'none'
    if name in storage.keys():
        print('Имя: {}, уже существует!'.format(name))
        # спросить о перезаписи и воткнуть функцию замены или чего там еще !   !   !  ! ! ! !!!
    else:
        if len(args) > 1:
            data = args[1]
        if '' != str(name) != 'None':
            storage[name] = data
    return storage


def handle_get(args, storage):
    name = namein(args)
    if name in storage.keys():
        print('info:', storage[name])
    else:
        print('Имя не найдено!')
    return storage


def handle_unset(args, storage):
    name = namein(args)
    if name in storage.keys():
        print('Имя удалено')
        del storage[name]
    else:
        print('Имя не найдено!')
    return storage


def handle_counts(args, storage):
    quantity = 0
    total = 0
    for i in storage:
        quantity = quantity + 1
        if storage[i].isdigit():
            total = total + int(storage[i])
    print('Записей:', quantity, 'Итого:', total)
    return storage


def handle_find(args, storage):
    name = namein(args)
    for i in storage:
        if storage[i] == name:
            print(i)
    return storage


AVAILABLE_COMMANDS = {   # словарь (хранилище) всех доступных обработчиков
    'SET': handle_set,
    'GET': handle_get,
    'UNSET': handle_unset,
    'COUNTS': handle_counts,
    'FIND': handle_find
}
EXIT_COMMANDS = {'', ' ', 'END'}  # Множество значений для выхода
# Множество в python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.
