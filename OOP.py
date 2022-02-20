#!/usr/bin/env python


# building the framework for creating an object: a class
# helps to organizing things alphabetically. easier to find stuff later

#CLASSES INTRO

# create object definition
class Vehicle:
    """
    this is a vehicle
    """

    # attributes -
    #if using the __init__ method, don't list attributes here b/c it's redundant
    #color = None
    #make = None
    #model = None
    #name = None
    #year = None

    # methods
    
    def __init__(self,
                 color=None,
                 make=None,
                 model=None,
                 name='',  #string so no input doesn't cause error
                 year=None
                 ):
        self.color = color
        self.make = make
        self.model = model
        self.name = name
        self.year = year
        

    def __str__(self):
        return self.name
    
    def engine_start(self):
        """
        Start the vehicles engine.

        """
        print(' %s starting engine' % (self))

    def engine_stop(self):
        """
        Stop the vehicles engine.
        """
        print(' %s stopping engine' %(self))

    def honk_horn(self):
        """
        Honk the vehicle's horn.
        """
        print(' %s says HONK!' %(self))



class Car(Vehicle):

    wheels = 100
    

    def __init__(
        self,
        wheels = None,
        *args,
        **kwargs,
     ):
        
        #This is a car. It inherits from Vehicle.
        #Instantiates it by lising first Car attributes, then Vehicle attributes
        
       super().__init__(*args, **kwargs)
       self.wheels = wheels
#override a method
   # def engine_start(self):
      #  print('vroom')

#comment this stuff out for now  
"""  
car = Car()
print(car.wheels)
print(car.color)
car.engine_start()
    



# apply our class (create some objects)

vehicle_1 = Vehicle(
    'silver',
    'Toyota',
    'Sienna',
    'Matt',
    2004,
)


car_1 = Car(
    '100',
    'silver',
    'Toyota',
    'Sienna',
    'Matt',
    2004,
)

car_2 = Car(color='blue')
print(car_2.color)

vehicle_1.engine_start()
print(vehicle_1.year,vehicle_1.color)
vehicle_1.honk_horn()
vehicle_1.engine_stop()

vehicle_2=Vehicle(year=2020)
print(vehicle_2.year)

"""


    

    
    
