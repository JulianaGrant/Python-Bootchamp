# implicit conversion
num1 = 20
num2 = 30.5
num1 = num1 + num2
print(type(num1))
print(type(num2))

# explicit conversion
num2 = int(num1)
print(type(num2))


age = input(" Tell me your age ")
age = int(age)
new_age = 1 + age
print(new_age)
