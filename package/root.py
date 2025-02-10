from colorama import Fore
from validators import email, domain, ipv4, url, ipv6
from requests import get, exceptions
from tabulate import tabulate

import socket

def get_data_from_ip(command: str) -> None:
    print(Fore.LIGHTWHITE_EX + '\n>>> Поиск данных по IPv4-адресу\n')
    import ipwhois
    try:
        results = ipwhois.IPWhois(command).lookup_whois()
        print(Fore.LIGHTWHITE_EX + tabulate([['>>>', 'ПАРАМЕТР', 'ЗНАЧЕНИЕ'],
                                             ['>>>', 'ASN', str(results['asn'])],
                                             ['>>>', 'ASN CIDR', str(results['asn_cidr'])],
                                             ['>>>', 'ДАТА РЕГИСТРАЦИИ ASN', str(results['asn_date'])],
                                             ['>>>', 'СТРАНА', str(results['asn_country_code'])],
                                             ['>>>', 'ОПИСАНИЕ ASN', str(results['asn_description'])],
                                             ['>>>', 'РЕЕСТР ASN', str(results['asn_registry'])],
                                             ['>>>', 'НАЦИОНАЛЬНЫЙ ИНТЕРНЕТ РЕГИСТР', str(results['nir'])],
                                             ['>>>', 'QUERY', str(results['query'])],
                                             ], colalign=("center",), tablefmt="grid", showindex="always",
                                            headers="firstrow", stralign='left', maxcolwidths=[60, 60, 60, 60, 60]))
        for i in range(len(results['nets'])):
            print(Fore.LIGHTWHITE_EX + f'\nNETWORK {i + 1}\n')
            print(Fore.LIGHTWHITE_EX + tabulate([['>>>', 'ПАРАМЕТР', 'ЗНАЧЕНИЕ'],
                                                 ['>>>', 'АДРЕС', str(results['nets'][i]['address'])],
                                                 ['>>>', 'CIDR', str(results['nets'][i]['cidr'])],
                                                 ['>>>', 'ГОРОД', str(results['nets'][i]['city'])],
                                                 ['>>>', 'СТРАНА', str(results['nets'][i]['country'])],
                                                 ['>>>', 'ДАТА СОЗДАНИЯ', str(results['nets'][i]['created'])],
                                                 ['>>>', 'ОПИСАНИЕ', str(results['nets'][i]['description'])],
                                                 ['>>>', 'EMAIL АДРЕСА', str(results['nets'][i]['emails'])],
                                                 ['>>>', 'HANDLE', str(results['nets'][i]['handle'])],
                                                 ['>>>', 'ИМЯ', str(results['nets'][i]['name'])],
                                                 ['>>>', 'ПОЧТОВЫЙ ИНДЕКС', str(results['nets'][i]['postal_code'])],
                                                 ['>>>', 'ДИАПОЗОН', str(results['nets'][i]['range'])],
                                                 ['>>>', 'ШТАТ', str(results['nets'][i]['state'])],
                                                 ['>>>', 'ОБНОВЛЕНО', str(results['nets'][i]['updated'])]],
                                                colalign=("center",), tablefmt="grid", showindex="always",
                                                headers="firstrow", stralign='left', maxcolwidths=[60, 60, 60, 60, 60]))
        print(Fore.LIGHTWHITE_EX + '\n>>> Поиск по базе данных WhoIs\n')
        from whois import whois
        data = whois(command)
        print(Fore.LIGHTWHITE_EX + tabulate([['>>>', 'ПАРАМЕТР', 'ЗНАЧЕНИЕ'],
                                             ['>>>', 'АДРЕС', str(data['address'])],
                                             ['>>>', 'ГОРОД', str(data['city'])],
                                             ['>>>', 'СТРАНА', str(data['country'])],
                                             ['>>>', 'ДАТА РЕГИСТРАЦИИ', str(data['creation_date'])],
                                             ['>>>', 'DNSSEC', str(data['dnssec'])],
                                             ['>>>', 'ДОМЕННОЕ ИМЯ', str(data['domain_name'])],
                                             ['>>>', 'EMAIL АДРЕСА', str(data['emails'])],
                                             ['>>>', 'ДАТА ИСТЕЧЕНИЯ', str(data['expiration_date'])],
                                             ['>>>', 'ИМЯ', str(data['name'])],
                                             ['>>>', 'ИМЕНА СЕРВЕРОВ', str(data['name_servers'])],
                                             ['>>>', 'ОРГАНИЗАЦИЯ', str(data['org'])],
                                             ['>>>', 'РЕФЕРАЛЬНЫЙ URL', str(data['referral_url'])],
                                             ['>>>', 'РЕГИСТРАТОР', str(data['registrar'])],
                                             ['>>>', 'URL РЕГИСТРАТОРА', str(data['registrar_url'])],
                                             ['>>>', 'ПОСРЕДНИК', str(data['reseller'])],
                                             ['>>>', 'ШТАТ', str(data['state'])],
                                             ['>>>', 'СТАТУС', str(data['status'])],
                                             ['>>>', 'ДАТА ОБНОВЛЕНИЯ', str(data['updated_date'])],
                                             ['>>>', 'СЕРВЕР WHOIS', str(data['whois_server'])]],
                                            colalign=("center",), tablefmt="grid", showindex="always",
                                            headers="firstrow", stralign='left', maxcolwidths=[60, 60, 60, 60, 60]))
    except:
        print(Fore.LIGHTRED_EX + '>>> [ERROR] ОШИБКА ПРИ ПОЛУЧЕНИЯ ДАННЫХ')

def get_whois_data_from_url(data: str) -> None:
    print(Fore.LIGHTWHITE_EX + '\n>>> Поиск по базе данных WhoIs:')
    from whois import whois
    whois_data = whois(data)
    try:
        whois_table = [['>>>', 'ПАРАМЕТР', 'ЗНАЧЕНИЕ'],
                           ['>>>', 'АДРЕС', str(whois_data['address'])],
                           ['>>>', 'ГОРОД', str(whois_data['city'])],
                           ['>>>', 'СТРАНА', str(whois_data['country'])],
                           ['>>>', 'ДАТА СОЗДАНИЯ', str(whois_data['creation_date'])],
                           ['>>>', 'АДРЕС', str(whois_data['address'])],
                           ['>>>', 'ПРОТОКОЛ DNSSEC', str(whois_data['dnssec'])],
                           ['>>>', 'ДОМЕННОЕ ИМЯ', str(whois_data['domain_name'])],
                           ['>>>', 'EMAIL АДРЕСЫ', str(whois_data['emails'])],
                           ['>>>', 'ДАТА ИСТЕЧЕНИЯ', str(whois_data['address'])],
                           ['>>>', 'ИМЯ', str(whois_data['name'])],
                           ['>>>', 'ИМЕНА СЕРВЕРОВ', str(whois_data['name_servers'])],
                           ['>>>', 'ОРГАНИЗАЦИЯ', str(whois_data['org'])],
                           ['>>>', 'РЕФЕРАЛЬНЫЙ URL', str(whois_data['referral_url'])],
                           ['>>>', 'ПОЧТОВЫЙ ИНДЕКС', str(whois_data['registrant_postal_code'])],
                           ['>>>', 'РЕГИСТРАТОР', str(whois_data['registrar'])],
                           ['>>>', 'URL РЕГИСТРАТОРА', str(whois_data['registrar_url'])],
                           ['>>>', 'ПОСРЕДНИК', str(whois_data['reseller'])],
                           ['>>>', 'ШТАТ', str(whois_data['state'])],
                           ['>>>', 'ДАТА ОБНОВЛЕНИЯ', str(whois_data['updated_date'])],
                           ['>>>', 'СЕРВЕР WHOIS', str(whois_data['whois_server'])], ]
        print(Fore.LIGHTWHITE_EX + tabulate(whois_table, colalign=("center",), tablefmt="grid", showindex="always",
                                                headers="firstrow", stralign='left',
                                                maxcolwidths=[60, 60, 60, 60, 60, 60, 60]))
    except:
        print(Fore.LIGHTWHITE_EX + f'Данные для {data} не найдены')

def get_ip_from_url(data: str) -> None:
    print(Fore.LIGHTWHITE_EX+'\n>>> Поиск IPv4-адресов хостинг-сервера по URL:')
    try:
        hostname = data.replace('https://', '').replace('http://', '').split('/')[0]
        result = socket.getaddrinfo(hostname, None, socket.AF_INET)  # socket.AF_INET -  указывает на IPv4
        ipv4_addresses = [item[4][0] for item in result]
        for i in range(len(ipv4_addresses)):
            print(Fore.LIGHTWHITE_EX+f'{i}. IPv4-адрес хостинг-сервера для {data} - {ipv4_addresses[i]}')
    except socket.gaierror:
        print(Fore.LIGHTRED_EX+'>>> [ERROR] Ошибка DNS-запроса') # Обработка ошибок DNS-запроса

    print(Fore.LIGHTWHITE_EX + '>>> Поиск IPv6-адресов хостинг-сервера по URL:')
    try:
        result = socket.getaddrinfo(data, None, socket.AF_INET6)
        if result:
            ipv6_addresses = [addr[4][0] for addr in result]  # Извлекаем все IPv6 адреса
            for i in range(len(ipv6_addresses)):
                print(Fore.LIGHTWHITE_EX + f'{i}. IPv6-адрес хостинг-сервера для {data} - {ipv6_addresses[i]}')
        else:
            print(Fore.LIGHTWHITE_EX+'Не найдено...') # Возвращаем пустой список, если адреса не найдены
    except socket.gaierror as e:
        print(Fore.LIGHTRED_EX+'>>> [ERROR] Ошибка DNS-запроса')

def get_ssl_certificate(data: str):
    import ssl
    try:
        hostname = data.split('://')[1].split('/')[0] # Извлекаем имя хоста
        port = 443 # Порт по умолчанию для HTTPS
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as sslsock:
                certificate = sslsock.getpeercert()
                table = [['>>>', 'ПАРАМЕТР', 'ЗНАЧЕНИЕ'],
                         ['>>>', 'ТИП СЕРТИФИКАТА', str(certificate['subject'])],
                         ['>>>', 'ISSUER', str(certificate['issuer'])],
                         ['>>>', 'СЕРИЙНЫЙ НОМЕР', str(certificate['serialNumber'])],
                         ['>>>', 'РЕГИСТРАЦИЯ', str(certificate['notBefore'])],
                         ['>>>', 'ИСТЕЧЕНИЕ', str(certificate['notAfter'])],
                         ]
                print(Fore.LIGHTWHITE_EX + f"\n>>> SSL Сертификат для {data}:\n")
                # Можно вывести различные атрибуты сертификата
                print(Fore.LIGHTWHITE_EX + tabulate(table, colalign=("center",), tablefmt="grid", showindex="always",
                      headers="firstrow", stralign='left', maxcolwidths=[60, 60, 60, 60, 60]))
    except ssl.SSLError as e:
        print(Fore.LIGHTRED_EX+">>> [ERROR] Ошибка SSL")
        return None
    except socket.gaierror as e:
        print(Fore.LIGHTRED_EX+">>> [ERROR] Ошибка DNS")
        return None
    except Exception as e:
        print(Fore.LIGHTRED_EX+">>> [ERROR] Ошибка SSL")
        return None

def input_check(command: str) -> None:
    if (command == '-h') or (command == '--help'): pass
    elif ((command[0:2] == '+7' and len(command) == 12) or (command[0] == '8' and len(command) == 11)) and command[1::].isdigit():
        print('>>> Телефонные номера пока не поддерживаются')
    elif email(command):
        print('>>> EMAIL-адреса пока не поддерживаются')
    elif domain(command):
        print('>>> Доменные имена пока не поддерживаются')
    elif ipv6(command):
        print('>>> IPv6-адреса пока не поддерживаются')
    elif ipv4(command):
        get_data_from_ip(command)
    elif url(command):
        try:
            response = get(command)
            get_ip_from_url(command)
            get_whois_data_from_url(command)
            get_ssl_certificate(command)
        except exceptions.ConnectionError:
            print(Fore.LIGHTRED_EX+'>>> [ERROR] Веб-ресурс не найден')