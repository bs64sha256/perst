from validators import email, domain, ipv4, url, ipv6
from requests import get, exceptions
from tabulate import tabulate
from config import tables_color, text_color, error_color


def input_check(command: str) -> None:
    if (command == '-h') or (command == '--help'):
        from config import help_list
        print(tables_color+tabulate(help_list, colalign=("center",), tablefmt="grid", showindex="always",
                                    headers="firstrow", stralign='left',maxcolwidths=[60, 60, 60, 60, 60, 60, 60]))
    elif ((command[0:2] == '+7' and len(command) == 12) or (command[0] == '8' and len(command) == 11)) and command[1::].isdigit():
        print('>>> Телефонные номера пока не поддерживаются')
    elif email(command):
        print('>>> EMAIL-адреса пока не поддерживаются')
    elif domain(command):
        print('>>> Доменные имена пока не поддерживаются')
    elif ipv6(command):
        print('>>> IPv6-адреса пока не поддерживаются')
    elif ipv4(command):
        from package import get_data_from_ip
        get_data_from_ip(command)
    elif url(command):
        from package import get_ip_from_url
        from package import get_whois_data_from_url
        from package import get_ssl_certificate
        try:
            response = get(command)
            get_ip_from_url(command)
            get_whois_data_from_url(command)
            get_ssl_certificate(command)
        except exceptions.ConnectionError:
            print(error_color+'>>> [ERROR] Веб-ресурс не найден')
    elif command[0:4] == 'scan':
        from package import scan_ports
        data = command[5::]
        if data == '':
            print(error_color + '>>> [TARGET] Объект сканирования не введен')
        else:
            if url(data):
                from package import extract_useful_links
                from package import xss_test
                extract_useful_links(data)
                from config import xss_payloads
                print(text_color+'\n>>> Поиск XSS-уязвимостей:\n')
                for payload in xss_payloads:
                    if xss_test(data, payload) == 'error':
                        break
                    elif xss_test(data, payload):
                        print(text_color + f"Возможная XSS-уязвимость обнаружена с payload: {payload}")
                    else:
                        print(text_color + f"XSS-уязвимость с payload: {payload} не обнаружена.")
                print('')
            elif ipv4(data):
                scan_ports(data)
            else:
                print(error_color + '>>> [ERROR] Некорректный ввод')
