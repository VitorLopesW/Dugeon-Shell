class effect:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

bleed = effect(
    'Bleed', 
    'This attack contain a chance to make the target bleeds, taking 1/6 damage per turn',
    'bleed'
    )