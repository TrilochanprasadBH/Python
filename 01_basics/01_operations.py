x = 10;
y = 20;

# Addition
sum_result = x + y;
print("Sum:", sum_result);

# Subtraction
diff_result = y - x;
print("Difference:", diff_result);  

# Multiplication
prod_result = x * y;
print("Product:", prod_result);         

# Division
div_result = y / x;
print("Division:", div_result); 
# Floor Division
floor_div_result = y // x;
print("Floor Division:", floor_div_result); 

# Modulus
mod_result = y % x;
print("Modulus:", mod_result);      

# Exponentiation        
exp_result = x ** 2;
print("Exponentiation:", exp_result);   

# Comparison Operators
print("Is x equal to y?", x == y);
print("Is x not equal to y?", x != y);
print("Is x greater than y?", x > y);
print("Is x less than y?", x < y);
print("Is x greater than or equal to y?", x >= y);
print("Is x less than or equal to y?", x <= y);

# Logical Operators
a = True;
b = False;
print("a AND b:", a and b);
print("a OR b:", a or b);
print("NOT a:", not a); 

# Bitwise Operators
bit_and = x & y;
print("Bitwise AND:", bit_and);
bit_or = x | y;
print("Bitwise OR:", bit_or);
bit_xor = x ^ y;
print("Bitwise XOR:", bit_xor);
bit_not = ~x;
print("Bitwise NOT:", bit_not);
left_shift = x << 2;
print("Left Shift:", left_shift);
right_shift = y >> 2;
print("Right Shift:", right_shift); 

# Membership Operators
list_example = [10, 20, 30, 40, 50];
print("Is 20 in list?", 20 in list_example);
print("Is 60 not in list?", 60 not in list_example);
# Identity Operators
a = 1000;
b = 1000;
print("Is a identical to b?", a is b);
print("Is a not identical to b?", a is not b);
# Note: 'is' checks for identity, not equality. For small integers, Python caches values, so 'is' may return True.

# Assignment Operators
c = 5;
print("Initial c:", c);
c += 3;  # c = c + 3
print("After c += 3:", c);
c -= 2;  # c = c - 2
print("After c -= 2:", c);          

c *= 4;  # c = c * 4
print("After c *= 4:", c);
c /= 2;  # c = c / 2
print("After c /= 2:", c);
c %= 3;  # c = c % 3
print("After c %= 3:", c);
c **= 2; # c = c ** 2
print("After c **= 2:", c);
c //= 3; # c = c // 3
print("After c //= 3:", c);
# Note: Python does not have a separate operator for string concatenation; the '+' operator is used for that purpose.
str1 = "Hello, ";
str2 = "World!";
str1 += str2;  # str1 = str1 + str2
print("String after concatenation:", str1);

# Python does not have a specific operator for string repetition; the '*' operator is used for that purpose.
str3 = "Ha";
str3 *= 3;  # str3 = str3 * 3
print("String after repetition:", str3);

# Python does not have a specific operator for list concatenation; the '+' operator is used for that purpose.
list1 = [1, 2, 3];
list2 = [4, 5, 6];
list1 += list2;  # list1 = list1 + list2
print("List after concatenation:", list1);
list3 = [7, 8];

#this is quite unusual but valid
list3 *= 2;  # list3 = list3 * 2
print("List after repetition:", list3);  # Output: [7, 8, 7, 8]