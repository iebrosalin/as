# Реестр недопустимых событий: меры и средства для предотвращения инцидентов информационной безопасности.
class RecommRange:
    
    # event - событие, proposal - предложение/рекомендация, protection - тип защиты
    def __init__(self, event, proposal, protection):
        self.event = event
        self.proposal = proposal
        self.protection = protection

objects = [RecommRange("Подмена", "WAF - блокирует вредоносные запросы.", "WAF")] 
   
print(objects[0].event)
print(objects[0].proposal)
print(objects[0].protection)    