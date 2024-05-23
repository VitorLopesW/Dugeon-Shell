class generic_character: 
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.current_hp = self.hp
        # Stats
        self.strength = 5
        self.agility = 5
        self.intelligence = 5
        self.luck = 5
        #Status
        self.status = {
            'bleeding': False,
            'poisoned': False,
        }
    def modify_hp(self, value):
        self.current_hp += value
        if self.current_hp > self.hp:
            self.current_hp = self.hp
    def modify_status(self, status, value):
        self.status[status] = value
    def get_status(self, status):
        return self.status[status]
    def status_turn(self):
        if self.status['bleeding']:
            self.current_hp -= 3
        if self.status['poisoned']:
            self.current_hp -= int(self.hp/6)