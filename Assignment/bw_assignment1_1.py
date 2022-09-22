#!/usr/bin/env python
# coding: utf-8

# In[5]:


#1.	Write a program to check whether a person is eligible for voting or not. (Accept age from user)
age=int(input('Enter Age:'))
if(age >= 18):
    print('Eligible for vote')
else:
    print('Not eligible for vote')


# In[4]:


#2.	Write a program to check whether a number entered by user is even or odd
num=int(input('Enter number'))
if(num%2==0):
    print(f'{num} is even number')
else:
    print(f'{num} is even odd')


# In[5]:


#3.	Write a program to check whether a number is divisible by 7 or not
num=int(input('Enter number'))
if(num%7==0):
    print(f'{num} is divisible by 7')
else:
    print(f'{num} is not divisible by 7')


# In[7]:


#4.	Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye"
num=int(input('Enter number'))
if(num%5==0):
    print('Hello')
else:
    print('Bye')


# In[9]:


#5.Write a program to accept percentage from the user and display the grade according to the following criteria:
#Marks                 Grade
# > 90                  A
# > 80 and <= 90        B
# >= 60 and <= 80       C
# below 60              D
percent = int(input('Enter percentage: '))
if(percent > 90):
    print('A')
elif(percent > 80 and percent <= 90):
    print('B')
elif(percent >= 60 and percent <= 80):
    print('C')
elif(percent < 60):
    print('D')


# In[13]:


#6.Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday, 2 for Monday and so on.
num=int(input('Enter number:'))
if(num>=1 and num <=7):
    if(num==1):
        print('Sunday')
    elif(num==2):
        print('Monday')
    elif(num==3):
        print('Tuesday')
    elif(num==4):
        print('Wednesday')
    elif(num==5):
        print('Thursday')
    elif(num==6):
        print('Friday')
    elif(num==7):
        print('Saturday')
else:
    print('Enter number in range 1 to 7')


# In[14]:


#7.Write a program to find the lowest number out of two numbers excepted from user.
num1=int(input('Enter number 1 :'))
num2=int(input('Enter number 2 :'))
if(num1<num2):
    print(f'Lowest number is : {num1}')
else:
    print(f'Lowest number is : {num2}')


# In[16]:


#8.Write a program to check whether a number (accepted from user) is positive or negative
num=int(input('Enter number:'))
if(num<0):
    print(f'{num} is negative')
else:
    print(f'{num} is positive')


# In[18]:


#9.Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

num=int(input('Enter number:'))
if(num%2==0 and num%3==0):
    print(f'{num} is divisible by both 2 and 3')
else:
    print(f'{num} is not divisible by both 2 and 3')


# In[24]:


#10.Write a program to find the largest number out of three numbers excepted from user
x, y, z = input("Enter three values: ").split()
if(x>y):
    if(x>z):
        print(f'Largest value is {x}')
    else:
        print(f'Largest value is {z}')
elif(y>z):
        print(f'Largest value is {y}')
else:
    print(f'Largest value is {z}')


# In[3]:


#11.Accept the age of 4 people and display the oldest one
a, b, c, d = input("Enter age of 4 people: ").split()
temp=int(a)
if(int(b)>temp):
    temp = int(b)
if(int(c)>temp):
    temp = int(c)
if(int(d)>temp):
    temp=int(d)
print(f'Oldest age is {temp}')


# In[2]:


#12.Create simple calculator Add, Sub, Mul, dev takes two numbers from user.
x, y = [int(x) for x in input("Enter two value: ").split()]
add=x+y
sub=x-y
mult=x*y
div=x/y
print(f'{x}+{y}={add}')
print(f'{x}-{y}={sub}')
print(f'{x}*{y}={mult}')
print(f'{x}/{y}={div}')


# %%
