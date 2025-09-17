#learn basics of inheritance 

class Vehicle:
    def __init__(self,company,model,year):
        self.company=company
        self.model=model
        self.year=year
        self.is_running = False
    
    def start_engine(self):
        self.is_running = True
        print(f"{self.company} vehicle , {self.model} model , {self.year} year release is running/started")
    
    def stop_engine(self): 
        self.is_running = False
        print(f"{self.company} vehicle , {self.model} model , {self.year} year release has stopped")

#child class, this will inherit parent class vehicle 

class Car(Vehicle):
    def __init__(self, company, model, year,number_of_doors):
        #calling parent constructor
        super().__init__(company, model, year)
        self.number_of_doors = number_of_doors
    
    def display_details(self):
        print(f" number of doors is :{self.number_of_doors}")

    def honk(self):
        print('car honking')

car = Car('bmw','r12','2020',4)
car.start_engine() #inherited method  from vehicle used on car
car.honk() 
car.display_details()
