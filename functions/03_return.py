def learn_return(cups, price_per_cup):
    total_cost = cups * price_per_cup
    return total_cost

output = learn_return(3,5)
print(f"Total cost : {output}")