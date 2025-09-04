choice = input("enter your choice of drink (tea/coffee):").lower(); 

if choice == "tea" or choice == "coffee":
    print(f"you have selected {choice}");
else:
    print("invalid choice");