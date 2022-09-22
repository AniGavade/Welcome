#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.Write a Python function to find the Max of three numbers
def MaxNum(n1,n2,n3):
    maxn=n1
    if n2>maxn :
        maxn = n2
    else:
        maxn = n3
    return maxn

x=MaxNum(210,410,30)
print(x)             


# In[5]:


#2.	Write a Python function to sum all the numbers in a list. 
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20
def sumList(lst):
    lsum=0
    for ele in lst:
        lsum += ele
    return lsum
List1=[8, 2, 3, 0, 7]
print(sumList(List1))        


# In[6]:


#3.Write a Python function to multiply all the numbers in a list.  
#Sample List : (8, 2, 3, -1, 7)
#Expected Output : -336
def multList(lst):
    mult=1
    for ele in lst:
        mult = mult*ele
    return mult
List1=[8, 2, 3, -1, 7]
print(multList(List1)) 


# In[11]:


#4.Write a Python program to reverse a string.  
# Sample String : "1234abcd"
# Expected Output : "dcba4321"
#Approach-1:Using for loop
def revStr(strn):
    for i in range(len(strn)-1,-1,-1):
        print(strn[i],end='')
revStr("1234abcd")
        
print("\n--------------------------------------------------------------")

#Approach-2:Using slicing
def revStr(strn):
    print(strn[::-1])
revStr("1234abcd")


# In[12]:


#5.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the 
#number as an argument.
def calc_factorial(n):
    fact=1
    if n < 0:
        print("Enter non-negative number")
    elif n==0 or n==1:
        return fact
    else :
        fact = n * calc_factorial(n-1)
        
    return fact

print(calc_factorial(6))


# In[13]:


#6.Write a Python function to check whether a number falls in a given range
def checkRange(start,end,num):
    flag=False
    if num>=start and num<=end:
        flag=True
    return flag

x=checkRange(20,40,33)
if(x):
    print("Given number falls in given range")
else:
    print("Given number doesn't fall in given range")


# In[18]:


#7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
def calc_case_num(strn):
    lcount=0
    ucount=0
    for i in strn:
        if i.isupper():
            ucount += 1
        elif i.islower():
            lcount += 1
    print('No. of Upper case characters :',ucount)
    print('No. of Lower case characters :',lcount)
    
calc_case_num('The quick Brow Fox')


# In[20]:


#8.Write a Python function that takes a list and returns a new list with unique elements of the first list. 
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def unique_ele_list(lst):
    output_lst=[]
    for ele in lst:
        if ele not in output_lst:
            output_lst.append(ele)
    return output_lst
List1=[1,2,3,3,3,3,4,5]
print(unique_ele_list(List1))


# In[21]:


#9.Write a Python function that takes a number as a parameter and check the number is prime or not
def check_prime(num):
    flag = False
    if num > 1:
        for i in range(2,num):
            if(num%i)==0:
                flag=True
                break
    if flag:
        print(num," is not prime number")
    else:
        print(num," is prime number")

n=int(input("Enter number to check prime : "))
check_prime(n)


# In[22]:


#10.Write a Python function that checks whether a passed string is palindrome or not
def check_palindrome(str):
    if str == str[::-1]:
        print(str," is palindrome")
    else:
        print(str," is not palindrome")

check_palindrome('OYO')


# In[23]:


#11.Write a Python function to check whether a string is a pangram or not 
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
def check_pangram(arg):
    if len(set('abcdefghijklmnopqrstuvwxyz') - set(arg.lower())) == 0 :
        return True
    return False

user_str = input("Enter a string to check for pangram : ")

if(check_pangram(user_str)):
    print("It is a pangram string")
else:
    print("Not a pangram string")


# In[24]:


#12.Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.  
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow
def sort_str(arg):
    output="-".join(sorted(arg.split('-')))
    return output

print(sort_str('green-red-yellow-black-white'))


# In[26]:


#13.Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
def print_square(start,end):
    sqr_lst=[]
    while(start<=end):
        sqr_lst.append(start**2)
        start=start+1
    return sqr_lst

print(print_square(1,30))


# In[27]:


#14.Write a Python program to access a function inside a function
def outer_func():
    def inner_func():
        print("Hello, World!")
    inner_func()
outer_func()


# In[30]:


#15.Write a Python program to detect the number of local variables declared in a function
def fun():
    a = 1
    str = 'Python Program'
  
  
# Driver program
print(fun.__code__.co_nlocals)

