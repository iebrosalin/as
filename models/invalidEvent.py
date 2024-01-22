# Реестр недопустимых событий внешнего периметра
class InvalidEventRange: 
   
    # title - название, effects - эффект/последствия, low-acceptable-high_damage - слабый/допустимый/высокий ущерб.
    def __init__(self, title, effects, low_damage, acceptable_damage, high_damage):
        self.title = title
        self.effects = effects
        self.low_damage = low_damage
        self.acceptable_damage = acceptable_damage
        self.high_damage = high_damage

objects = [InvalidEventRange("подмена сайта", "репутационные потери", "неприменимо", "неприменимо", "неприменимо")]

print(objects[0].title)
print(objects[0].effects)
print(objects[0].low_damage)
print(objects[0].acceptable_damage)
print(objects[0].high_damage)