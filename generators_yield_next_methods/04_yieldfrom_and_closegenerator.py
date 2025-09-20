# here we will learn and build upon 03 file learnings about generators and yield. 
# return vs yield ,we now know the differnce. 

def local_juice():
    yield "Mango Juice" #just like we write return this or that, we have written yield this or that 
    yield "Orange Juice"

def non_local_juice():
    yield "Avocado Juice"
    yield "Raspberry Juice"

def all_in_one_menu():
    yield from local_juice()
    yield from non_local_juice()

for juice in all_in_one_menu():
    print(juice) #this prints all of them 
    #what if we need to print in controlled manner 

inst1 = all_in_one_menu()
print(f"this is inst1:{next(inst1)}")
