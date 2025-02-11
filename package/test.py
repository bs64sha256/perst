import requests
import time
import subprocess
from config import text_color, error_color

def url_stress_test(url: str, num_requests: int = 1000) -> None:
    print(text_color+'>>> Стресс-тестирование по URL [1000] запросов')
    for i in range(num_requests):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Проверка кода ответа (200 OK)
            print(text_color+f">>> Запрос {i+1}/{num_requests}: Успешно, статус {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(error_color+f">>> Запрос {i+1}/{num_requests}: Ошибка: {e}")
        time.sleep(0.1) # Небольшая задержка, чтобы не перегружать слишком быстро

def ipv4_ping_test(ip_address: str, num_pings: int = 1000) -> None:
    print(text_color + '>>> Стресс-тестирование по IPv4 [1000] запросов')
    for i in range(num_pings):
        try:
            result = subprocess.run(['ping', '-c', '1', ip_address], capture_output=True, text=True, check=True)
            print(text_color+f">>> Ping {i+1}/{num_pings}: Успешно")
            print(text_color+f'   >>> {result.stdout}')  # Вывод ping
        except subprocess.CalledProcessError as e:
            print(error_color+f">>> Ping {i+1}/{num_pings}: Ошибка: {e}")
        time.sleep(0.1) # задержка между пингами

