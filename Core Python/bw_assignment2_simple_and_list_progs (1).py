#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.Python program to add two numbers
a=int(input("Enter number1"))
b=int(input("Enter number2"))
c= a+b
print(a,'+',b,'=',c)


# In[3]:


#2.Maximum of two numbers in Python
a=int(input("Enter number1"))
b=int(input("Enter number2"))
if(a > b):
    print("Greater among ",a,' and ',b,' is ',a)
else:
    print("Greater among ",a,' and ',b,' is ',b)


# In[5]:


#3.Python Program for factorial of a number
a=int(input("Enter number"))
factorial =1
temp=a
while(a>0):
    factorial = factorial*a
    a -= 1
print(temp,'!=',factorial)


# In[6]:


#4.Python Program for simple interest
p=float(input("Enter principle : "))
t=int(input("Enter time : "))
r=float(input("Enter rate : "))
si=(p*t*r)/100
print("Simple Interest = ",si)


# In[7]:


#5.Python Program for compound interest
def compound_interest(p,t,r):
    print("Principle : ",p)
    print("Time : ",t)
    print("Rate : ",r)
    a=p*((1+r/100)**t)
    ci=a-p
    return ci

print("The compound interest is ",compound_interest(1200,2,5.4))


# In[10]:


#6.Python Program to check Armstrong Number
num=int(input('Enter number'))
x=num
sumd =0
while num > 0 :
    digit = num %10
    sumd += digit**3
    num=num //10
if(x==sumd):
    print(f'The number {x} is armstrong number')
else:
    print(f'The number {x} is not armstrong number')


# In[11]:


#7.Python Program for Program to find area of a circle
radius=int(input('Enter radius of circle : '))
PI=3.142
area=PI*radius*radius
print("Area of circle is ",area)


# In[12]:


#8.Python program to print all Prime numbers in an Interval
def prime_numbers(start,end):
    prime_list = []
    for i in range(start,end+1,1):
        if i==0 or i==1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

s=int(input("Enter Start: "))
e=int(input("Enter End: "))
pnum_list=prime_numbers(s,e)
print(pnum_list) 


# In[2]:


#9.Python program to check whether a number is Prime or not
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


# In[28]:


#10.Python Program for n-th Fibonacci number
def fibonacci(n):
    a=0
    b=1
    sums=0
    i=2
    while(i<n):
        sums=a+b
        a=b
        b=sums
        i += 1
    return b
    
print(fibonacci(9))


# In[38]:


#11.Python Program for How to check if a given number is Fibonacci number?
import math
def is_perfect_square(num):
    if(num>0):
        sr = int(math.sqrt(num))
        return ((sr*sr) == num)
    return False

def check_fibonacci(n):
    cond1=5*n**2+4
    cond2=5*n**2-4
    if(is_perfect_square(cond1)):
        print(n," is fibonacci number")
    elif(is_perfect_square(cond2)):
        print(n," is fibonacci number")
    else:
        print(n," is not fibonacci number")
        
n=int(input("Enter number to check if it is Fibonacci number : "))
check_fibonacci(n)


# In[30]:


#12.Python Program for n\’th multiple of a number in Fibonacci Series
def find_position(k, n):
    a = 0
    b = 1
    i =2;
    while i!=0:
        sums = a + b;
        a = b;
        b = sums;
 
        if b%k == 0:
            return n*i
 
        i+=1
         
    return
print(find_position(4,5))


# In[31]:


#13.Program to print ASCII Value of a character
ch=input("Enter character: ")
print("ASCII value of character ",ch ," is ",ord(ch))


# In[32]:


#14.Python Program for Sum of squares of first n natural numbers
def sum_square(n):
    sum_sq =0
    for i in range(1,n+1):
        sum_sq = sum_sq+i**2        
    return sum_sq
print(sum_square(5))


# In[34]:


#15.Python Program for cube sum of first n natural numbers
def sum_cubes(n):
    sum_cubs=0
    for i in range(1,n+1):
        sum_cubs = sum_cubs+i**3        
    return sum_cubs
print(sum_cubes(5))


# In[35]:


#16.Python program to interchange first and last elements in a list
def change_first_last(Lst):
    new_lst=[]
    new_lst.append(Lst[-1])
    for i in range(1,len(Lst)-1):
        new_lst.append(Lst[i])
    new_lst.append(Lst[0])
    print(new_lst)

Lst=[20,10,30,50,22,7]
change_first_last(Lst)


# In[36]:


#17.Python program to swap two elements in a list
def swap(Lst,pos1,pos2):
    temp=Lst[pos1]
    Lst[pos1]=Lst[pos2]
    Lst[pos2]=temp
    return Lst
 
List=[20,10,30,50,22,7]
print(swap(List,1,4))


# In[ ]:


#18.Python | Ways to find length of list
def find_length(Lst):
    count=0
    for c in Lst:
        count += 1
    return count
 
List=[20,10,30,50,22,7]
print(find_length(List))


# In[37]:


#19.Python | Ways to check if element exists in list
def check_in_list(Lst,c):
    if c in Lst:
        return True
    else:
        return False
 
 
List=[20,10,30,50,22,7]
ch=int(input("Enter element:"))
x=check_in_list(List,ch)
if(x==True):
    print(ch," exists in List")
else:
    print(ch," does not exists in List")
    
Or

def check_in_list(Lst,c):
    for i in range(0,len(Lst)):
        if Lst[i]==c:
            return True
    else:
        return False
Listn=[20,10,30,50,22,7]
ch=int(input("Enter element:"))
x=check_in_list(Listn,ch)
if(x==True):
    print(ch," exists in List")
else:
    print(ch," does not exists in List")


# In[41]:


#20.Different ways to clear a list in Python
#Method #1 : Using clear() method
Lst=[6,0,1,2]
print("List before clear:",Lst)
Lst.clear()
print("List after clear:",Lst)

list1 = [1, 2, 3]
print("List before clear:",list1)
# deleting list using reinitialization
list1 = []
print("List after clear:",list1)


# In[42]:


#21.Python | Reversing a List
def reverse_list(Lst):
    reversed_list=[]
    for i in range (len(Lst)-1,-1,-1):
        reversed_list.append(Lst[i])
    return reversed_list

Listn=[20,10,30,50,22,7]
print(reverse_list(Listn))

OR 

def Reverse(lst):
    lst.reverse()
    return lst
     
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))


# In[ ]:


#22.Python program to find sum of elements in list
def sum_lst(lst):
    return sum(lst)
     
lst = [10, 11, 12, 13, 14, 15]
print(sum_lst(lst))


# In[43]:


#23.Python | Multiply all numbers in the list
def mult_lst(lst):
    mult=1
    for i in lst:
        mult=mult*i
    return mult
     
lst = [1,2,3,4]
print(mult_lst(lst))


# In[44]:


#24.Python program to find smallest number in a list
def smallest_num(lst):
    numMin=lst[0]
    for i in lst:
        if i<numMin:
            numMin=i
    return numMin
     
lst = [1,2,3,4]
print(smallest_num(lst))


# In[4]:


#25.Python program to find largest number in a list
def largest_num(lst):
    numLarge=lst[0]
    for i in lst:
        if i>numLarge:
            numLarge=i
    return numLarge
     
lst = [1,2,3,4,4]
print(largest_num(lst))


# In[3]:


#26.Python program to find second largest number in a list
def second_largest(Lst):
    Lst.sort(reverse=True)
    return Lst[1]
    
lst = [10, 22, 12, 35, 14, 15,35]
print(second_largest(lst))


# In[47]:


#27.Python program to find N largest elements from a list
def nth_largest(Lst,n):
    Lst.sort(reverse=True)
    return Lst[n-1]
    
lst = [10, 22, 12, 35, 14, 15]
print(nth_largest(lst,4))   


# In[3]:


#28.Python program to print even numbers in a list
def print_even(Lst):
    even_lst=[]
    for i in Lst:
        if i %2 ==0:
            even_lst.append(i)
    return even_lst
    
lst = [10, 22, 12, 35, 14, 15]
print(print_even(lst)) 

#or

even_list=list(filter(lambda x:(x%2 ==0),lst))
print("using lambda function",even_list)


# In[2]:


#29.Python program to print odd numbers in a List
def print_odd(Lst):
    odd_lst=[]
    for i in Lst:
        if i %2 !=0:
            odd_lst.append(i)
    return odd_lst
    
lst = [10, 22, 12, 35, 14, 15]
print(print_odd(lst))   

#OR

new_list=list(filter(lambda x:(x%2 !=0),lst))
print("Using Lambda function",new_list)


# In[50]:


#30.Python program to print all even numbers in a range
def even_range(start,end):
    even_lst=[]
    while(start<=end):
        if start %2 == 0:
            even_lst.append(start)
        start += 1
    return even_lst
    
print(even_range(10,20))  


# In[51]:


#31.Python program to print all odd numbers in a range
def odd_range(start,end):
    odd_lst=[]
    while(start<=end):
        if start %2 != 0:
            odd_lst.append(start)
        start += 1
    return odd_lst
    
print(odd_range(10,20))


# In[1]:


#32.Python program to print positive numbers in a list
def print_positive(Lst):
    positive_lst=[]
    for i in Lst:
        if i>0:
            positive_lst.append(i)
    return positive_lst

lst = [10, -22, 12, 0, -14, 15]
print(print_positive(lst))      


# In[54]:


#33.Python program to print negative numbers in a list
def print_negative(Lst):
    negative_lst=[]
    for i in Lst:
        if i<0:
            negative_lst.append(i)
    return negative_lst

lst = [10, -22, 12, -35, -14, 15]
print(print_negative(lst))  


# In[56]:


#34.Python program to print all positive numbers in a range
def positive_range(start,end):
    positive_lst=[]
    while(start<=end):
        if start >= 0:
            positive_lst.append(start)
        start += 1
    return positive_lst
    
print(positive_range(-10,20))  
    


# In[58]:


#35.Python program to print all negative numbers in a range
def negative_range(start,end):
    negative_lst=[]
    while(start<=end):
        if start < 0:
            negative_lst.append(start)
        start += 1
    return negative_lst
    
print(negative_range(-10,10))  


# In[59]:


#36.Remove multiple elements from a list in Python
list1 = [11, 5, 17, 18, 23, 50]
unwanted_num = {11, 5}
list1 = [ele for ele in list1 if ele not in unwanted_num]
print("New list after removing unwanted numbers: ", list1)


# In[62]:


#37.Python – Remove empty List from List
test_list = [5, 6, [], 3, [], [], 9]
print("The original list is : " + str(test_list))
res = list(filter(None, test_list))
print ("List after empty list removal : " + str(res))


# In[63]:


#38.Python | Cloning or Copying a list
#1. Using slicing
def Cloning(li1):
    li_copy = li1[:]
    return li_copy

li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)

#2. Using the extend()
def Cloning(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)

#3. Using the list()
def Cloning(li1):
    li_copy = list(li1)
    return li_copy
   
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)

#4. Using the append() 
def Cloning(li1):
    li_copy =[]
    for item in li1: li_copy.append(item)
    return li_copy
   
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)

#5.  Using the copy()
def Cloning(li1):
    li_copy =[]
    li_copy = li1.copy()
    return li_copy
   
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)


# In[60]:


#39.Python | Count occurrences of an element in a list
def count_occurence(lst,num):
    cnt=0
    for i in lst:
        if i==num:
            cnt += 1
    return cnt
list1 = [11, 5, 17, 11, 23, 50]
print(count_occurence(list1,11))


# In[2]:


#40.Python | Remove empty tuples from a list
def Remove(tuples):
    tuples_list = list(filter(None, tuples))
    return tuples_list
  
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))


# In[61]:


#41.Python | Program to print duplicates from a list of integers
def duplicate_entries(lst):
    visited_lst=[]
    dup_list=[]
    for i in lst:
        if i not in visited_lst:
            visited_lst.append(i)
        else:
            dup_list.append(i)
    return dup_list
list1 = [11, 5, 17, 11, 23, 5]
print(duplicate_entries(list1))


# In[68]:


#42.Python program to find Cumulative sum of a list
def cumulative_sum(lst):
    new_lst=[]
    csum=0
    for i in lst:
        csum = csum + i
        new_lst.append(csum)
    return new_lst

list1 = [10, 20, 30, 40, 50]
print(cumulative_sum(list1))


# In[69]:


#43.Python | Sum of number digits in List
def digit_sum(lst):
    sum_lst=[]
    for i in lst:
        dsum=0
        for d in str(i):
            dsum += int(d)
        sum_lst.append(dsum)
    return sum_lst

list1 = [10, 22, 30, 40, 56]
print(digit_sum(list1))


# In[70]:


#44.Break a list into chunks of size N in Python
our_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
chunked_list = []
chunk_size = 3
for i in range(0, len(our_list), chunk_size):
    chunked_list.append(our_list[i:i+chunk_size])
print(chunked_list)


# In[ ]:


#45.Python | Sort the values of first list using second list

