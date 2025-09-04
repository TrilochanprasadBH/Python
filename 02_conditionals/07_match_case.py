seat_type = str(input("Enter the seat type (sleeper/ac/general/luxury): ")).lower()

# "match-case" statement to determine the price based on seat type 
# we avoid lengthy if-elif-else statements using match-case

match seat_type:
    case "sleeper":
        price = 500
        print("Sleeper class selected,price is 500.")
    case "ac":
        price = 1000
        print("AC class selected,price is 1000.")
    case "general":
        price = 300
        print("General class selected,price is 300.")
    case "luxury":  
        price = 2000
        print("Luxury class selected,price is 2000.")
    case _:  # default case if none of the above match
        price = 0
        print("Invalid seat type entered.") 