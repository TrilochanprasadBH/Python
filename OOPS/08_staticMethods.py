class ChaiUtils:

    def cleanData(self,text):
        print(text)
    

obj = ChaiUtils() #there is no constructor , so class cant take args
# obj.cleanData('ok') ---TypeError: ChaiUtils.cleanData() takes 1 positional argument but 2 were given
#python implicitly passed 1st arg as self, and then 2nd as 'ok' , 
# as self is missing in cleandata(self,text), above, this error comes 

#options to fix are 
#1. make it an instance method , as usual , ie add self and call on obj. 
obj.cleanData('ok')

#2. use STATIC METHODS - Make it a static method (no self, no class needed)

class ChaiUtils2:
    @staticmethod
    def clean_data(text):
        print(text)

ChaiUtils2.clean_data('ok trilo this is static method')
# ChaiUtils().cleanData('ok') - this is also accepted way to call static method

#3.  Make it a class method (needs class, not instance)

class ChaiUtils3:
    @classmethod
    def cleanData(cls, text):
        print(text, 'from', cls.__name__)

ChaiUtils3.cleanData('ok, tis is class method')