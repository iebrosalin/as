# Введение
class Introduction(): 
    
    # Описание переменных (атрибутов)
    Customer = "" # Заказчик
    Executor = "" # Исполнитель
    Service = "Автоматизированный пентест"
    Goal = "Выявление актуальных векторов атак на внешний периметр"
    
    # Задачи, решаемые в ходе оказания Услуг:
    task_list = [
        "• Определение сервисов на внешнем сетевом периметре;",
        "• Обнаружение поддоменов веб-ресурсов, иных IP-адресов, относящиеся к Заказчику;",
        "• Обнаружение интересных для злоумышленника файлов в открытом доступе;",
        "• Составление списка URL-наиболее интересных для атакующего;",
        "• Проверка публично доступных эксплойтов для уязвимостей;",
        "• Подбор наиболее актуальных атак."
    ]

    # Описание функции (методов)
    def set(self, Customer, Executor, Service, Goal):
        self.Customer = Customer
        self.Executor = Executor
        self.Service = Service
        self. Goal =  Goal