class Dog:

    # Constructor
    def __init__(self, name, month, day, year, speakText):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText

    # This is an accessor method. Every method has "self" as its
    # first parameter. The "self" parameter is a reference to the current
    # object. The current object appears on the left hand side of the dot (i.e.
    # the .) when the method is called.
    def speak(self):
        return self.speakText
    
    def getName(self):
        return self.name
    
    def birthDate(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)
    
    # This is a mutator method that changes the speakText of the Dog object.    
    def changeBark(self,bark): 
        self.speakText = bark

boyDog = Dog("Mesa",5,15,2004,"WOOOF")
print(boyDog.speak())