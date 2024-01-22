class FormsRange:

    # forms - форма, interaction - взаимодействие, access - открытый доступ
    def __init__(self, forms, interaction, access):
        self.forms = forms 
        self.interaction = interaction
        self.access = access

objects = [FormsRange("Skillbox", "Ведётся через формы обратного звонка.", "Не получено.")]

print(objects[0].forms)
print(objects[0].interaction)
print(objects[0].access)