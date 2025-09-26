class History:
    battle = 'talikota'

    def war(self):
       return f"{self.battle} is name of battle"

h1 = History()
#print(h1.war) #<bound method History.war of <__main__.History object at 0x10223a900>> , here i need to call func ()
print(h1.war())
# print(History.war) <function History.war at 0x10106f6a0>.  here also need to call function , ()

# print(History.war()) - throws error - TypeError: History.war() missing 1 required positional argument: 'self'
#class will not have reference to give arg ,so 

print(History.war(h1)) #after passing ref h1, it prints now 
