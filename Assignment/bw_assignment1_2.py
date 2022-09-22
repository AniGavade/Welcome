#!/usr/bin/env python
# coding: utf-8

# In[2]:


#13.Write a Python program to count the number of even and odd numbers from a series of numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
odd_cnt =0
even_cnt=0
for i in numbers:
    if(i%2==0):
        even_cnt +=1
    else:
        odd_cnt +=1
print(f'Even count is {even_cnt} and odd count is {odd_cnt}')


# In[3]:


#14.Write a Python program that prints all the numbers from 0 to 6 except 3 and 6
for i in range(7):
    if(i==3 or i==6):
        continue
    else:
        print(i)


# In[6]:


#15.Write a program in Python to display the Factorial of a number.
num=int(input('Enter number'))
x=num;
fact=1
while(num>1):
    fact=fact*num
    num -= 1
print(f'Factorial of {x} is {fact}')


# In[1]:


#16.Write a program in Python to reverse a word.
word=input('Enter word for reverse:')
for i in range(len(word),0,-1):
    print(word[i-1],end='')


# In[11]:


#17.Write a Python program to reverse a number.
num=int(input('Enter number:'))
while num>0:
    num_part = num%10
    num=num//10
    print(num_part,end='')


# In[2]:


#18.Write a program to print n natural number in descending order using a while loop
num=int(input('Enter number:'))
while(num>0):
    print(num)
    num=num-1


# In[15]:


#19.Write a python program to print the square of all numbers from 0 to10
for i in range(0,11):
    sqrt_num=i*i
    print(f'{i}^2={sqrt_num}')


# In[17]:


#20. Write a python program to find the sum of all even numbers from 0to10
for i in range(11):
    total=0
    if(i%2==0):
        total = total+ i
print(f'sum of even numbers = {total}')

