class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale,Exhale.")
    
class Fish(Animal): #inheriting 

    def __init__(self):
        super().__init__() #trigger super class.

    def breathe(self):
        super().breathe() #inherite breathe method from super class and add extra code.
        print("doing this under water.")

    def swim(self):
        print("moving in water.")
    

nemo = Fish() #create object of fish class.
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)


#now fish class inherit all the attribute and method from animal class.
#inheritance => take existing class and build on top of it.