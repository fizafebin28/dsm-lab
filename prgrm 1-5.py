#!/usr/bin/env python
# coding: utf-8

# In[11]:


a=int(input("Enter first no: "))
b=int(input("Enter second no: "))
ch=int(input("Enter choice:\n1.Additon\n2.Subtraction\n3.Multiplication\n4.Division\n"))
if(ch==1):      
    print("Addition: ",a+b)
elif(ch==2):
        print("Subtraction: ",a-b)
elif(ch==3):
        print("Multiplication: ",a*b)
elif(ch==4):
        if b!=0:
            print("Division: ",a/b)
        else:
            print("Division with 0 not allowed")
else:
    print("Invalid choice!!!")


# In[14]:


a=int(input("Enter first no: "))
b=int(input("Enter second no: "))
if a>0 and b>0:
    print("\nBoth nos are positive")
if a>0 or b>0:
    print("Atleast one no is positive")
if not a==b:
    print("Both nos are not equal")
if a==b:
    print("Both nos are equal")
if a>=b:
    print("First no is greater than or equal to second")
if a<=b:
    print("First no is less than or equal to second")
if a!=b:
    print("Both nos are not equal")
    


# In[21]:


dict1={"A":"Apple","B":"Balloon"}
dict2={"C":"Cat","D":"Dog"}
dict1.update(dict2)
print(dict1)


# In[24]:


a=int(input("Enter first no: "))
b=int(input("Enter second no: "))
c=int(input("Enter third no: "))

if a>b and a>c:
    print(a,"is greatest")
elif b>c:
    print(b,"is greatest")
else:
    print(c,"is greatest")


# In[51]:


lst=[1,2,3,4,5,6,7,8,9]
lst1=lst.copy()
print("Copy: ",lst1)
lst.append(10)
print("Append: ",lst)
lst.remove(10)
print("Remove: ",lst)
lst.insert(3,11)
print("Insert(11): ",lst)
lst.pop(3)
print("Pop(11): ",lst)



# In[ ]:




