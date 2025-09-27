class BaseClass:
    def __init__(self,rain,temperature):
        self.rain=rain
        self.temperature=temperature

class IcanInherit(BaseClass):
    #1 way of calling 
    # def __init__(self, rain, temperature,humidity):
    #     self.rain=rain
    #     self.temperature=temperature
    #     self.humidity=humidity

    #2nd way of calling 
    # def __init__(self, rain, temperature,humidity):
    #     BaseClass.__init__(self,rain,temperature)
    #     self.humidity=humidity

    #3rd way of calling , BEST AND MOST PREFERRED
    def __init__(self, rain, temperature,humidity):
        super().__init__(rain, temperature) #super is as good as calling the parent class ie baseclass 
        self.humidity=humidity




checkInherit = IcanInherit('rainy','25deg','high humidity')
print(checkInherit.humidity,checkInherit.rain,checkInherit.temperature)
        