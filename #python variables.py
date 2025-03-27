#python variables

'''variable a container for a value
#acts as the value it contains
strings= a series of characters
'''
#string a series of charachters enclosed within double or single quotes 
name="ellen sirleaf"
print(name)
#the variable name behaves as the name itself and while printing we dont use the quotes
#combining string with variables 
print("hello " +name)
#you can also check the data type of a variable 
print(type(name))
#integers(int)
age=20
#can be increased or decreased
age=age+1
age+=1
print(age)
#you can also print the type 
print(type(age))
#float for floating point numbers 
height=5.6
print(height)
print(type(height))
#boolean stores true or false 
#used in if statements and the F is capital and T is also capitalised
human=True
print(human)
print(type(human))
print(f"your name is; {name}")
print(f"your are; {age} years old")
