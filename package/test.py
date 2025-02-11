import requests
import time

def url_stress_test(url: str, num_requests: int = 1000):
    for i in range(num_requests):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Проверка кода ответа (200 OK)
            print(f"Запрос {i+1}/{num_requests}: Успешно, статус {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Запрос {i+1}/{num_requests}: Ошибка: {e}")
        time.sleep(0.1) # Небольшая задержка, чтобы не перегружать слишком быстро

