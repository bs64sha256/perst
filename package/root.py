from validators import email, domain, ipv4, url, ipv6
from requests import get, exceptions
from tabulate import tabulate
from config import tables_color, text_color, error_color

import socket

def get_data_from_ip(command: str) -> None:
    print(text_color + '\n>>> Поиск данных по IPv4-адресу\n')
    import ipwhois
    try:
        results = ipwhois.IPWhois(command).lookup_whois()
        print(tables_color + tabulate([['>>>', 'ПАРАМЕТР', 'ЗНАЧЕНИЕ'],
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
            print(text_color + f'\nNETWORK {i + 1}\n')
            print(tables_color + tabulate([['>>>', 'ПАРАМЕТР', 'ЗНАЧЕНИЕ'],
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
        print(text_color + '\n>>> Поиск по базе данных WhoIs\n')
        from whois import whois
        data = whois(command)
        print(tables_color + tabulate([['>>>', 'ПАРАМЕТР', 'ЗНАЧЕНИЕ'],
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
        print(error_color + '>>> [ERROR] ОШИБКА ПРИ ПОЛУЧЕНИЯ ДАННЫХ')

def get_whois_data_from_url(data: str) -> None:
    print(text_color + '\n>>> Поиск по базе данных WhoIs:')
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
        print(tables_color + tabulate(whois_table, colalign=("center",), tablefmt="grid", showindex="always",
                                                headers="firstrow", stralign='left',
                                                maxcolwidths=[60, 60, 60, 60, 60, 60, 60]))
    except:
        print(error_color + f'Данные для {data} не найдены')

def get_ip_from_url(data: str) -> None:
    print(text_color+'\n>>> Поиск IPv4-адресов хостинг-сервера по URL:')
    try:
        hostname = data.replace('https://', '').replace('http://', '').split('/')[0]
        result = socket.getaddrinfo(hostname, None, socket.AF_INET)  # socket.AF_INET -  указывает на IPv4
        ipv4_addresses = [item[4][0] for item in result]
        for i in range(len(ipv4_addresses)):
            print(text_color+f'{i}. IPv4-адрес хостинг-сервера для {data} - {ipv4_addresses[i]}')
    except socket.gaierror:
        print(error_color+'>>> [ERROR] Ошибка DNS-запроса') # Обработка ошибок DNS-запроса

    print(text_color + '>>> Поиск IPv6-адресов хостинг-сервера по URL:')
    try:
        result = socket.getaddrinfo(data, None, socket.AF_INET6)
        if result:
            ipv6_addresses = [addr[4][0] for addr in result]  # Извлекаем все IPv6 адреса
            for i in range(len(ipv6_addresses)):
                print(text_color + f'{i}. IPv6-адрес хостинг-сервера для {data} - {ipv6_addresses[i]}')
        else:
            print(error_color+'Не найдено...') # Возвращаем пустой список, если адреса не найдены
    except socket.gaierror as e:
        print(error_color+'>>> [ERROR] Ошибка DNS-запроса')

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
                print(text_color + f"\n>>> SSL Сертификат для {data}:\n")
                # Можно вывести различные атрибуты сертификата
                print(tables_color + tabulate(table, colalign=("center",), tablefmt="grid", showindex="always",
                      headers="firstrow", stralign='left', maxcolwidths=[60, 60, 60, 60, 60]))
    except ssl.SSLError as e:
        print(error_color+">>> [ERROR] Ошибка SSL")
        return None
    except socket.gaierror as e:
        print(error_color+">>> [ERROR] Ошибка DNS")
        return None
    except Exception as e:
        print(error_color+">>> [ERROR] Ошибка SSL")
        return None

def extract_useful_links(data: str) -> None:
    import requests
    from bs4 import BeautifulSoup

    try:
        response = requests.get(data)
        response.raise_for_status() # Проверка кода ответа (200 OK)

        soup = BeautifulSoup(response.content, "html.parser")

        absolute_links = []
        for link in soup.find_all("a", href=True):
            href = link["href"]
            # Фильтрация ссылок
            if href.startswith("http"):
                absolute_links.append(href)

        print(text_color+'\n>>> Абсолютные ссылки для URL-адреса:\n')
        abs_links_list = [['>>>', 'ССЫЛКА']]
        for link in absolute_links:
            abs_links_list.append(['>>>', str(link)])
        print(tables_color+tabulate(abs_links_list, colalign=("center",), tablefmt="grid", showindex="always",
                                          headers="firstrow", stralign='left', maxcolwidths=[80, 80, 80, 80, 80]))


    except Exception as e:
        print(error_color + f">>> [ERROR] Ошибка при загрузке страницы")

def xss_test(data: str, payload: str):
    import requests
    try:
        requests.get(data)
        try:
            response = requests.get(data, params={"param": payload}) #  Можно добавить другие методы запроса и параметры
            response.raise_for_status() # Проверка кода ответа
            return payload in response.text
        except requests.exceptions.RequestException:
            return False
    except:
        print(error_color + '>>> [ERROR] Веб-ресурс не найден')
        return 'error'


def scan_ports(data: str) -> None:
    import socket
    import threading
    import time


    def check_port(ip_address, port):
        """Проверяет открыт ли порт."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)  # Уменьшаем таймаут для ускорения
                result = sock.connect_ex((ip_address, port))
                if result == 0:
                    return True  # Порт открыт
                else:
                    return False  # Порт закрыт
        except (socket.timeout, OSError) as e:
            return False  # Ошибка соединения

    def scan_port(ip_address, port, results):
        """Сканирует один порт."""
        if check_port(ip_address, port):
            results.append(port)

    def scan_ports(ip_address, port_range):
        """Сканирует заданный диапазон портов."""
        results = []
        threads = []
        start_time = time.time()


        for port in port_range:
            thread = threading.Thread(target=scan_port, args=(ip_address, port, results))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        end_time = time.time()
        elapsed_time = end_time - start_time

        return results, elapsed_time

    ip_address = data
    start_port = 1
    end_port = 65535

    print(text_color+f'\n>>> Сканирование портов на {data} c №{start_port} по №{end_port}')
    port_range = range(start_port, end_port + 1)
    open_ports, elapsed_time = scan_ports(ip_address, port_range)
    if open_ports:
        for port in open_ports:
            print(text_color+f'\nНа {ip_address} открыт порт --------------------- № {port}')
    else:
        print(text_color+'\n>>> [NONE] Открытых портов не найдено')
    print(text_color+f"\nСканирование заняло {elapsed_time:.2f} секунд.\n")


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
        get_data_from_ip(command)
    elif url(command):
        try:
            response = get(command)
            get_ip_from_url(command)
            get_whois_data_from_url(command)
            get_ssl_certificate(command)
        except exceptions.ConnectionError:
            print(error_color+'>>> [ERROR] Веб-ресурс не найден')
    elif command[0:4] == 'scan':
        data = command[5::]
        if data == '':
            print(error_color + '>>> [TARGET] Объект сканирования не введен')
        else:
            if url(data):
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
