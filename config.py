from colorama import Fore

title_color : Fore = Fore.LIGHTGREEN_EX
tables_color : Fore = Fore.LIGHTWHITE_EX
text_color : Fore = Fore.LIGHTWHITE_EX
error_color : Fore = Fore.LIGHTRED_EX
input_color : Fore = Fore.LIGHTGREEN_EX

xss_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<iframe src='javascript:alert('XSS')'></iframe>",
    '"><img src=x onerror=alert("XSS")>',
    "'javascript:alert('XSS')'",
    '"><script>alert("XSS")</script>',
    '%27"><script>alert("XSS")</script>',
    "<script>document.write(document.cookie)</script>",
    "<script>localStorage.setItem('key','value')</script>",
    "<script>sessionStorage.setItem('key','value')</script>",
]

help_list = [['>>>', 'КОМАНДА', 'ПАРАМЕТР', 'ДЕЙСТВИЕ'],
             ['>>>', 'scan', '<URL-адрес>', '1) Сканирование ресурса на уязвимость к XSS-атакам'
                                     '            2) Получение всех абсолютных ссылок на ресурсе'],
             ['>>>', 'scan', '<IPv4-адрес>', '1) сканирование портов в диапазоне от 1 до 65535']]