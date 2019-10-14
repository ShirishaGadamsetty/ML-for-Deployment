
# coding: utf-8

# ## Task 1:

# 1. Install Jupyter notebook and run the first program and share the screenshot of the output

# In[44]:


1+2


# 2. Write a program which will find all such numbers which are divisible by 7 but are not a  multipleof 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[45]:


list = []
for i in range(2000,3200):
    if i%7==0 :
        if i%5!=0:
            list.append(i)
# print(list)
s = [str(i) for i in list] 
print(",".join(s))


# 3. Write a Python program to accept the user's first and last name and then getting them      printed in the the reverse order with a space between first name and last name.
# 

# In[46]:


# print("Enter your first name")
firstname = input("Enter your first name")
lastname = input("enter your last name")
print(firstname[::-1] + " " + lastname[::-1])


# 4. Write a Python program to find the volume of a sphere with diameter 12 cm.
#    Formula: V=4/3 * π * r3

# In[47]:


r=12
pi = 3.1415926535897931
v = 4/3 * pi* r**3
print(v)


# # Task 2:
# 1. Write a program which accepts a sequence of comma-separated numbers from console and
#    generate a list.
# 

# In[48]:


values = input("enter comma seperated values")
list = values.split(",")

print('List : ',list)


# 2. Create the below pattern using nested for loop in Python.
# 

# In[49]:


for i in range(0,5):
    for j in range(0,i+1):
        print("* ",end="") #end:   string appended after the last value, default a newline.
    print("\r")  
for i in range(5,0,-1):
    for j in range(0,i+1):
        print("* ",end="") #end:   string appended after the last value, default a newline.
    print("\r")      


# 3. Write a Python program to reverse a word after accepting the input from the user.
#    Sample Output:
#    Input word: AcadGild
#    Output: dilGdacA

# In[50]:


s = input("enter your word ")
def reverse_slicing(s):
    return s[::-1]
print(reverse_slicing(s))


# In[51]:


s = input("enter your word")
s[::-1]


# 4. Write a Python Program to print the given string in the format specified in the sample output.
#    WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens

# In[52]:


print("WE, THE PEOPLE OF INDIA\n\thaving solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\tand to secure to all its citizens \n")  

