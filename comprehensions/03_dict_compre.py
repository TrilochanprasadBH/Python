#to get keys use .keys()
#to get values use .values()
#to get both of them use .items()

my_dict = {
    "name":'trilo',
    "class":"historical",
    "random": "kuch bhi",
    "hello": "indian"  
}

dict_compre = {hesar:value for hesar, value in my_dict.items() }
print("dict_compre:",dict_compre)