
# coding: utf-8

# Q1. How can we create an iterator object from a list?
# a) Bypassing the given list to the iter() function
# b) By using a for a loop.
# c) By using a while loop.
# d) You cannot create an iterable object
# 
# 

# In[ ]:


## a) Bypassing the given list to the iter() function 

List = [1,2,3,4,5]
iteror = iter(List)
next(iteror)
next(iteror)


# Q2. If the function contains at least of one “yield” statement, then it 
# becomes ______
# Choose one
# a) An iterable
# b) a generator function
# c) an anonymous function
# d) None of the above
# 

# In[ ]:


# b) A generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# Using for loop
for item in my_gen():
    print(item)    


# Q3. What is the output of the code?
# 

# In[ ]:


# b) 1 9
mylist = [1, 3, 6, 10]
a = (x**2 for x in mylist)
print(next(a), next(a))


# Q4. What are the criteria that must be met to create closure in Python?

# In[ ]:


def transmit_to_space(message):
#   "This is the enclosing function"
  def data_transmitter():
#       "The nested function"
      print(message)
    return data_transmitter

fun2 = transmit_to_space("Burn the Sun!")
fun2()


# Q5. What is the output of the code?
# 
# Ans) 50 

# In[ ]:


def Foo(n):
    def multiplier(x):
        return x*n
    return multiplier  

a = Foo(5)
b = Foo(5)
print(a(b(2)))


# Q6. What is the output of the code?
# Ans) i got decorated
#      I am ordinary
# 

# In[ ]:


def make_pretty(func):
    def inner():
    print("i got decorated")
    func()
    return inner  

def ordinary():
    print("I am ordinary")
    
pretty = make_pretty(ordinary)
pretty()    


# Q7: What is the more pythonic way to use getters and setters?
# Ans) @property

# In[ ]:


# Python program showing the use of 
# @property 

class Geeks: 
	def __init__(self): 
		self._age = 0
	
	# using property decorator 
	# a getter function 
	@property
	def age(self): 
		print("getter method called") 
		return self._age 
	
	# a setter function 
	@age.setter 
	def age(self, a): 
		if(a < 18): 
			raise ValueError("Sorry you age is below eligibility criteria") 
		print("setter method called") 
		self._age = a 

mark = Geeks() 

mark.age = 19

print(mark.age) 


# Q8. In Python, there is a built-in function property() that returns a 
# property object. The property object has which of the methods?
# Ans) getter() setter() delete()

# Q9. Which of the following statement is true?
# a) You cannot chain multiple decorators in Python.
# b) Decorators don’t work with functions that take parameters.
# c) The @ symbol doesn’t have any use while using decorators.
# d) None of the above
# 
# 
#  Ans ) None of the above

# Q10. For the following codes, which of the following statements is true?
# Ans ) b) Both printHello() and the reference to the same object.

# In[ ]:


#b) Both printHello() and the reference to the same object.
def printHello():
    print("Hello")
a = printHello()  


# In[ ]:


get_ipython().set_next_input('Q11. What is the output of the program');get_ipython().run_line_magic('pinfo', 'program')


# In[ ]:


def outerFunction():
    global a 
    a = 20
    def innerFunction():
    global a
    a = 30
    print('a =',a)
a=10
outerFunction()
print('a =',a)    


# Q12. Which of the following statements is true?
# a) A class is a blueprint for the object.
# b) You can only make the single object from the given class
# c) Both statements are true.
# d) Neither statement is true.
# 
#  Ans) c) Both statements are true.
# 

# Q13. What is the output of the code?
# Ans ) c) Java

# In[ ]:


class Foo():
    def printLine(self , line = 'Python'):
    print(line)

ol = Foo()
ol.printLine('java')    


# Q14. What is the function of the __init__() function in Python?
# Ans ) b) This function is called, when the new object is instantiated
# 

# Q15. What is the output of the code?
# Ans) b) 1 1

# In[ ]:


class Point():
    def __init__(self , x=0 , y=0):
    self.x = x+1
    self.y = y+1

pl = Point()
print(pl.x,pl.y) 


# Q16. Which of the following code used the inheritance feature?
# 

# In[ ]:


#Ans ) c
class Foo():
   pass
class Hoo(Foo):
   pass  


# Q17 If you a class is derived from two different classes, it’s called 
# Ans) b) Multiple Inheritance

# Q18. Which of the following statements is true?
# a) In Python, the same operator may behave differently depends upon the operands.
# b) You can change the way operators which behave in Python.
# c) Special method __add()__ is called when + operator
# d) All of the above.
# 
# 
# Ans) d) All of the above.

# Q19. What is the output of the code?
# b) 4 6

# In[1]:


class point:
    def __init__(self, x=0 , y=0):
        self.x=x
        self.y=y
    def __sub__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return point(x,y)
    
p1 = point(3,4)   
p2=point(1,2)
result = p1-p2
print(result.x,result.y)


# Q20. Opening a file in ‘a’ mode
# c) opens the file for appending, at the end of file

# Q21. What does the following code do?
#  f = open("test.txt")
# b) Opens test.txt file for reading only

# Q22. Which of the codes closes files automatically if an exception occurs?
# b)
# try:
#     f = open("test.txt",encoding = 'utf-8')
# finally:
#      f.close()
# 

# Q23. For the following code,
# 1. f = open('test.txt', 'r', encoding = 'utf-8')
# 2. f.read()
# a) This program reads the content of the test.txt file.

# Q24. What does the following code do?
# c) Prints all the directories and files inside the given directory

# Q25. Which of the following is correct?
# d) All of the above.

# Q26. What will happen if we try to open the file that doesn’t exist?
# c) An exception is raised.

# c) An exception is raised.
# number = 5.0
# try:
#   r = 10/number
#   print(r)
# except:
#   print("Oops!Error Occured.")
# 
# Ans) b) 2.0

# Q28. What does the following code do?
# 1. try:
# 3.    pass
# 5. except (TypeError, ZeroDivisionError):
# 6.    print("Two")
# 
# c) Prints Two if the TypeError or ZeroDivisionError exception occurs.

# Q29. Which of the following statement is true?
# b) You can create the user-defined exception by deriving a class from Exception class.

# Q30. Which of the following statement is true?
# d) All of the above

# Q31. What is the output of the code?
# 1. def printLine(text):
# 2.   print(text, 'is awesome.')
# 4. printLine('Python')
# 
# b) Python is awesome.

# Q32. If the return statement is not used inside the function, the function will return:
# b) None object

# Q33. What is the output of the code?
# 1. def greetPerson(*name):
# 2.    print('Hello', name)
# 4. greetPerson('Frodo', 'Sauron')
# 
# b) Hello ('Frodo', 'Sauron')

# Q34. What is a recursive function?
# b) A function that calls itself.

# Q35. What is the output of the program?
# 1. result = lambda x: x * x
# 2. print(result(5))
# 
# c) 25

# Q36. What is the output of the program?
# 1. def Foo(x):
# 2.   if (x==1):
# 3.    return 1
# 4.   else:
# 5.    return x+Foo(x-1)
# 7. print(Foo(4))
# 
# a) 10

# Q37. Suppose you need to print pi constant defined in the math module. Which of the following code can do this task?
# 
# c)
# 1. from math import pi
# 2. print(pi)

# Q38. Which operator is used in Python to import modules from the packages?
# a). operator

# Q39. What is the output of the code?
# 1. numbers = [1, 3, 6]
# 2. newNumbers = tuple(map(lambda x: x , numbers))
# 3. print(newNumbers)
# 
# b) (1, 3, 6)

# Q40. What is the output of the code?
# 1. if None:
# 2.   print(“Hello”)
# 
# c) Nothing will be printed

# Q41. The if-elif-else executes only one block of code among several blocks
# a) True.

# Q42. What is the output of the code?
# 1. for i in [1,0]:
# 2.   print(i+1)
# 
# a) 2
#    1

# Q43. In the Python, for and while loop can have the optional else statement?
# c) Both loops can have optional else statement

# Q44. What is the output of the code?
# 1.i = sum = 0
# 3.while i <= 4:
# 4.  sum += i
# 5.  i = i+1
# 7.print(sum)
# 
# b) 10

# Q45. What is the output of the code?
# 1. while 4 == 4:
# 2.   print('4')
# 
# c) 4 is printed infinitely until the program closes

# Q46. Is it better to use the for loop instead of while if we are iteratingthrough a sequence?
# b) Yes, for loop is more pythonic choice.

# Q47. Which of the following statement is true?
# d) All of the above.

# Q48. What is the output of the code?
# 1. for char in 'PYTHON STRING':
# 2. if char == ' ':
# 3.     break
# 7. if char == 'O':
# 8.   continue
# 
# a) PYTHON

# Q49. Which of the statement is true about the “pass” statement?
# c) It is used as the placeholder for future implementation of functions, loops, etc

# Q50. In regards to separated value files such as .csv and .tsv, what is the delimiter?
# c) Any character such as the comma (,) or tab (\t) that is used to separate the column data.

# Q51. In separated value files such as .csv and .tsv, what does the first row in the file typically contain?
# a) The column names of the data.

# Q52. Assume you have a file object my_data, which has properly 
# opened a separated value file that uses the tab character (\t) as the delimiter.
# What is the proper way to open the file using the Python CSV module and assign it to the variable csv_reader?
# 
# b) csv.reader(my_data, delimiter='\t')
# 

# Q53. When iterating over an object returned from csv.reader(), what is returned with each iteration?
# for item in csv_reader:
#  print(item)
# 
# d) The column data as a list

# Q54. When writing to a CSV file using the .writerow() method of the csv.DictWriter object, what must each key in the input dict represent? Below is an example:
# with open('test_file.csv', mode='w') as csv_file:
#  writer = csv.DictWriter(
#    csv_file,
#  fieldnames=['first_col', 'second_col']
#  )
#  writer.writeheader()
#  writer.writerow({'key1':'value1', 'key2':'value2'})
#  
# c) Each key must match up to the field names (column names) used to identify the column data 

# Q55. Which is the correct way to open the CSV file hrdata.csv for reading using the pandas package? Assume that the pandas package has already been imported.
# 
# c) pandas.read_csv('hrdata.csv')

# Q56. By default, pandas uses 0-based indices for indexing rows. Which is the correct way to import the CSV file hrdata.csv for reading and using the 'Name' column as the index row instead?
# 
# a) pandas.read_csv('hrdata.csv', index_col='Name')
# 

# Q57. Given the file dog_breeds.txt, which of the following is the correct way to open the file for reading as a text file? Select all that apply.
# 
# b) open('dog_breeds.txt', 'r')

# Q58. Given the following directory structure:
# 
# Ans)animals\feline

# Q59. Given the file jack_russell.png, which of the following is the correct way to open the file for reading as a buffered binary file? Select all that apply.
# 
# Ans) open('jack_russell.png', 'rb')

# Q60. Using the same directory structure as before:
# 
# Ans) animals\ursine\bears.gif

# Q61. Whenever possible, what is the recommended way to ensure that a file object is properly closed after usage?
# 
# c) By using the try/finally block

# Q62. Using the same directory structure as before:
# 
# Ans) feline\animals\ursine\bears.gif

# Q63. When reading a file using the file object, what method is best for reading the entire file into a single string?
# 
# d) .readline()

# Q64. The value 1.73 rounded to one decimal place using the “rounding up” strategy is…
# a) 1.8

# Q65. The value -2.961 rounded to two decimal places using the “rounding down” strategy is…
# a) -2.96

# Q66. When a value is truncated to 3 decimal places, which of the following is true?
# a) Positive numbers are rounded up, and negative numbers are rounded down.

# Q67. The value -0.045 rounded to 2 decimal places using the “round half away from zero” strategy is…
# b) -0.04

# Q68. Which rounding strategy does Python’s built-in round() function use?
# 

# Q69. The value 4.65 rounded to one decimal place using the “round half to even” strategy is…
# a) 4.6

# Q70. Which problem arises due to the multiple inheritances, if hierarchical inheritance is used previously for its base classes?
# 
# a) Diamond

# Q71. How many classes should a program contain to implement the multiple inheritances?
# c) At least 3

# Q72. If class a inherits class b and class c as “class a: public class b, public class c {// class body ;}; ”, which class constructor will be called first?
# b) Class B

# Q73.If all the members of all base classes are private then,
# a) There won’t be any use of multiple inheritance

# Q74. Can the derived class be made abstract if multiple inheritance is used?
# d) No, since constructors won’t be there

# Q75. Which among the following best defines the multilevel inheritance?
# c) Continuing single level inheritance

# Q76. If there are 5 classes, E is derived from D, D from C, C from B and B from A. Which class constructor will be called first if the object of E or D is created?
# 
# a) A
# 

# Q77. Which Class is having the highest degree of abstraction in multilevel inheritance of 5 levels?
# a) Class at 1st level

# Q78. Multilevel inheritance allows _________________ in the program.
# d) As many levels of inheritance as required

# Q79. If all the classes used parameterized constructors and no default constructor then, ___________
# 
# b) Object of lower level classes must call parent class constructors explicitly

# Q80. Which is the universal exception handler class?
# d) Exceptions

# Q81. What are two exception classes in the hierarchy of java exceptions class?
# c) Runtime exceptions and other exceptions

# Q82. Which are the two blocks that are used to check error and handle the error?
# a) Try and catch

# Q83. To catch the exceptions ___________________
# a) An object must be created to catch the exception

# Q84. Which class is used to handle the input and output exceptions?
# c) IOExceptions

# Q85. Which among the following is true for the class exceptions?
# c) Either base or derived class may produce exceptions

# Q86. If both base and derived class caught the exceptions, _____.
# a) Then catch block of a derived class must be defined before the base class

# Q87. The catching of base class the exception _________ in java.
# b) Before derived class is not allowed by compiler

# Q88. Which of the following handles the undefined class in the program?
# d) ClassNotFoundException

# Q89. Which among the following is true?
# c) Both the base and derived class catch the blocks are important.

# Q90. Which condition among the following might result in memory exception?
# c) Infinite loops

# ##Q91. Which among the following is the correct definition for static member functions?
#  
# ##ANS ) b) Functions made to maintain a single copy of member functions for all the objects
# 

# ##Q92. The static member functions __________________
# ##Ans) c) Having access to only the static members of a class.
# 

# ##Q93. Which is the correct syntax to access the static member with a class name?
# functions 
# ##a) className . functionName;
#  

# ##Q94. The static members are ______________________
# 
# Ans) d) Created and initialised, only once
# 

# ##Q95. Which among the following is true?
# b) Static member functions can’t be overloaded.
#  

# ##Q96. The static member functions _______________
# 
# d) Can’t be declared const, volatile or const volatile
# 

# Q97. Which among the following can’t be used to access the members in anyway?
# c) Single colon.
# 

# Q98. If static data member are made inline, ______________
# c) Those can be initialized within the class
# 

# Q99. The static data member _________________
# b) Can’t be mutable
# 

# Q100. We can use the static member functions and static data member 
# a) Even if class object is not created
# 

# Q101. Point out the wrong statement:
# c) rPy provides lots of scientific routines that work on top of NumPy.
# 

# Q102. The ________ function returns its argument with the modified  shape, whereas the ________ method modifies the array itself.
# a) reshape,resize
# 
# 

# Q103. To create sequences of the numbers, NumPy provides a function __________ 
# 
# analogous to range that returns arrays instead of lists.
# 
# a) arange
# 

# 5. Point out the correct statement:
# 
# d) All of the Mentioned
# 

# Q105. Which of the following function stack 1D array as the columns into the 2D array?
# b) column_stack
# 

# Q106. ndarray is also known as an alias array.
# a) False
# 

# Q107. Which of the following method creates the new array object that looks at the same data?
# b) copy.

# Q108. Which of the functions can be used to combine the different vectors to obtain the result for each n-uplet?
# b) ix_

# Q109. ndarray.dataitemSize is the buffer containing actual elements of an array.
# a) True
# 

# Q110. Which of the following is in the NumPy library?
# d) all of the Mentioned

# Q111. Which of the following sets the size of the buffer used in ufuncs ?
# c) setbufsize(size)
# 

# 112. Point out the wrong statement.
# b) In Numpy, universal functions are instances of the numpy.ufunction class

# Q113. Which of the following attribute should be used while checking the type combination input and output?
# a) .types

# Q114. Which of the following returns an array of “ones” with the same shape and type as a given array?
# b) ones_like

# Q115. Point out the wrong statement:
# c) The output of the ufunc is necessarily an ndarray, if all input arguments are ndarrays

# Q116. Which of the following set of a floating-point error callback function or a log object?
# b) settercall

# Q117. Some ufuncs can take output arguments.
# b) False

# Q118. ___________ decompose the elements of x into the mantissa and the two’s exponent.
# c) frexp

# Q119. Which of the following function take the only a single value as input?
# a) iscomplex

# Q120. The array object returned by the _array_prepare_ is passed to  ufunc for computation.
# a) True

# Q121. All pandas data structures are ___mutable but not always _______-mutable.
# c) value,size

# Q122. Point out the correct statement:
# d) All of the Mentioned
# 

# Q123. Which of the following statement will import the pandas?
# a) import pandas as pd

# Q124. Which of the following object did we get after reading the CSV file?
# a) DataFrame

# Q125. Point out the wrong statement:
# c) The panel is generally 2D labelled, also a size-mutable array.

# Q126. Which of the following library is similar to the pandas?
# a) NumPy

# Q127. Panel is a container for the Series, and DataFrame is a container for DataFrame objects.
# b) False

# Q128. Which of the following is the prominent python “statistics and econometrics library”?
# a) Bokeh

# Q129. Which of the following is the foundational exploratory visualisation package for the R language in the pandas ecosystem?
# a) yhat

# Q130. Pandas consist of static and the moving window linear and panel regression.
# a) True

# Q131. Quandl API for Python wraps the __ REST API to returns the pandas DataFrames with time series indexes.
# a) Quandl

# Q132. Point out the correct statement:
# a) Statsmodels provides powerful statistics, econometrics, analysis and modeling functionality that is out of panda’s scope

# Q133.Which of the following library is used to retrieve and to acquire statistical data and metadata disseminated in SDMX 2.1?
# a) pandaSDMX

# Q134. Which of the following provides the standard API for doing computations with MongoDB?
# a) Blaze

# Q135. Point out the wrong statement:
# c) Spyder is a cross-platform Qt-based open-source R IDE

# Q136. Which of the following makes use of the pandas and returns data in a Series or DataFrame?
# 
# b) freedapi

# Q137. Spyder can introspect and display Pandas DataFrames.
# b) False

# Q138. Which of the following is used for machine learning in the python?
# a) sci-kit-learn.

# Q139. The ________ project builds on top of the pandas and matplotlib to provide easy plotting of data.
# b) Seaborn

# Q140 x-ray brings the labelled data power of pandas to the physical sciences.
# a) True

# Q141. Which of the following is the base layer of all of the sparse has it indexed data structures?
# b) SparseArray

# Q142. Point out the correct statement.
# d) All of the mentioned
# 

# Q143. Which of the following is not an indexed object?
# d) None of the mentioned

# Q144. Which of the following list like data structure is used for managing the dynamic collection of SparseArrays?
# a) SparseList

# Q145. Point out the wrong statement.
# a) to_array. append can accept scalar values or any 2-dimensional sequence

# Q146. Which of the following method used for transforming the Sparse-series index by the MultiIndex to a scipy.sparse.coo_matrix?
# a) SparseSeries.to_coo()

# Q147. The integer format tracks only the locations and the sizes of blocks of data.
# b) False

# Q148. Which of the following is used for the testing for membership in the list of column names?
# a) in

# Q149. Which of the following indexing capabilities is used as the concise means of selecting data from a pandas object?
# b) ix

# Q150. Pandas follow the NumPy convention of raising an error when you try to convert something to a bool.
# a) True
