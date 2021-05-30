class Planet: 
    def __init__(self, name, radius, gravity, system):#kind of like a constructor method
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system
    def rad(self): 
        return f'the radius of {self.name} is {self.radius}'
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'
    

hoth =Planet("Hoth", 20000000, 5.5, "Hoth System")
print(hoth.rad())
print(hoth.orbit())


naboo = Planet("Naboo", 300000, 8, "Naboo System")

print(naboo.rad())
print(naboo.orbit())


listy = [1,2,3,4,5]

for num in listy: 
    print(num)