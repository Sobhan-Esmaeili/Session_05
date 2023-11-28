# my_lanbda_01 = lambda x: x*2
# print(my_lanbda_01(2))

# my_list = [2, 4, 6, 8]
# my_lanbda_02 = lambda number: number * 2
# new_list = list(map(my_lanbda_02, my_list))
# print(new_list)

# num = 0.25
# print(id(num))

# text = "Sobhan Esmaeili"
# print(type(text))


# Creating a Class
# class Car():
#     pass  # simply using as a placeholder until we add more code tomorrow


# # Creating an Instance
# # instantiating an object from a class
# class Car():  # parens are optional here
#     pass
# ford = Car() # creates an instance of the Car class and stores into the variable ford
# print(ford)

# Creating Multiple Instances
# instantiating multiple objects from the same class
# class Car():
#     pass
# ford = Car()
# subaru = Car()  # creates another object from the car class
# print(hash(ford))
# print(hash(subaru))  # hash outputs a numerical representation of the location in memory for the variable


# # how to define a class attribute
# class Car():
#     sound = "beep"  # all car objects will have this sound attribute and its' value
#     color = "red"  # all car objects will have this color attribute and its' value
# ford = Car()
# print(ford.color)  # known as 'dot syntax'


# # Changing an Instance Attributes
# # changing the value of an attribute
# class Car():
#     sound = "beep"
#     color = "red"
# ford = Car()
# print(ford.sound)  # will output 'beep'
# ford.sound = "honk"  # from now on the value of fords sound is honk, this does not affect other instances
# print(ford.sound)  # will output 'honk
# benz = Car()
# print(benz.sound)


#  # using the init method to give instances personalized attributes upon creation
# class Car():
#     def __init__(self, color):
#         self.color = color  # sets the attribute color to the value passed in
# ford = Car("blue")  # instantiating a Car class with the color blue
# print(ford.color)


# # Instantiating Multiple Objects with __init__( )
# # defining different values for multiple instances
# class Car():
#     def __init__(self, color, year):
#         self.color = color # sets the attribute color to the value passed in
#         self.year = year
# ford = Car("blue", 2016) # create a car object with the color blue and year 2016
# subaru = Car("red", 2018) # create a car object with the color red and year 2018
# print(ford.color, ford.year)
# print(subaru.color, subaru.year)

# # Global Attributes vs. Instance Attributes
# # using and accessing global class attributes
# class Car():
#     sound = "beep" # global attribute, accessible through the class itself
#     def __init__(self, color):
#         self.color = "blue" # instance specific attribute, not accessible through the class itself
# print(Car.sound)  # print(Car.color) won't work, as color is only available to instances of the Car class, not the class itself
# ford = Car("blue")
# print(ford.sound, ford.color)  # color will work as this is an instance


# # Defining and Calling a Method
# # defining and calling our first class method
# class Dog():
#     def makeSound(self):
#         print("bark")
# sam = Dog()
# sam.makeSound()


# # Accessing Class Attributes in Methods
# # using the self keyword to access attributes within class methods
# class Dog():
#     sound = "bark"
#     def makeSound(self):
#         print(self.sound) # self required to access attributes defined in the class
# sam = Dog()
# sam.makeSound()

# # Method Scope
# # understanding which methods are accessible via the class itself and class instances
# class Dog():
#     sound = "bark"
#     def makeSound(self):
#         print(self.sound)
#     def printInfo():
#         print("I am a dog.")
# Dog.printInfo() # able to run printInfo method because it does not include self parameter
# # Dog.makeSound( ) would produce error, self is in reference to instances only
# sam = Dog()
# sam.makeSound()  # able to access, self can reference the instance of sam
# # sam.printInfo( ) will produce error, instances require the self parameter to access methods


# # Passing Arguments into Methods
# # writing methods that accept parameters
# class Dog():
#     def showAge(self, age):
#         print(age)  # does not need self, age is referencing the parameter not an attribute
# sam = Dog()
# sam.showAge(6)  # passing the integer 6 as an argument to the showAge method


# class person():
#     def __init__(self, first_name, last_name):
#         self.name = first_name
#         self.family = last_name
#         self.age = 35
#     def __str__(self):
#         return "My Name is {} and my Family is {}".format(self.name, self.family)
#
# class employee(person):
#     pass
#
# my_emploee = employee("Sobhan", "Esmaeili")
# print(my_emploee)




