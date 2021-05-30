class Planet: 
    def __init__(self):#kind of like a constructor method
        self.name = 'Hoth'
        self.radius = 2000000
        self.gravity = 5.5
        self.system = 'Hoth System'

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'
    

hoth =Planet()
print(f'radius is {hoth.radius}')
print(hoth.orbit())
