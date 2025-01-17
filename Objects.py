# Creating Objects using this syntext 
# variable = type(other_object_values)
x="22"
y= int(x)
print(y)

# The type is any type or class name in Python, like int, float, str or any other
# type. The other_object_values is a comma-separated sequence of references to other
# objects that are needed by the class or type to create an instance (i.e an object) of that
# type.

z = float('6.3')
w = str(z)
u = list(w) # this results in the list [’6’, ’.’, ’3’]
print(u)

# CallingMethods on Objects

# two kinds of methods in any object-oriented language: mutator
# and accessor methods. Accessor methods access the current state of an object but
# don’t change the object. Accessor methods return new object references when called.
# The upper method is an accessor method. the method upper is called on the object that x refers to. The upper
# accessor method returns a new object, a str object,
x = 'how are you'
y = x.upper()
print(y)

#Mutator Methods

myList = [1, 2, 3]
myList.reverse()
print(myList) # This prints [3, 2, 1] to the screen