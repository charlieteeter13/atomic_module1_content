#!/usr/bin/env python

class Results:

    def __init__(self,
                 name ='',
                 date =None,
                 purpose =None,
                 status = None,
                 ):
        
        self.name = name
        self.date = date
        self.purpose = purpose
        self.status = status


    def __str__():
         return 'Results %s on %s' % (self.name, self.date)

class Experiment(Results):
    def __str__():
        return 'Experiment %s on %s' % (self.name, self.date)

class Simulation(Results):
    def __str__():
        return 'Simulation %s on %s' % (self.name, self.date)


