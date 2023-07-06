Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=5
b=5.5
sum = a+b
print(sum)
10.5
print(type(sum))
<class 'float'>

 #type() is used to display the datatype of a variable
# this is implicit type conversion
#explicit is demonstrated below
num_int=123
num_str="456" #which is a string
#to convert
print(type(num_int))
<class 'int'>
num_int = str(num_int)
print(type(num_int))
<class 'str'>
