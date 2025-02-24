
# Ans 1 :
name = "Raj Deep Bania"

# Ans 2 :
age = 12
height = 172.2

# Ans 3 :
fav_color = input("please enter your favourite color : ")
print(fav_color)

# Ans 4 :
num = 12
str_num = str(num)
print(type(str_num))

# Output <class 'str'>

# Ans 5 :
float_num = 12.22
int_num = int(float_num)
print(int_num)

#Output 12

# Ans 6 :
var = None
print(type(var))

#Output <class 'NoneType'>

# Ans 7 :
name = "Python"
age = 33
print(f"My name is {name} and i am {age} yours old.")

#Output My name is Python and i am 33 years old.

# Ans : 8
'''
difference between int and float
int is used for whole numbers whereas float is used for numbers with decimal point
int uses less memory whereas float uses more memory.
int is exact number whereas float is less approximate due to precision error. 
'''

#Ans 9:
a = "first"
b = "second"
print(f"initail values a={a} and b ={b}")
(a,b) = (b,a)
print(f"Swapped values a={a} and b={b}" )


''' Output initail values a=first and b =second
    Swapped values a=second and b=first
'''

#Ans : 10
import datetime
x = datetime.datetime.now()
current_year = x.year
birth_year = int(input("Enter your year of birth: "))
print(f"Your age is {current_year - birth_year}")

#Ans 11 :
x = 16
print(id(var))

#Output 10869704

#Ans 12
IMP_VALUE = 1080

# Ans 13 :
is_active = True
has_access = False
print(is_active)
print(has_access)

#Ans 14 :
inta = 12
strb = "14"
print(f"adding inta and strb we get {inta + (int(strb))}")

#Output : adding inta and strb we get 26

#Ans 15 :
name, age, height = "appy", 14, 1.2

print(name)
print(age)
print(height)