from veh import *
class Car(Vehicle):
    def __init__(self,name,number,width,depth):
        Vehicle.__init__(self,name,number,width,depth)