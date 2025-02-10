from art import tprint
from colorama import init, Fore
from dotenv import dotenv_values
from package import input_check
from tabulate import tabulate

from config import tables_color, text_color, input_color

# Инициализация конфигурационного файла
config : dict = dotenv_values('.env')

# Функция вывода стартового сообщения и получения пользовательского ввода
def start() -> None:
    # Вывод title сообщения
    tprint("\n [     P  E  R  S  T     ]", font="8")
    # Вывод полезных ссылок
    print(f'Наша электронная почта: ', end='')
    print(text_color + f'{config['EMAIL']}')
    print(f'Наш сайт: {config['SITE']}\nНаш GitHub репозиторий: {config['GITHUB']}\n')
    print(tables_color + tabulate([['>>>', 'ВВОД', 'ПРИМЕР', 'ОПИСАНИЕ'],
                                         ['>>>', '[URL]', 'https://www.example.com', 'Выполнение OSINT операций по URL-адресу'],
                                         ['>>>', '[IPv4]', '2255.255.255.255', 'Выполнение OSINT операций по IPv4-адресу']],
                                         colalign=("center",), tablefmt="grid", showindex="always", headers="firstrow")+'\n')
    print(text_color+'Введите -h или --help для получения справки\n')
    # Обработка ввода в бесконечном цикле
    while True:
        command = input(input_color+'Ввод: ').lower()
        # Функция обработки ввода

        input_check(command=command)

# Главная функция
def main() -> None:
    init(autoreset=True)
    start()


if __name__ == '__main__':
    main()


