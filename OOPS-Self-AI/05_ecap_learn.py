#learning encapsulation through an example. basics. 

class Banking:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.__balance = balance #this is private attribute, observe __balance 
        self._pin=1234
    
    def show_balance(self):
        return self.__balance
    
    def __validate_pin(self,entered_pin):
        return self._pin == entered_pin
        
    def withdraw(self,amount,pin):
        if self.__validate_pin(pin):
            if amount <= self.__balance:
                self.__balance-=amount
                print(f"balance:{self.__balance}")
            else:
                print('amount exceeds balance')
        else:
            print('enter correct pin')

b1 = Banking(12345,250)
print(b1.show_balance())
b1.withdraw(100,1234)
b1.withdraw(100,1234)
print(b1.__validate_pin(1234)) #this throws error - has no attribute __validate_pin as the method is mangled and as its private method we cant access it directly

#print(b1._Banking__validate_pin(1234)) #this works, but never do this as you are name-mangling to access a private method 
