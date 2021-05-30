"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    def __init__(self):
        self.items = []
        
    
    def addItem(self, stringy):
        self.items.append(stringy)
    
    def getClassiness(self):
        score = 0
        for item in self.items:
            if item == "tophat": 
                score +=2
                
            if item == "bowtie":
                score +=4
                
            if item == "monocle":
                score +=5
            
        
        return score
            

# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.items)
print(me.getClassiness())
print("_________________________-")

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.items)
print(me.getClassiness())
print("_________________________-")

me.addItem("bowtie")
print(me.items)
# Should be 15
print(me.getClassiness())
print("_________________________-")
print(me.items)

