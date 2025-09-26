class BaseChai:
    def __init__(self,type_):
        self.type = type_
        #type has underscore , just to differentiate it from type keyword of python. 
    def prepare(self):
        print(f"i am preparing {self.type} kind of chai")

class SpecialChai(BaseChai): #this is how INHERITANCE is shown. syntax 
    def add_spices(self):
        print('adding spices like cardmom to chai')
    
class ChaiShop:
    chai_class = BaseChai #this is COMPOSITION
    def __init__(self):
        self.chai = self.chai_class('Regularchai') #see how we are making use of BaseChai here to access the type 
    #method of BaseChai, prepare(), will now be available on self.chai
    #here self.chai is as good as instance of base chai , so call type on this not
    #here i am directly reading the type from base chai, not calling the method below insdie brewing 
    def brewing(self):
        print(f'i am brewing {self.chai.type} ,through composition on ChaiShop, composition of BaseChai')


class FancyChaiShop(ChaiShop): #inheritance
    chai_clas_fancy = SpecialChai #this is composition 


shop = ChaiShop()
fancy = FancyChaiShop()

fancy.brewing()
shop.brewing()
# fancy.chai_clas_fancy.add_spices()  
# fancy.chai_clas_fancy.prepare()  
# this gives error, SpecialChai.add_spices() missing 1 required positional argument: 'self'
# as chai_clas_fancy - has no contructor of own , there is no self reference i can give. hence to solve this lets use 

fancy.chai.prepare() #here instead i made use of chai, to connect to prepare as in,
#chaishop , i composition of basechai and in constructor assing self.chai = self.chai_class('Regularchai')
#so this will have reference to self , hence it can print 