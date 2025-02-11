from config import text_color, error_color, tables_color

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

def extract_useful_links(data: str) -> None:
    from tabulate import tabulate
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