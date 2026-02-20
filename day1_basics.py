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
