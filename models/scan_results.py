# Результаты анализа защищённости веб-ресурсов
class Scan_results:
     
    subdomain = [
        "https://go.skillbox.ru (Личный кабинет)"
    ]

    email_phone = [
        "ekaterina.fufaeva@skillbox.ru",
        "hello@skillbox.ru"
    ]

# Данные форм и API!!!

    Detected_data = "Не обнаруженно"
    Free_access = "Не получено"

    # Актуальные атаки
    Technology_stack = ""
    Attack_vectors = ""
    
# Уязвимости после Акутальных атак!!!
   
    # Обнаруженные средства защиты
    Protection = ""
    Type = ""
    effects = [
        "• Неработоспособности ресурса из-за блокировки запросов к ресурсу, ответов ресурса;",
        "• Отключены нужные правила защита, в исключения для правил внесено слишком много URL-адресов, что создаёт новые дыры в безопасности;",
        "• Отсутствует длительное хранение информации об атаках, из-за чего ретроспективное расследование, аналитику за квартал, год, 5 лет не провести."
    ]

    # Расширение площади атаки
    expansion = [
        "• Перебор доменных имён, с целью обнаружения общих ресурсов, тестовых стендов и т.п.;",
        "• Поиска исходного кода, например, на GitHub, который можно ассоциировать со skillbox.ru;",
        "• Продолжение попыток получения доступа к панели администрирования ресурсом;",
        "• Учитывая размеры организации, то можно трудоустроится разработчиком, тестировщиком или другим IT-специалистом;",
        "• Основой целью тестирования не был личный кабинет учащегося https://go.skillbox.ru, но открытая регистрация позволяет свободно изучать его."
    ]
    
# Уязвимости
class VulnerRange: 

    # vulnerability - уязвимость, description - описание, way - способ исправления, evaluation - базовая оценка
    def __init__(self, vulnerability, description, way, evaluation):
        self.vulnerability = vulnerability
        self.description = description
        self.way = way
        self.evaluation = evaluation

objects = [VulnerRange("CVE-2016-9838", "Возможна повторная регистрация", "Обновление CMS веб-ресурсов до последней версии", "5.0")]

print(objects[0].vulnerability)
print(objects[0].description)
print(objects[0].way)   
print(objects[0].evaluation)   
    