#for else loop is important , see how it works 

students = [('Rolf', 25), ('Adam', 30), ('Anne', 28), ('Mary', 22)]

for name,age in students:
    if age <=18:
        print(f"{name} is an adult")
        break
else:  #this else is associated with for loop, not with if statement.
    print("All students are minors")  #this will not be printed as loop is broken