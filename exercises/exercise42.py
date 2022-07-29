# Animal is-a object (yes, sort of confusing) look at the extra credit


# Animal is an object
class Animal(object):
    pass


# Dog is an Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has a name
        self.name = name


# Cat is an Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has a name
        self.name = name


class Person(object):
    ## Person is an object
    def __init__(self, name):
        ## person has a name
        self.name = name
        ## person has-a pet of some kind
        self.pet = None


## Employee is a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## Person has a name
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary


## Fish is an object
class Fish(object):
    pass


## Salmon is a Fish
class Salmon(Fish):
    pass


## Halibut is a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")


## mary is a Person
mary = Person("Mary")

## mary has a pet(satan)
mary.pet = satan

## frank is a Employee and has a  name frank and salary
frank = Employee("Frank", 120000)

## frank has-a pet (frank's pet is-a rover)
frank.pet = rover

## flipper is-a Salmon
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()
