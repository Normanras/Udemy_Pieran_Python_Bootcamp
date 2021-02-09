#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Errors and Exceptions Homework

# ### Problem 1
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.

# In[1]:


for i in ['a','b','c']:
    try:
        i*i*i
        print(i**2)
    except Error:
        print("Oops! That didn't work")


# ### Problem 2
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks. Then use a <code>finally</code> block to print 'All Done.'

# In[2]:


x = 5
y = 0
try:
    z = x/y
    print(z)
except ZeroDivisionError:
    print("You can't divide by zero dude")
finally:
    print("All done")



# ### Problem 3
# Write a function that asks for an integer and prints the square of it. 
# Use a <code>while</code> loop with a <code>try</code>, 
# <code>except</code>, <code>else</code> block to 
# account for incorrect inputs.

# In[3]:

def ask():
    input=input_a

input_a = (input())
while input_a != '':
    print(input_a)
    try:
        x = (input_a)**2
        print(x)
    except ValueError or TypeError:
        print("That's not a valid input")
    else:
        print("What is happening?")
        break


# In[4]:


ask()


# # Great Job!

# %%
