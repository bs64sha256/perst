from art import tprint
from colorama import init, Fore
from dotenv import dotenv_values
from package import input_check
from tabulate import tabulate

# Инициализация конфигурационного файла
config : dict = dotenv_values('.env')

# Функция вывода стартового сообщения и получения пользовательского ввода
def start() -> None:
    # Вывод title сообщения
    tprint("\n [     P E R S T     ]", font="8")
    # Вывод полезных ссылок
    print(f'Наша электронная почта: ', end='')
    print(Fore.LIGHTWHITE_EX + f'{config['EMAIL']}')
    print(f'Наш сайт: {config['SITE']}\nНаш GitHub репозиторий: {config['GITHUB']}\n')
    '''print(Fore.LIGHTWHITE_EX + tabulate([['', 'ВВОД', 'ПРИМЕР', 'ОПИСАНИЕ'],
                                         ['>>>', '[URL]', 'https://www.example.com', 'Выполнение операций по URL-адресу'],
                                         ['>>>', '[IPv4]', '2255.255.255.255', 'Выполнение операций по IPv4-адресу'],
                                         ['>>>', '[email]', 'example@gmail.com', 'Выполнение операций по email'],
                                         ['>>>', '[phone]', '+79999999999', 'Выполнение операций по номеру телефона'],
                                         ['>>>', '[domain]', 'example.com', 'Выполнение операций по доменному имени']],
                                         colalign=("center",), tablefmt="grid", showindex="always", headers="firstrow")+'\n')
    # Обработка ввода в бесконечном цикле'''
    while True:
        command = input(Fore.LIGHTGREEN_EX+'Ввод: ').lower()
        # Функция обработки ввода
        input_check(command=command)

# Главная функция
def main() -> None:
    init(autoreset=True)
    start()

if __name__ == '__main__':
    main()


