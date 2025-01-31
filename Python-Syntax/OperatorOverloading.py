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

    # Operator Overloading 
    # When creating the new puppy we don’t know it’s birthday. Pick the
    # first dog’s birthday plus one year. The speakText will be the
    # concatenation of both dog’s text. The dog on the left side of the +
    # operator is the object referenced by the "self" parameter. The
    # "otherDog" parameter is the dog on the right side of the + operator.

    #Other examples of operator overloading 
    # __add__(self, other)  self + other
    # __sub__(self, other)  self - other
    # __mul__(self, other)  self * other
    # __truediv__(self, other)  self / other
    # __eq__(self, other)  self == other
    # __lt__(self, other)  self < other
    # __len__(self)  len(self)
    # __str__(self)  print(self)
    # __float__(self)  float(self) i.e cast
    # __pow__  self**other
    def __add__(self,otherDog):
        return Dog("Puppy of " + self.name + " and " + otherDog.name, self.month, self.day, self.year + 1, self.speakText + otherDog.speakText)
    
def main():
    boyDog = Dog("Mesa", 5, 15, 2004, "WOOOOF")
    girlDog = Dog("Sequoia", 5, 6, 2004, "barkbark")
    puppy = boyDog + girlDog
    print(puppy.speak())
    print(puppy.getName())

if __name__ == "__main__":
    main()