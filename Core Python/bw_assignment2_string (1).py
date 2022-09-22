#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.Python program to check if a string is palindrome or not
def check_palindrome(str):
    if str == str[::-1]:
        print(str," is palindrome")
    else:
        print(str," is not palindrome")

check_palindrome('OYO')


# In[ ]:


#2.	Reverse words in a given String in Python
def reverse_str(str):
    return str[::-1]
print(reverse_str('Hello Word!'))


# In[ ]:


#4.Ways to remove i’th character from string in Python
def remove_char(str,i):
    return str[:i-1]+str[i:] 

print(remove_char('Pallavi',3))


# In[ ]:


#5.Python | Check if a Substring is Present in a Given String
def check_substr(str,substr):
    if substr in str:
        print(substr,' is present in ',str)

check_substr('Pallavi','avi')


# In[15]:


#6.Python – Words Frequency in String Shorthands
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'
print("The original string is : " + str(test_str))
res = {key: test_str.count(key) for key in test_str.split()}
print("The words frequency : " + str(res)) 


# In[ ]:


#7.Python – Convert Snake case to Pascal case
str='Hello_world'
pascal_str=str.replace("_"," ").title()
pascal_str=pascal_str.replace(" ","")
print(pascal_str)


# In[ ]:


#8.Find length of a string in python (4 ways)
str="Hello World!"
#1.Using len()
print("Using len method: ",len(str))
#2.Using for loop
cnt=0
for i in str:
    cnt += 1
print("Using for loop: ",cnt)
#3.Using while loop
counter=0
while(str[counter:]):
    counter +=1
print("Using while loop: ",counter)


# In[ ]:


#9.Python program to print even length words in a string
def even_word(str):
    s=str.split()
    for word in s:
        if len(word)%2==0:
            print(word)
s = "Pallavi is writting python code"
even_word(s)


# In[ ]:


#10.Python program to accept the strings which contains all vowels
def check(string):
    string = string.replace(' ', '')
    string = string.lower()
    vowel = [string.count('a'), string.count('e'), string.count(
        'i'), string.count('o'), string.count('u')]
 
    # If 0 is present in vowel count array
    if vowel.count(0) > 0:
        return('not accepted')
    else:
        return('accepted')

print(check("eutopia"))
print(check("Pallavi"))


# In[ ]:


#11.Python | Count the Number of matching characters in a pair of string
def count(str1, str2):
    c, j = 0, 0
    for i in str1:
        if str2.find(i)>= 0 and j == str1.find(i): 
            c += 1
        j += 1
    print('No. of matching characters are : ', c)

str1 ='aabcddekll12@' # first string
str2 ='bb2211@55k' # second string
count(str1, str2)


# In[ ]:


#12.Remove all duplicates from a given string in Python
def unique(s):
    st = ""
    length = len(s)
    for i in range(length):
        c = s[i]
        if c not in st:
            st += c
    return st

s = "geeksforgeeks"
print(unique(s))


# In[ ]:


#13.Python – Least Frequent Character in String
test_str = "GeeksforGeeks"
  
print ("The original string is : " + test_str)

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = min(all_freq, key = all_freq.get) 
print ("The minimum of all characters in GeeksforGeeks is : " ,res)


# In[ ]:


#14.Python | Maximum frequency character in String
test_str = "GeeksforGeeks"
  
print ("The original string is : " + test_str)
all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

res = max(all_freq, key = all_freq.get) 
print ("The maximum of all characters in GeeksforGeeks is : " ,res)


# In[ ]:


#15.Python | Program to check if a string contains any special character
import re

strn = input('Enter any string: ')

# check string contains special characters or not
if(bool(re.search('^[a-zA-Z0-9]*$', strn)) == True):
    print('String does not contain any special characters.')
else:
    print('The string contains special characters.')


# In[ ]:


#16.Generating random strings until a given string is generated
import string
import random
import time

possibleCharacters=string.ascii_lowercase+string.ascii_uppercase

t=str(input('Enter String'))

attemptThis=''.join(random.choice(possibleCharacters) for i in range(len(t)))
attemptNext = ''
 
completed = False
iteration = 0
while completed==False:
    print(attemptThis)
    attemptNext=''
    completed = True
    # Fix the index if matches with 
    # the strings to be generated
    for i in range(len(t)):
        if attemptThis[i] != t[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += t[i]
             
    # increment the iteration 
    iteration += 1
    attemptThis = attemptNext
    time.sleep(0.1)

print("Target matched after ",iteration," iterations")


# In[1]:


#17.Find words which are greater than given length k
myStr =  input('Enter the string : ')
k = int(input('Enter k :'))
largerStrings = []
words=myStr.split(" ")
for word in words:
    if len(word)>k:
        largerStrings.append(word)
        
print("Words greater than given length: ",largerStrings)


# In[2]:


#18.Python program for removing i-th character from a string
myStr =  input('Enter the string : ')
k = int(input('Enter i : '))
res=myStr[:k]+myStr[k+1:]
print(res)


# In[3]:


#19.Python program to split and join a string
myStr =  input('Enter the string : ')
str1=myStr.split(" ")
res='-'.join(str1)
print(res)


# In[4]:


#20.Python | Check if a given string is binary string or not
def check(string) :
    b = set(string)
    s = {'0', '1'}
    if s == b or b == {'0'} or b == {'1'}:
        print("Binary String")
    else :
        print("Non Binary String")

s1= "00110101"
check(s1)
s2 = "1010100200111"
check(s2)


# In[5]:


#21.Python program to find uncommon words from two Strings
def uncommon(s1,s2):
    list_s1 = s1.split()
    list_s2 = s2.split()
    uc_words = ""
    for i in list_s1:
        if i not in list_s2:
            uc_words =  uc_words+" "+i
    for j in list_s2:
        if j not in list_s1:
             uc_words =  uc_words+" "+j
  
    return  uc_words
  
a = "berry mango cherry"
b = "berry peach cherry"
print(uncommon(a,b))


# In[7]:


#22.Python – Replace duplicate Occurrence in String
strng="Sonali is a girl. Sonali is good in Math , Math is her favourite subject."

replace_dict={'Sonali':'She','Math':'that'}

visited_list=[]
string_list=strng.split(" ")

for i in string_list:
    if i in visited_list:
        if i in replace_dict.keys():
            visited_list.append(replace_dict[i])
        else:
            visited_list.append(i)
    else:
        visited_list.append(i)
    
print(' '.join(visited_list))


# In[ ]:


#23.Python – Replace multiple words with K
sample_string = "This is a sample string"
char_to_replace = ['is','string']
repl_wrd = 'test'
res = ' '.join([repl_wrd if idx in char_to_replace else idx for idx in sample_string.split()])
print(res)


# In[9]:


#24.Python | Permutation of a given string using inbuilt function
from itertools import permutations
input_str=str(input('Enter String:'))
words = [''.join(p) for p in permutations(input_str)]
print(words)

#OR
input_str1=str(input('Enter String:'))
def get_permutation(string, i=0):

    if i == len(string):   	 
        print("".join(string))

    for j in range(i, len(string)):

        words = [c for c in string]
   
        # swap
        words[i], words[j] = words[j], words[i]
 
        get_permutation(words, i + 1)

print(get_permutation(input_str1))


# In[11]:


#25.Python | Check for URL in a String
import re
def findURL(string):
    regex=r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url= re.findall(regex,string)
    return [x[0] for x in url]

input_str1=str(input('Enter String:'))
s=findURL(input_str1)
if s!= '':
    print(s)
else:
    print("URL not found")


# In[12]:


#26.Execute a String of Code in Python
def execute_code():
    Code="""
def sum(num1,num2):
  sum=num1+num2
  return sum
print(sum(12,28)) """

    exec(Code)

execute_code()


# In[14]:


#27.String slicing in Python to rotate a string
def rotate_string(s,d):
    return s[d:]+s[:d]
    
    
str1=str(input('Enter String:'))
idx=int(input("Enter index for slicing:"))
rstr=rotate_string(str1,idx)
print(rstr)


# In[16]:


#28.String slicing in Python to check if a string can become empty by recursive deletion
def check_empty(str1,sub_str):
    while(len(str1) != 0):
        try:
            idx=str1.index(sub_str)
        except valueError:
            return False
        str1=str1[0:idx]+str1[idx+len(sub_str):]
        print(str1)
    return True
        

str1=str(input("Enter string:"))
sub_str=str(input("Enter sub string:"))

print(check_empty(str1,sub_str))


# In[17]:


#29.Python Counter| Find all duplicate characters in string
from collections import Counter

word="Programming"
word_length=Counter(word)
for k,v in word_length.items():
    if v>1:
        print(f"{k} is happening {v} times")


# In[18]:


#30.Python – Replace all occurrences of a substring in a string
test_str = "Java Programming"
  
# printing original string
print("The original string is : " + test_str)
  
# Swap Binary substring
# Using translate()
temp = str.maketrans("Java", "Pyth")
test_str = test_str.translate(temp)
  
# printing result 
print("The string after swap : " + str(test_str)) 

