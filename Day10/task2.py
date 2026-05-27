x=input("Enter First: ") #KANAN
y=input("Enter Second: ") #3

print("\nAddition:")
print(x+y, "~ This is called Concatenation\n") #KANAN3
# print(int(x) + int(y)) Because x is a string, we cannot convert it to an integer. This will raise a ValueError.

print("Subtraction: Not possible\n")
#print(x-y) Not possible because x and y are strings. This will raise a TypeError.
# print(int(x) - int(y)) Because x is a string, we cannot convert it to an integer. This will raise a ValueError.

print("Multiplication:")
print(x * int(y), "~ This is called Repetition\n")
# print(x*y) Not possible because x and y are strings. This will raise a TypeError.
# print(int(x) * int(y)) Because x is a string, we cannot convert it to an integer. This will raise a ValueError.

print("Division: Not possible\n")
#print(x/y) Not possible because x and y are strings. This will raise a TypeError.
# print(int(x) / int(y)) Because x is a string, we cannot convert it to an integer. This will raise a ValueError.

print("Floor Division: Not possible\n")
# print(x//y) Not possible because x and y are strings. This will raise a TypeError.
# print(int(x) // int(y)) Because x is a string, we cannot convert it to an integer. This will raise a ValueError.

print("Modulus: Not possible\n")
# print(x%y) Not possible because x and y are strings. This will raise a TypeError.
# print(int(x) % int(y)) Because x is a string, we cannot convert it to an integer. This will raise a ValueError.

print("Exponentiation: Not possible\n")
# print(x**y) Not possible because x and y are strings. This will raise a TypeError.
# print(int(x) ** int(y)) Because x is a string, we cannot convert it to an integer. This will raise a ValueError.