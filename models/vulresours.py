# Классификация уровней уязвимостей   
class VulResoursRange:

    def __init__(self, level, valuation, describe):
        self.level = level
        self.valuation = valuation
        self.describe = describe

objects = [VulResoursRange("Критический", "9.0 - 10", "Обнаруженная уязвимость имеет критический уровень. Требуется немедленное реагирование.")]
        
print(objects[0].level)
print(objects[0].valuation)
print(objects[0].describe) 