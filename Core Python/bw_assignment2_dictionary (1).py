#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Python – Extract Unique values dictionary values
#Approach-1
test_dict = {'a' : [5, 6, 7, 8],
             'b' : [10, 11, 7, 5],
             'c' : [6, 12, 10, 8],
             'd' : [1, 2, 5]}
unique_list=[]
l2=list(test_dict.values())
for list in l2:
     for number in list:
            if number not in unique_list:
                unique_list.append(number)
            
print(sorted(unique_list))

#Approach-2
res = list(sorted({ele for val in test_dict.values() for ele in val}))
print(res)

#Approach-3
from itertools import chain
res = list(sorted(set(chain(*test_dict.values()))))
print(res)


# In[5]:


#2.Python program to find the sum of all items in a dictionary
input_dict= {'a': 100, 'b':200, 'c':300}

#Approach-1:Using sum
print("Sum :",sum(input_dict.values()))

#Approach-2:Using for loop
sumd = 0
for i in input_dict:
    sumd = sumd + input_dict[i]
print("Sum: ",sumd)
      


# In[10]:


#3.Python | Ways to remove a key from dictionary
#Method 1 : Using del
names_dict={"Sonali":25,"Arpita":22,"Rohan":24,"Dhruv":25}
print("Original dictionary",names_dict)
del names_dict["Dhruv"]
print("Dictionary after removing key Using del",names_dict)

print('---------------------------------------------------------------------------------------------')

#Method 2 : Using pop()
names_dict={"Sonali":25,"Arpita":22,"Rohan":24,"Dhruv":25}
print("Original dictionary",names_dict)
names_dict.pop("Dhruv")
print("Dictionary after removing key Using pop()",names_dict)

print('---------------------------------------------------------------------------------------------')

#Method 3 : Using items() + dict comprehension
names_dict={"Sonali":25,"Arpita":22,"Rohan":24,"Dhruv":25}
new_dict = {key:val for key, val in names_dict.items() if key != 'Dhruv'}
print("Dictionary afterUsing items() + dict comprehension",new_dict)


# In[18]:


#4.Ways to sort list of dictionaries by values in Python – Using itemgetter
from operator import itemgetter
lis = [{ "name" : "Nandini", "age" : 20}, 
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

# using sorted and itemgetter to print list sorted by age 
print("The list printed sorting by age: ")
print(sorted(lis, key=itemgetter('age')))

# using sorted and itemgetter to print list sorted by both age and name
print("The list printed sorting by age and name: ")
print(sorted(lis, key=itemgetter('age', 'name')))

# using sorted and itemgetter to print list sorted by age in descending order
print( "The list printed sorting by age in descending order: ")
print(sorted(lis, key=itemgetter('age'),reverse = True))


# In[21]:


#5.Ways to sort list of dictionaries by values in Python – Using lambda function
lis = [{ "name" : "Nandini", "age" : 20}, 
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

# using sorted and itemgetter to print list sorted by age 
print("The list printed sorting by age: ")
print(sorted(lis,key= lambda i: i['age']))

# using sorted and itemgetter to print list sorted by both age and name
print("The list printed sorting by age and name: ")
print(sorted(lis,key= lambda i: (i['age'],i['name'])))

# using sorted and itemgetter to print list sorted by age in descending order
print( "The list printed sorting by age in descending order: ")
print(sorted(lis, key= lambda i: i['age'],reverse = True))


# In[22]:


#6.Python | Merging two Dictionaries
#Approach-1:Using update() method
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print("Using update() method:",dict1)

#Approach-2:Using **
dict3 = {**dict1, **dict2}
print("Using ** :",dict3)

#Approach-3:Using copy()
dict3 = dict1.copy()
dict3.update(dict2)
print("Using copy() : ",dict3)


# In[24]:


#7.Python – Convert key-values list to flat dictionary
month_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}
res = dict(zip(month_dict['month'], month_dict['name']))
print(res)


# In[25]:


#8.Python – Insertion at the beginning in OrderedDict
from collections import OrderedDict

iniordered_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])
# inserting items in starting of dict
iniordered_dict.update({'manjeet':'3'})
iniordered_dict.move_to_end('manjeet', last = False)
 
# print result
print ("Resultant Dictionary : "+str(iniordered_dict))


# In[26]:


#9.Python | Check order of character in string using OrderedDict( )
from collections import OrderedDict 
  
def checkOrder(input, pattern): 
    # create empty OrderedDict 
    # output will be like {'a': None,'b': None, 'c': None} 
    dict = OrderedDict.fromkeys(input) 
  
    # traverse generated OrderedDict parallel with 
    # pattern string to check if order of characters 
    # are same or not 
    ptrlen = 0
    for key,value in dict.items(): 
        if (key == pattern[ptrlen]): 
            ptrlen = ptrlen + 1
          
        # check if we have traverse complete 
        # pattern string 
        if (ptrlen == (len(pattern))): 
            return 'true'
  
    # if we come out from for loop that means 
    # order was mismatched 
    return 'false'

input = 'engineers rock'
pattern = 'egr'
print (checkOrder(input,pattern)) 


# In[28]:


#10.Dictionary and counter in Python to find winner of election
#Approach-1
votes = ['Giggs', 'Giggs', 'Greg', 'Joan', 'Jenny', 'Jenny', 'Jenny', 'Jones']
votes_dict = {}
for contestant in votes:
    if contestant in votes_dict:
        votes_dict[contestant] += 1
    else:
        votes_dict[contestant] = 1
#print(votes_dict) this will give tuple with contestant name and count
contestants_sorted=sorted(votes_dict.items(),key=lambda contestant:contestant[1],reverse=True)
print(contestants_sorted[0])

#Approach-2
from collections import Counter
votes = ['Giggs', 'Giggs', 'Greg', 'Joan', 'Jenny', 'Jenny', 'Jenny', 'Jones']
votes_counter = Counter(votes)
#get winner using Counter's most_common() method.
top_contestant_info = votes_counter.most_common(1)
winner, top_votes = top_contestant_info[0]
print('{} won with {} votes.'.format(winner, top_votes))


# In[30]:


#11.Python – Append Dictionary Keys and Values ( In order ) in dictionary
#Approach-1
test_dict = {"Python" : 1, "is" : 2, "Best" : 3}
res=list(test_dict.keys())+list(test_dict.values())
print(res)

#Approach-2
from itertools import chain
# chain() is used for concatenation
res = list(chain(test_dict.keys(), test_dict.values()))
print(res)


# In[33]:


#12.Python | Sort Python Dictionaries by Key or Value
#Approach-1-Sort by key
test_dict = {"Python" : 4, "is" : 2, "Best" : 3}
res={k: v for k, v in sorted(test_dict.items(), key=lambda item: item[0])}
print(res)

#Approach-2-Sort by value
test_dict = {"Python" : 4, "is" : 2, "Best" : 3}
res={k: v for k, v in sorted(test_dict.items(), key=lambda item: item[1])}
print(res)

#Approach-3-Using dict()+sorted()
print(dict(sorted(test_dict.items(), key=lambda item: item[1])))


# In[37]:


#13.Python – Sort Dictionary key and values List
#Method #1 : Using sorted() + loop
test_dict = {'Python': [7, 6, 3], 
             'is': [2, 10, 3], 
             'best': [19, 4]}
res = dict()
for key in sorted(test_dict):
    res[key] = sorted(test_dict[key])
print(res)

#Method #2: Using dictionary comprehension + sorted()
res = {key : sorted(test_dict[key]) for key in sorted(test_dict)}
print(res)


# In[3]:


#14.Handling missing keys in Python dictionaries
#Approach-1:Using get() Method to handle KeyError
country_dict = {'India' : 'IN', 'Australia' : 'AU', 'Brazil' : 'BR'}
print(country_dict.get('Australia', 'Not Found'))
print(country_dict.get('Canada', 'Not Found'))

#Approach-2:Using setdefault() Method to handle KeyError
country_dict = {'India' : 'IN', 'Australia' : 'AU', 'Brazil' : 'BR'}
country_dict.setdefault('Canada', 'Not Present') #Set a default value for Canada
print(country_dict['Australia'])
print(country_dict['Canada'])

#Approach-3:Using defaultdict
import collections as col
#set the default factory with the string 'key not present'
country_dict = col.defaultdict(lambda: 'Key Not Present')
country_dict['India'] = 'IN'
country_dict['Australia'] = 'AU'
country_dict['Brazil'] = 'BR'
print(country_dict['Australia'])
print(country_dict['Canada'])


# In[8]:


#15.Python dictionary with keys having multiple inputs
#Approach-1
sample_dict={}
a,b,c=5,3,10
p,q,r=12,6,9
sample_dict["x-y+z"]=[a-b+c,p-q+r]
print(sample_dict)

print("\n------------------------------------------------------------------------------------------")
#Approach-2
# dictionary with multiple inputs in a key
# function to add multiple values
def add_values_in_dict(dic, key, list_of_values):
#Append multiple values to a key in the given dictionary
    if key not in dic:
        dic[key] = list()
    dic[key].extend(list_of_values)
    return dic
 
# dictionary containing states and its cities
places = {("Maharashtra"):["Mumbai","Pune","Nagpur"],
          ("Madhya Pradesh"):["Delhi","Bhopal","Indore"]}
 
print('\n',places)

#adding values
add_val=add_values_in_dict(places, "Madhya Pradesh", ["Ujjain", "Sagar"])
print("After adding values")
print(add_val)


# In[9]:


#16.Print anagrams together in Python using List and Dictionary
def Anagram(d1):  
    # empty dictionary for anagrams together 
    dict = {} 
   # traversal 
    for val in d1: 
       # sorts list
        key = ''.join(sorted(val)) 
          
        if key in dict.keys(): 
            dict[key].append(val) 
        else: 
            dict[key] = [] 
            dict[key].append(val) 
  
    # traverse dictionary and join keys together 
    result = "" 
    for key,value in dict.items(): 
        result = result + ' '.join(value) + ' '
  
    return result 
  
d1=['act', 'cat', 'silent','listen']
print("Words: ",d1)
print("Anagram: ",Anagram(d1))


# In[10]:


#17.K’th Non-repeating Character in Python using List Comprehension and OrderedDict
from collections import OrderedDict 
  
def kthRepeating(input,k): 
  
    # OrderedDict returns a dictionary data 
        # structure having characters of input 
    # string as keys in the same order they 
        # were inserted and 0 as their default value 
    dict=OrderedDict.fromkeys(input,0) 
  
    # now traverse input string to calculate frequency of each character 
    for ch in input: 
        dict[ch]+=1
  
    # now extract list of all keys whose value is 1 from dict Ordered Dictionary 
    nonRepeatDict = [key for (key,value) in dict.items() if value==1] 
      
    # now return (k-1)th character from above list 
    if len(nonRepeatDict) < k: 
        return 'Less than k non-repeating characters in input.' 
    else: 
        return nonRepeatDict[k-1] 
  
 
input = "geeksforgeeks"
k = 3
print (kthRepeating(input, k))


# In[11]:


#18.Check if binary representations of two numbers are anagram
from collections import Counter
def checkAnagram(n1,n2):
    # convert numbers into binary.bin() returns output starting with 0b
    #so use slicing from index 2
    bin1 = bin(n1)[2:]
    bin2 = bin(n2)[2:]
    # append zeros in shorter string
    zeros = abs(len(bin1)-len(bin2))
    if (len(bin1)>len(bin2)):
         bin2 = zeros * '0' + bin2
    else:
         bin1 = zeros * '0' + bin1
    # convert binary to  dictionary
    dict1 = Counter(bin1)
    dict2 = Counter(bin2)
  
    # compare both dictionaries
    if dict1 == dict2:
         print('Yes')
    else:
         print('No')
n1 = 12
n2 = 3
checkAnagram(n1,n2)


# In[ ]:


#19.Python Counter to find the size of largest subset of anagram words
from collections import Counter
def maxAnagramSize(input):
    input = input.split(" ")

    for i in range(0, len(input)):
        input[i] = "" . join( sorted(input[i]))
        
    print(input)
    freqDict = Counter(input)
    print(freqDict)


    print(max(freqDict.values()))
    
input = 'ant magenta magnate tan gnamate'
maxAnagramSize(input)


# In[16]:


#20.Python | Remove all duplicates words from a given sentence
#Approach-1:Using fromKeys()
string = "Python is good Python is for beginners"
print(' '.join(dict.fromkeys(string.split())))

#Approach-2:using dictionary and Counter() method
from collections import Counter 
def remove_duplicate(s):
    s = s.split(" ")
    word_dic = Counter(s)
    result = " ".join(word_dic.keys())
    print (result)

st='There are two children children playing in the park'
remove_duplicate(st)

#Approach-3:Using count()
string = "Python is good and Java is also good"
words_str = string.split()
result = []
for word in words_str:
    # store unique words in list
    if (string.count(word)>=1 and (word not in result)):
        result.append(word)
print(' '.join(result))

#Approach-4:Using in operator
def unique_list(text_str):
    l = text_str.split()
    temp = []
    for x in l:
        if x not in temp:
            temp.append(x)
    return ' '.join(temp)

text_str = 'Python Exercises Practice Solution Exercises'
unique_list(text_str)


# In[ ]:


#21.Python Dictionary to find mirror characters in a string
def MirrorChar(string,k):
 
    # create dictionary
    order = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictChars = dict(zip(order,reverse))
 
    # divide string at k    
    pre = string[0:k-1]
    suffix = string[k-1:]
    mirror = ''
 
    for i in range( len(suffix)):
         mirror = mirror + dictChars[suffix[i]]
 
    return pre+mirror
          
print("Mirrored string: ",MirrorChar('Pallavi',4))


# In[17]:


#22.Counting the frequencies in a list using dictionary in Python
#Approach-1:Using Counter
from collections import Counter
list1=['a','a','a','b','b']
count_dict=Counter(list1)
print(count_dict)

#Approach-2:Using user defined function
def countFreq(lst):
    output_dict={}
    for i in lst:
        if i in output_dict:
            output_dict[i] += 1
        else:
            output_dict[i] = 1
    return output_dict
            
list1=['a','a','a','b','b']
print(countFreq(list1))


# In[18]:


#23.Python | Convert a list of Tuples into Dictionary
tups = [("akash", 10), ("gaurav", 12), ("anand", 14), 
    ("suraj", 20), ("akhil", 25), ("ashish", 30)]
print(dict(tups))


# In[ ]:


#24.Python counter and dictionary intersection example (Make a string using deletion and rearrangement)
#Given two strings, find if we can make first string from second 
#by deleting some characters from second and rearranging remaining characters.
from collections import Counter
def makeString(str1,str2):
    dict1 = Counter(str1)
    dict2 = Counter(str2)
    
    # take intersection of two dictionries
    result = dict1 & dict2
    
    return result == dict1

str1 = 'ABHISHEKsinGH'
str2 = 'gfhfBHkooIHnfndSHEKsiAnG'
if (makeString(str1,str2)==True):
    print("Possible")
else:
    print("Not Possible")


# In[19]:


#25.Python dictionary, set and counter to check if frequencies can become same
from collections import Counter
  
def allSame(input):
      
    dict=Counter(input)
    same = list(set(dict.values()))
  
    if len(same)>2:
        print('No')
    elif len (same)==2 and same[1]-same[0]>1:
        print('No')
    else:
        print('Yes')
        
input = 'zzzzzzzz'
allSame(input)


# In[20]:


#26.Scraping And Finding Ordered Words In A Dictionary using Python
import requests 
def scrapeWords(): 
    scrape_url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    scrapeData = requests.get(scrape_url) 
    listofwords = scrapeData.content 
    listofwords = listofwords.decode("utf-8").split() 
    return listofwords 
def isOrdered(): 
    collection = scrapeWords() 
    collection = collection[:100] 
    word = '' 
    for word in collection:
        result = 'Word is ordered'
        i = 0
        l = len(word) - 1
        if (len(word) < 3): 
            continue
        while i < l:
            if (ord(word[i]) > ord(word[i+1])): 
                result = 'Word is not ordered'
                break
            else: 
                i += 1 
        if (result == 'Word is ordered'):
            print(word,': ',result) 
isOrdered()


# In[21]:


#27.Possible Words using given characters in Python
def Countchar(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict
def find_words(word_list, charSet):
    for word in word_list:
        flag = 1
        chars = Countchar(word)
        for key in chars:
            if key not in charSet:
                flag = 0
            else:
                if charSet.count(key) != chars[key]:
                    flag = 0
        if flag == 1:
            print(word)
# input            
word_list = ['mat', 'boy', 'bat', 'goal', 'get', 'got', 'orange']
charSet = ['e', 'o', 'b', 'a', 'g', 'l', 't']
find_words(word_list, charSet)


# In[22]:


#28.Python – Keys associated with Values in Dictionary
test_dict = {'gfg' : [4, 5], 'is' : [8], 'best' : [10, 12]}
val_list = [5, 10]
temp = {}
for key, vals in test_dict.items():
    for val in vals:
        temp[val] = key
res = [temp[ele] for ele in val_list]
print("The keys mapped to " + str(val_list) + " are : " + str(res)) 

