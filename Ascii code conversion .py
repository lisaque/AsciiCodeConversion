#!/usr/bin/env python
# coding: utf-8

# In[3]:


StringA = input("Type something: ") #First you input the string. This also 
#prints the string typed in

StringAascii=[] #The list is created to be appended afterwards

for asccii in StringA:
    StringAascii.append(ord(asccii))  #The list is appended by the ASCII values
# of the inputted string

print(StringAascii) #List is printed with the appended values
print()

def list_multiply(multiply): #This function will return the product of the list
#multiplication
  result = 1
  for m in multiply:
    result = result*m  #This multiplies each number until the end of the array
  return result

print("The product of the ASCII code is: ",list_multiply(StringAascii))


# In[4]:


import random
random.seed(2)
RandomNumber = random.randint(len(StringA),2000000)
                            

MyValue = list_multiply(StringAascii)

XORvalue = RandomNumber ^ MyValue
#import operator
#XORvalue = operator.xor(MyValue, RandomNumber)

# Printing the XOR value
print(RandomNumber, "XOR", MyValue, "=", XORvalue)

print()

print(hex(RandomNumber), "XOR", hex(MyValue), "=", hex(XORvalue))
print()

reducedTo16 = hex(XORvalue)[0:15]

print("XOR value reduced to 16 characters & hash code: ",reducedTo16)


# In[ ]:




