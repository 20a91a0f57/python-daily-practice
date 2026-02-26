"""DAY-1 — Python Introduction + Setup + Basics"""
"""In Command prompt"""
C:\Users\sree>python --version
Python 3.14.3
C:\Users\sree>python
Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> print("Hello!")
Hello!  
>>> """variable"""
'variable'
>>> name = "Madhuri"
>>> age = 22
>>> percentage = 85.5
>>> print(name, age, percentage)
Madhuri 22 85.5
>>> name = "Madhuri"
>>> age = 22
>>> percentage = 95.5
>>> status = "Pass"
>>> print(name,age,percentage,status)
Madhuri 22 95.5 Pass
>>> print("My name is:",name,"and My age is:",age,"My percentage is:",percentage,"status(Pass/Fail):",status)
My name is: Madhuri and My age is: 22 My percentage is: 95.5 status(Pass/Fail): Pass
>>> print(f"My name is: {name}. My age is: {age}. My percentage is: {percentage}. Status(Pass/Fail): {status}.")
My name is: Madhuri. My age is: 22. My percentage is: 95.5. Status(Pass/Fail): Pass.
>>> print("My name is: {}. My age is: {}. My percentage is: {}. Status(Pass/Fail): {}.".format("Madhuri","22","95.5","pass"))
My name is: Madhuri. My age is: 22. My percentage is: 95.5. Status(Pass/Fail): pass.
>>> print("My name is: {}. My age is: {}. My percentage is: {}. Status(Pass/Fail): {}.".format("Madhuri",22,95.5,"pass"))
My name is: Madhuri. My age is: 22. My percentage is: 95.5. Status(Pass/Fail): pass.
>>> print(type(status))
<class 'str'>
>>> print(type(name))
<class 'str'>
>>> print(type(age))
<class 'int'>
>>> print(type(percentage))
>>> "Take 2 float numbers  multiply"
'Take 2 float numbers  multiply'
>>> a = float(input("Enter Number1:"))
Enter Number1:58.6
>>> b = float(input("Enter Number2:"))
Enter Number2:95.3
>>> print(a * b)
5584.58
<class 'float'>
>>> """Adding Two Numbers using int() function"""
'Adding Two Numbers using int() function'
// Both are int(). so, no error
>>> a, b = map(int, input("Enter Numbers:").split())
Enter Numbers:5 9   
>>> print(a + b)
14

//In int() but we gave float(). so, error
>>> a, b = map(int, input("Enter Numbers:").split())
Enter Numbers:5.6 9.5     
Traceback (most recent call last):
  File "<python-input-28>", line 1, in <module>
    a, b = map(int, input("Enter Numbers:").split())
    ^^^^
ValueError: invalid literal for int() with base 10: '5.6'

//In int() we use one is int() and one is float(). so, error
>>> a, b = map(int, input("Enter Numbers:").split())
Enter Numbers:5 5.9   
Traceback (most recent call last):
  File "<python-input-33>", line 1, in <module>
    a, b = map(int, input("Enter Numbers:").split())
    ^^^^
ValueError: invalid literal for int() with base 10: '5.9'

"""Adding Two Numbers using float() function"""
'Adding Two Numbers using float() function'
//Both are float(). so, no error  
>>> a, b = map(float,  input("Enter Numbers:").split())
Enter Numbers:5.6 9.5
>>> print(a + b)
15.1
//In float() we can use both int() numbers but no error 
>>> a, b = map(float,  input("Enter Numbers:").split())
Enter Numbers:2 9
>>> print(a + b)
11.0
//In float() we can use one int() and one is float() but no error 
>>> a, b = map(float,  input("Enter Numbers:").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ())
Enter Numbers:8 5.6
>>> print(a + b)
13.6

>>> a = int(input("Enter Number1:"))
Enter Number1:8
>>> b = float(input("Enter Number2:"))
Enter Number2:5.6
>>> print(a + b)
13.6
>>> a = int(input("Enter Number1:"))
Enter Number1:5.6
Traceback (most recent call last):
  File "<python-input-32>", line 1, in <module>
    a = int(input("Enter Number1:"))
ValueError: invalid literal for int() with base 10: '5.6'
>>>int() can takee only integer numbers not any of the data types.
>>>float() can take both the integer and float numbers.

>>> """printing of square numbers"""
'printing of square numbers'
>>> a = int(input("Enter Number:")
... )
Enter Number:5
>>> print(a**2)
25
>>> a = float(input("Enter Number:"))
Enter Number:5.0
>>> print(a**2)
25.0
>>> a = int(input("Enter Number:"))
Enter Number:5
>>> print(a**2)
25
>>> a = float(input("Enter Number:"))
Enter Number:6
>>> print(a**2)
36.0
>>> a = int(input("Enter Number:"))
Enter Number:6.0
Traceback (most recent call last):
  File "<python-input-45>", line 1, in <module>
    a = int(input("Enter Number:"))
ValueError: invalid literal for int() with base 10: '6.0'
>>>

>>> a = int(input())
5
>>> b = float(input())
5.6
>>> a, b = b, a
>>> print(a, b)
5.6 5
>>> a = input()
5
>>> b = input()
6
>>> a, b = b, a
>>> print(a, b)
6 5
>>> print(int(a), int(b))
6 5
>>> print(float(a), float(b))
6.0 5.0
>>> print(float(a), int(b))
6.0 5
>>> print(int(a), float(b))
6 5.0
>>> a = input()
5.6
>>> b = input()
5
>>> a, b = b, a
>>> print(a, b)
5 5.6
>>> print(float(a), int(b))
Traceback (most recent call last):
  File "<python-input-71>", line 1, in <module>
    print(float(a), int(b))
                    ~~~^^^
ValueError: invalid literal for int() with base 10: '5.6'
>>> print(int(a), float(b))
5 5.6
>>> print(float(a), float(b))
5.0 5.6
>>> a = input()
5.6
>>> b = input()
5
>>> print(float(a), int(b))
5.6 5
>>> print(int(a), float(b))
Traceback (most recent call last):
  File "<python-input-61>", line 1, in <module>
    print(int(a), float(b))
          ~~~^^^
ValueError: invalid literal for int() with base 10: '5.6'
>>> print(a, b)
5.6 5
>>> print(float(a), float(b))
5.6 5.0
>>> print(int(a), int(b))
Traceback (most recent call last):
  File "<python-input-64>", line 1, in <module>
    print(int(a), int(b))
          ~~~^^^  
ValueError: invalid literal for int() with base 10: '5.6'




   




















