#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.Python program to Find the size of a Tuple
#1.Using getsizeof() function
import sys
Tuple1 = ("A", 1, "B", 2, "C", 3)
print("Size of Tuple1: " + str(sys.getsizeof(Tuple1)) + "bytes")

#2.Using inbuilt __sizeof__() method
print("Size of Tuple1: " + str(Tuple1.__sizeof__()) + "bytes")

#The sys.getsizeof() function includes the marginal space usage, which includes the garbage collection overhead for the object.
#Python also has an inbuilt __sizeof__() method to determine the space allocation of an object without any additional 
#garbage value. 


# In[17]:


#2.Python – Maximum and Minimum K elements in Tuple
tuple1 = (70, 20, 10,110,50,40, 90)
print("The original tuple is : ",tuple1)
K = 2
tuple1=list(tuple1)
temp = sorted(tuple1)
res = tuple(temp[:K] + temp[-K:])
print(res)


# In[8]:


#3.Create a list of tuples from given list having number and its cube in each tuple

nums=[1, 2, 3]

#1.Using lambda function
cube_nums = list(map(lambda x:(x, x ** 3), nums))
print('Using lambda function:',cube_nums)

#2.Using list comprehension
res = [(val, pow(val, 3)) for val in nums]
print('Using list comprehension:',res)

#3.Using for loop
res1 = []
for i in nums:
    res1.append((i,i*i*i))
print('Using for loop:',res1)


# In[10]:


#4.Python – Adding Tuple to List and vice – versa
#1.Adding tuple to list
lst=[1,2,3,4]
tupl=(6,7)
lst += tupl
print(lst)

#2.Adding list to tuple
list1=[11,22,33]
tuple1=(88,77,99,111)
print(tuple(list(tuple1)+list1))


# In[11]:


#5.Python – Closest Pair to Kth index element in Tuple
list1=[(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
print("The original list is : ",list1)
tup = (17, 23)
K=1
min_dif, res = 999999999, None
for idx, val in enumerate(list1):
    dif = abs(tup[K - 1] - val[K - 1])
    if dif < min_dif:
        min_dif, res = dif, idx
print("The nearest tuple to Kth index element is : " + str(list1[res])) 


# In[14]:


#6.Python – Join Tuples if similar initial element
test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
res = []
for sub in test_list:                                           
    if res and res[-1][0] == sub[0]:              
        res[-1].extend(sub[1:])                        
    else:
        res.append([ele for ele in sub])     
res = list(map(tuple, res))
print("The extracted elements : ",res) 


# In[16]:


#7.Python – Extract digits from Tuple list
from itertools import chain
test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]
print("The original list is : " + str(test_list))
temp = map(lambda ele: str(ele), chain.from_iterable(test_list))
res = set()
for sub in temp:
    for ele in sub:
        res.add(ele)

print("The extracted digits : " + str(res))

#or

import re
test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]
temp = re.sub(r'[\[\]\(\), ]', '', str(test_list))
res = [int(ele) for ele in set(temp)]
print("The extracted digits : " + str(res))


# In[4]:


#8.Python – All pair combinations of 2 tuples
#Approach-1
t1=(10,20,30)
t2=(40,50)
tp_list=[]
for i in range (len(t1)):
    for j in range(len(t2)):
        tp_list.append((t1[i],t2[j]))
        tp_list.append((t2[j],t1[i]))
        
print("Approach-1:Using nested for loop : ",tp_list)

#Approach-2:Using List comprehension
res=[(a,b) for a in t1 for b in t2]+[(b,a) for b in t2 for a in t1]
print("Approach-2:Using List comprehension:",res)

#Approach-3:Using chain() + product()
from itertools import chain,product

res=list(chain(product(t1,t2),product(t2,t1)))
print("Approach-3:Using chain() + product():",res)


# In[10]:


#9.Python – Remove Tuples of Length K
#Approach-1:Using for loop
list1= [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
print("Approach-1:Using for loop")
print("List before removing tuple from list:",list1)
k=2
for ele in list1:
    if len(ele)==k:
        list1.remove(ele)
        
print("List after removing tuple from list:",list1)
print("--------------------------------------------------------------")

#Approach-2:Using list comprehension
print("Approach-2:Using list comprehension")
res=[ele for ele in list1 if len(list1)!=k]
print("List after removing tuple from list",res)
print("--------------------------------------------------------------")
#Approach-3:Using filter and lambda 
print("Approach-3:Using filter and lambda")
res=list(filter(lambda x:len(x) != k,list1))
print("List after removing tuple from list",res)


# In[12]:


#10.Sort a list of tuples by second Item
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
#Approach-1
tuple1 = list(tuple1)
tuple1.sort(key=lambda item:item[1])
print(tuple(tuple1))

#Approach-2
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)


# In[15]:


#11.Python program to Order Tuples using external List
test_list = [('Gfg', 10), ('best', 3), ('CS', 8), ('Geeks', 7)]
ord_list =['Geeks', 'best', 'CS', 'Gfg']
#Convert list of tuples into dictionary 
temp=dict(test_list)
res=[(key,temp[key]) for key in ord_list]
print(res)


# In[14]:


#12.Python – Flatten tuple of List to tuple
#Approach-1:Using chain.from_iterable()
test_tuple = ([5], [6], [3], [8])
from itertools import chain
ele=chain.from_iterable(test_tuple)
print(tuple(ele))

#Approach-2:Using tuple() and sum()
res=tuple(sum(test_tuple,[]))
print(res)


# In[17]:


#13.Python – Convert Nested Tuple to Custom Key Dictionary
#Approach-1:Using dictionary comprehension
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
res=[{'key':ele[0],'value':ele[1]} for ele in tuple1]
print(res)

#Approach-2:Using zip() + list comprehension
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
keys=['key','value']
res=[{key:val for key,val in zip(keys,ele)} for ele in tuple1]
print(res)

