  
# you can also use 'and' operator in if condition
# similarly you can use 'or' operator in if condition
# example of 'or' operator
age = int(input("enter your age:"));
if age < 18 or age > 60:
    print("you are not eligible to work");
else:
    print("you are eligible to work");  

# example of 'and' operator
marks = int(input("enter your marks:"));
if marks >= 0 and marks <= 100:
    print("valid marks");
else:
    print("invalid marks"); 