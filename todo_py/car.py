class Car: # class naming convetions should begin with capital letters, for formality.

    wheels = 4 #class variable - are always the default value of a module.
    #class variable is diffirent because it is declard inside of class but outside of the constructor.

    def __init__(self, make, model, year, color): #<<< A Special method that will construct object for us, also known as the "Constructor".
        self.make = make #<< "self." refers to the object we are currently working on or making.
        self.model = model #<< this variables are called instance variable. declared inside the oonstructor.
        self.year = year
        self.color = color


    def drive(self): #drive object
        print ("This " +self.model+ " is driving") #<< for the current object is printed.


    def stop(self): #stop object
        print("This car is stopped")