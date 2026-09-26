class Person:



    def __init__(self, name, age):  #__ __ id the dunder method, it is a special method in Python that is called when an object is created from a class. It is used to initialize the attributes of the object.

        print("Constructor called")  # This line prints a message indicating that the constructor has been called.
        self.name = name
        self.age = age

harry = Person("Harry", 25)
print(f"Name: {harry.name}, Age: {harry.age}")  # This line prints the name and age of the person object created.      

