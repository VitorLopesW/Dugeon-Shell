import random

female_names = ['Alice', 'Betty', 'Cathy', 'Diana', 'Eva', 'Fiona', 'Gina', 'Helen', 'Ivy', 'Jenny', 'Kathy', 'Linda', 'Mandy', 'Nancy', 'Olivia', 'Pamela', 'Queenie', 'Rose', 'Sandy', 'Tina', 'Ursula', 'Vicky', 'Wendy', 'Xena', 'Yvonne', 'Zoe']
male_names = ['Andy', 'Bob', 'Charlie', 'David', 'Edward', 'Frank', 'George', 'Henry', 'Ivan', 'Jack', 'Kevin', 'Leo', 'Mike', 'Nathan', 'Oscar', 'Peter', 'Quentin', 'Roger', 'Sam', 'Tom', 'Ulysses', 'Victor', 'William', 'Xavier', 'Yankee', 'Zack']
family_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker']
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Black', 'White', 'Grey', 'Brown', 'Pink', 'Cyan', 'Magenta', 'Lime', 'Teal', 'Indigo', 'Maroon', 'Navy', 'Olive', 'Silver', 'Turquoise', 'Violet', 'Peach', 'Mint', 'Lavender']

class Friendly_NPC:
    def __init__(self):
        self.family_name = random.choice(family_names)
        self.clothes_color = random.choice(colors)
    def loot(self):
        return ['gold', 10]

class Children(Friendly_NPC):
    def __init__(self, gender):
        super().__init__()
        self.gender = gender
        self.name = random.choice(male_names) if gender == 'male' else random.choice(female_names)
        self.age = random.randint(5, 13)
        self.background = random.choice(['Orphan', 'Noble', 'Peasant'])
    def loot(self):
        if self.background == 'Orphan':
            return ['gold', 1]
        elif self.background == 'Noble':
            return ['gold', 50]
        elif self.background == 'Peasant':
            return ['gold', 30]