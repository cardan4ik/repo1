# -*- coding: utf-8 -*-
#
from handlers import (parse_input, EXIT_COMMANDS, AVAILABLE_COMMANDS)


def run():
    print("Start running")  # печать "Start running"
    print('***********************************************************')
    storage = {}  # Здесь создаем хранилище для значений (словарь)
    while True:  # Работаем пока есть флаг (запускаем цикл)
        cmd, args = parse_input()  # Обращаемся к функции, парсим ввод, нас интересует первое слово и остаток
        if cmd in EXIT_COMMANDS:  # Если команда на выход, то выставляем флаг в false и выходим на следующей итерации
            break
        else:
            try:
                storage = AVAILABLE_COMMANDS[cmd](args, storage)  # Достаем нужный обработчик из хранилища обработчиков
            except Exception as err:
                print('Ошибка при запуске {}:'.format(cmd), err)  # выводим ошибку которая возникает при запуске функций
    print("Exited.")


if __name__ == "__main__":  # проверяем условия что данную программу запускаем напрямую
    run()  # обращаемся к функции run()
