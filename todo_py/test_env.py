from car import Car


car_1 = Car("chevy", "corvette", 2021, "Green") #upon calling the 'Car' module from 'car.py' it will the ncreate this object with the following parameters values.
car_2 = Car("Ford", "Mustang", 2022, "Black")

Car.wheels = 2 # changes the class variables, after the excution of this code.
car_1.wheels = 3 # changes the 'car_1' only set of wheels.


print(car_1.wheels) #<<< will print 
print(car_2.wheels)