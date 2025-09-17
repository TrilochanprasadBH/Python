#see how method over riding works in oops. 

class Learning:
    def __init__(self,subject,timeperiod,level):
        self.subject= subject
        self.timeperiod=timeperiod
        self.level=level
    
    def learning_method(self):
        print('this is shravana')

class Trilo(Learning):
    def __init__(self, subject, timeperiod, level,mentor):
        super().__init__(subject, timeperiod, level,)
        self.mentor=mentor 
    
    def learning_method(self):
        print(f"learning is {self.mentor}")

l1 = Trilo('philo','1 month',5,'sarrthi')
l1.learning_method()