
# coding: utf-8

# Q1. Write a Python program to get the string from the given string where 
# all the occurrence of its first char has been changed to '$,' except first 
# char itself?

# In[15]:


given_string = 'prospect'
a =given_string.replace(given_string[0],'$')
given_string = given_string[0]+a[1:]
print(given_string)


# Q2. Write a Python program to get the single string from the two given 
# strings, and separated by the space and swap the first two characters of 
# each string?

# In[16]:


str1 = 'abc'
str2 = 'xyz'
a = str1[:2]
b = str2[:2]
a1 = b+str1[2]
b1 = a+str2[2]
a1+" "+b1


# In[17]:


Samplestring = 'abcing'
if len(Samplestring) <= 3:
    Samplestring = Samplestring+'ing'
    print(Samplestring)
else:
    if ('ing' in Samplestring)== True:
        Samplestring=Samplestring+'ly'
        print(Samplestring)
               
    


# Q4. Write the Python program to find the first appearance of the 
# substring 'not' and 'poor' from the given string, if 'not' follows the 'poor', 
# replace the whole 'not'...' poor' substring with 'good'.Return the resulting 
# string.

# In[18]:


def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')
    print(snot)
    print(spoor)
    if spoor > snot and snot>0 and spoor>0:
        str1 = str1.replace(str1[snot:(spoor+4)], 'good')
        return str1
    else:
        return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))


# Q5. Write the Python program to remove the characters which have odd 
# index values of a given string.

# In[19]:


str = 'sirisathya'
str1=''
for i in range(len(str)):
    if i%2 == 0:
        str1 = str1+str[i]
        
print(str1)        


# Q6. Write the Python function to get a string made of 4 copies of the last 
# two characters of the specified string (length must be at least 2).

# In[20]:


str = 'Exercises'
str1=str[(len(str)-2):]
str2=''
for i in range(4):
    str2= str2+str1
    
print(str2)    


# Q7. Write the python function to get a string made of its first three 
# characters of a specified string. If the length of the string is less than 3 
# then return the original string.

# In[21]:


str = 'python'
def str3(str):
    if len(str)> 3:
        print(str[:3])
    else:
        print(str)
        
str3(str)        


# Q8. Write the python program to print the following floating numbers up
# to 2 decimal places?

# In[22]:


num = 12.3345
num = round(num,2)
print(num)


# Q9. Write the Python program to format a number with a percentage?

# In[23]:


num = 0.90
print("Formatted Number with percentage: "+"{:.2%}".format(num));
num = (num%100)*100
print(num)


# Q10. Write the Python program to count occurrences of a substring in a 
# String?

# In[24]:


str1 = 'The quick brown fox jumps over the lazy dog fox.'
print()
print(str1.count("fox"))
print()


# Q11. Write the Python program to count repeated characters in a string.

# Q12. Write the Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder

# In[25]:


area = 1256.66
volume = 1254.725
decimals = 2
print("The area of the rectangle is {0:.{1}f}cm\u00b2".format(area, decimals))
decimals = 3
print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals))


# Q15. Write the Python program to find the minimum window in the given
# string, which will contains all the characters of another given 
# strings?

# In[ ]:


import collections
def min_window(str1, str2):
    result_char, missing_char = collections.Counter(str2), len(str2)
    i = p = q = 0
    for j, c in enumerate(str1, 1):
        missing_char -= result_char[c] > 0
        result_char[c] -= 1
        if not missing_char:
            while i < q and result_char[str1[i]] < 0:
                result_char[str1[i]] += 1
                i += 1
            if not q or j - i <= q - p:
                p, q = i, j
    return str1[p:q]
           
str1 = "PRWSOERIUSFK"
str2 = "OSU"
print("Original Strings:\n",str1,"\n",str2)
print("Minimum window:")
print(min_window(str1,str2))


# In[ ]:


Q16. Write the Python program to find smallest window that contains all 
get_ipython().set_next_input('characters of the given string');get_ipython().run_line_magic('pinfo', 'string')


# In[1]:


# Python3 program to find the smallest 
# window containing 
# all characters of a pattern 

from collections import defaultdict 

MAX_CHARS = 256

# Function to find smallest window 
# containing 
# all distinct characters 


def findSubString(str): 
	n = len(str) 
	
	# Count all distinct characters. 
	dist_count = len(set([x for x in str])) 

	# Now follow the algorithm discussed in below 
	# post. We basically maintain a window of characters 
	# that contains all characters of given string. 
	# https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/ 

	count, start, start_index, min_len = 0, 0, -1, 9999999999
	curr_count = defaultdict(lambda: 0) 
	for j in range(n): 
		curr_count[str[j]] += 1
		# If any distinct character matched, 
		# then increment count 

		if curr_count[str[j]] == 1: 
			count += 1

		# Try to minimize the window i.e., check if 
		# any character is occurring more no. of times 
		# than its occurrence in pattern, if yes 
		# then remove it from starting and also remove 
		# the useless characters. 

		if count == dist_count: 
			while curr_count[str[start]] > 1: 
				if curr_count[str[start]] > 1: 
					curr_count[str[start]] -= 1
				start += 1

			# Update window size 
			len_window = j - start + 1
			if min_len > len_window: 
				min_len = len_window 
				start_index = start 

	# Return substring starting from start_index 
	# and length min_len """ 
	return str[start_index: start_index + min_len] 
	
# Driver code 
if __name__=='__main__': 
	print("Smallest window containing all distinct characters is {}"
		.format(findSubString("aabcbcdbca"))) 


# Q17. Write the Python program to count number of substrings from a 
# given string of lowercase alphabets with exactly k distinct (given) 
# characters?

# In[2]:


def count_k_dist(str1, k): 
	str_len = len(str1) 
	
	result = 0

	ctr = [0] * 27

	for i in range(0, str_len): 
		dist_ctr = 0

		ctr = [0] * 27

		for j in range(i, str_len): 
			
			if(ctr[ord(str1[j]) - 97] == 0): 
				dist_ctr += 1

			ctr[ord(str1[j]) - 97] += 1

			if(dist_ctr == k): 
				result += 1
			if(dist_ctr > k): 
				break

	return result 

str1 = input("Input a string (lowercase alphabets):")
k = int(input("Input k: "))
print("Number of substrings with exactly", k, "distinct characters : ", end = "") 
print(count_k_dist(str1, k))


# Q18. Write the Python program to count number of non-empty 
# substrings of the given string?

# In[3]:


def number_of_substrings(str): 
	str_len = len(str); 
	return int(str_len * (str_len + 1) / 2); 

str1 = input("Input a string: ")
print("Number of substrings:") 
print(number_of_substrings(str1))


# Q19. Write the Python program to count number of substrings with same 
# first and last characters of the given string?

# In[8]:



# Python program to count all substrings with same 
# first and last characters. 

# Returns true if first and last characters 
# of s are same. 
def checkEquality(s): 
    return (ord(s[0]) == ord(s[len(s) - 1])) 

def countSubstringWithEqualEnds(s): 
    result = 0 
    n = len(s) 

# Starting poof substring 
    for i in range(n): 

# Length of substring 
       for j in range(1,n-i+1): 
            if (checkEquality(s[i:i+j])):
                result+=1 

    return result 

# Driver code 
s = "abcab" 
print(countSubstringWithEqualEnds(s)) 


# Q20. Write the Python program to count the number of strings where the 
# string length is 2 or more, and first and last character are same 
# from a given list of strings.

# In[9]:


def match_words(words):
    ctr = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))


# Q21. Write the Python program to get a list, sorted in increasing order by 
# the last element in each tuple from the given list of non-empty 
# tuples?

# In[10]:


def last(n): return n[-1]

def sort_list_last(tuples):
    return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# Q22. Write the Python program to remove duplicates from a list?
# 

# In[11]:


a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)


# In[ ]:


Q23. Write the Python program to find the list of words that are longer 
get_ipython().set_next_input('than n from a given list of words');get_ipython().run_line_magic('pinfo', 'words')


# In[12]:


def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words(3, "The quick brown fox jumps over the lazy dog"))


# Q25. Write the Python program to generate all permutations of a list in 
# Python?

# In[13]:


import itertools
print(list(itertools.permutations([1,2,3])))


# Q26. Write the Python program to convert a pair of values into a sorted 
# unique array?

# In[14]:


L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]
print("Original List: ", L)
print("Sorted Unique Data:",sorted(set().union(*L)))


# Q27. Write the Python class to convert an integer to a roman numeral?

# In[15]:


class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


print(py_solution().int_to_Roman(1))
print(py_solution().int_to_Roman(4000))


# Q28 Write the Python class to convert a Roman numeral to an integer?

# In[16]:


class py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

print(py_solution().roman_to_int('MMMCMLXXXVI'))
print(py_solution().roman_to_int('MMMM'))
print(py_solution().roman_to_int('C'))


# Q29. Write the Python class to find the validity of the string of the
# parentheses, '(', ')', '{', '}', '[' and '] and the brackets must be closed
# in the correct order, example - "()" and "()[]{}" are valid but "[)",
# "({[)]" and "{{{" are invalid.

# In[17]:


class py_solution:
    def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))


# Q30. Write the Python class to get all possible unique subsets from a set 
# of distinct integers?

# In[18]:


class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print(py_solution().sub_sets([4,5,6]))


# Q31. Write the Python class to find a pair of elements (indices of the two 
# numbers) from a given array whose sum equals the specific target 
# number?

# In[19]:


class py_solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i )
            lookup[num] = i
print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),50))


# Q32. Write the Python class tofind the three elements that sum to zero 
# from the set of n real numbers?

# In[20]:


class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))


# Q33. Write the Python class to implement pow(x, n)?

# In[21]:


class py_solution:
    def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print(py_solution().pow(2, -3));
print(py_solution().pow(3, 5));
print(py_solution().pow(100, 0));


# Q34. Write the Python class which has two methods get_String and 
# print_String. get_String accept the string from the user and print_String print the string in upper case.

# In[22]:


class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()


# Q35. Write the Python class named Rectangle constructed by a length 
# and width and the method which will compute the area of the
# rectangle?

# In[23]:


class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())


# Q36. Write the Python class named Circle constructed by the radius 
# and two methods which will compute the area and perimeter of 
# the circle?

# In[24]:


class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())


# Q37. Write the Python program to get the class name of an instance in 
# Python?

# In[25]:


import itertools
x = itertools.cycle('ABCD')
print(type(x).__name__)


# Q38. Write the Python program to count the number of students of 
# individual class?

# In[26]:


from collections import Counter
classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)
students = Counter(class_name for class_name, no_students in classes)
print(students)


# Q39. Write the Python program to create an instance of an OrderedDict using the given dictionary and sort dictionary during the 
# creation and print members of the dictionary in reverse order?

# In[27]:


from collections import OrderedDict
dict = {'Afghanistan': 93, 'Albania': 355, 'Algeria': 213, 'Andorra': 376, 'Angola': 244}
new_dict = OrderedDict(dict.items())
for key in new_dict:
    print (key, new_dict[key])

print("\nIn reverse order:")
for key in reversed(new_dict):
    print (key, new_dict[key])


# Q40. Write the Python program to compare two unordered lists (not 
# sets)?

# In[29]:


def compare(s, t):
        t = list(t)   # make a mutable copy
        try:
            for elem in s:
                t.remove(elem)
        except ValueError:
            return False
        return not t


# Q41. Write the Python program to get an array buffer information?

# In[30]:


from array import array
a = array("I", (12,25))
print("Array buffer start address in memory and number of elements.")
print(a.buffer_info())


# Q42. Write the Python program to convert an array to an array of 
# machine values and return the bytes representation?

# In[34]:


from array import *
print("Bytes to String: ")
x = array('b', [118, 56, 114, 101,  115, 111, 117, 114, 99, 101])
s = x.tobytes()
print(s)


# Q43. Write the Python program to read a string and interpreting the 
# string as an array of machine values?

# In[35]:


from array import array
import binascii
array1 = array('i', [7, 8, 9, 10])
print('array1:', array1)
as_bytes = array1.tobytes()
print('Bytes:', binascii.hexlify(as_bytes))
array2 = array('i')
array2.frombytes(as_bytes)
print('array2:', array2)


# Q44. Write the Python program to push three items into the heap and 
# return the smallest item from the heap. Also, return and pop the 
# smallest item from the heap?

# In[36]:


import heapq
heap = []
heapq.heappush(heap, ('V', 3))
heapq.heappush(heap, ('V', 2))
heapq.heappush(heap, ('V', 1))
print("Items in the heap:")
for a in heap:
	print(a)
print("----------------------")
print("Using heappushpop push item on the heap and return the smallest item.")
heapq.heappushpop(heap, ('V', 6))
for a in heap:
	print(a)
	


# Q45. Write the Python program to locate the left insertion point for a 
# specified value in sorted order?

# In[37]:


import bisect
def index(a, x):
    i = bisect.bisect_left(a, x)
    return i
    
a = [1,2,4,5]
print(index(a, 6))
print(index(a, 3))


# Q46. Write the Python program to create the FIFO queue?

# In[1]:


import queue
q = queue.Queue()
#insert items at the end of the queue 
for x in range(4):
    q.put(str(x))
#remove items from the head of the queue 
while not q.empty():
    print(q.get(), end=" ")
print("\n")


# Q47. Write the Python program to calculate the harmonic sum of n-1.
#  Note: The harmonic sum is the sum of reciprocals of the positive 
# Integers?

# In[2]:


def harmonic_sum(n):
  if n < 2:
    return 1
  else:
    return 1 / n + (harmonic_sum(n - 1))
    
print(harmonic_sum(7))
print(harmonic_sum(4))


# Q48. Write the NumPy program to create a 2d array with 6 on the border 
# and 0 inside?

# In[3]:


import numpy as np
x = np.ones((5,5))
print("Original array:")
print(x)
print("1 on the border and 0 inside in the array")
x[1:-1,1:-1] = 0
print(x)


# Q49. Write the NumPy program to create a 8x8 matrix and fill it with the
# checkerboard pattern?

# In[4]:


import numpy as np
x = np.ones((3,3))
print("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)


# Q50. Write the NumPy program to create an empty and a full array.

# Q51. Write the NumPy program to convert the values of Centigrade
# degrees into the Fahrenheit degrees and the centigrade values are 
# stored in the NumPy array.

# In[6]:


import numpy as np
fvalues = [0, 12, 45.21, 34, 99.91]
F = np.array(fvalues)
print("Values in Fahrenheit degrees:")
print(F)
print("Values in  Centigrade degrees:") 
print(5*F/9 - 5*32/9)


# Q52. Write the NumPy program to find the real and imaginary parts of an 
# array of complex numbers?

# In[7]:


import numpy as np
x = np.sqrt([1+0j])
y = np.sqrt([0+1j])
print("Original array:x ",x)
print("Original array:y ",y)
print("Real part of the array:")
print(x.real)
print(y.real)
print("Imaginary part of the array:")
print(x.imag)
print(y.imag)


# In[ ]:


Q53. Write the NumPy program to test whether each element of a 1-D 
get_ipython().set_next_input('array is also present in the second array');get_ipython().run_line_magic('pinfo', 'array')


# In[8]:


import numpy as np
array1 = np.array([0, 10, 20, 40, 60])
print("Array1: ",array1)
array2 = [0, 40]
print("Array2: ",array2)
print("Compare each element of array1 and array2")
print(np.in1d(array1, array2))


# In[ ]:


Q54. Write the NumPy program to find common values between two 
get_ipython().run_line_magic('pinfo', 'arrays')


# In[9]:


import numpy as np
array1 = np.array([0, 10, 20, 40, 60])
print("Array1: ",array1)
array2 = [10, 30, 40]
print("Array2: ",array2)
print("Common values between two arrays:")
print(np.intersect1d(array1, array2))


# Q55. Write the NumPy program to get the unique elements of an array?

# In[10]:


import numpy as np
x = np.array([10, 10, 20, 20, 30, 30])
print("Original array:")
print(x)
print("Unique elements of the above array:")
print(np.unique(x))
x = np.array([[1, 1], [2, 3]])
print("Original array:")
print(x)
print("Unique elements of the above array:")
print(np.unique(x))


# Q56. Write the NumPy program to find the set exclusive-or of two arrays. 
# Set exclusive-or will return the sorted, unique values that are in 
# only one (not both) of the input arrays?

# In[11]:


import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",array1)
array2 = [10, 30, 40, 50, 70]
print("Array2: ",array2)
print("Unique values that are in only one (not both) of the input arrays:")
print(np.setxor1d(array1, array2))


# Q57. Write the NumPy program to test if all elements in an array 
# evaluate to True ?

# In[12]:


import numpy as np
print(np.all([[True,False],[True,True]]))
print(np.all([[True,True],[True,True]]))
print(np.all([10, 20, 0, -50]))
print(np.all([10, 20, -50]))


# Q58 Write the NumPy program to test whether any array element along 
# the given axis evaluates to True?

# In[13]:


import numpy as np
print(np.any([[False,False],[False,False]]))
print(np.any([[True,True],[True,True]]))
print(np.any([10, 20, 0, -50]))
print(np.any([10, 20, -50]))


# Q59. Write the NumPy program to construct an array by repeating?

# In[14]:


import numpy as np
a = [1, 2, 3, 4]
print("Original array")
print(a)
print("Repeating 2 times")
x = np.tile(a, 2)
print(x)
print("Repeating 3 times")
x = np.tile(a, 3)
print(x)


# Q51. Write the NumPy program to convert the values of Centigrade
# degrees into the Fahrenheit degrees and the centigrade values are 
# stored in the NumPy array.

# In[5]:


import numpy as np
fvalues = [0, 12, 45.21, 34, 99.91]
F = np.array(fvalues)
print("Values in Fahrenheit degrees:")
print(F)
print("Values in  Centigrade degrees:") 
print(5*F/9 - 5*32/9)


# Q60. Write the NumPy program to find the indices of the maximum and 
# minimum values with the given axis of an array?

# In[1]:


import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])
print("Original array: ",x)
print("Maximum Values: ",np.argmax(x))
print("Minimum Values: ",np.argmin(x))


# In[ ]:


get_ipython().set_next_input('Q61. Write the NumPy program compare two arrays using numpy');get_ipython().run_line_magic('pinfo', 'numpy')


# In[2]:


import numpy as np
a = np.array([1, 2])
b = np.array([4, 5])
print("Array a: ",a)
print("Array b: ",b)
print("a > b")
print(np.greater(a, b))
print("a >= b")
print(np.greater_equal(a, b))
print("a < b")
print(np.less(a, b))
print("a <= b")
print(np.less_equal(a, b))


# Q62. Write the NumPy program to sort an along the first, last axis of an 
# array?

# In[3]:


import numpy as np
a = np.array([[4, 6],[2, 1]])
print("Original array: ")
print(a)
print("Sort along the first axis: ")
x = np.sort(a, axis=0)
print(x)
print("Sort along the last axis: ")
y = np.sort(x, axis=1)
print(y)


# Q63. Write the NumPy program to sort pairs of first name and last name 
# return their indices (first by last name, then by first name).

# In[4]:


import numpy as np
first_names =    ('Margery', 'Betsey', 'Shelley', 'Lanell', 'Genesis')
last_names = ('Woolum', 'Battle', 'Plotner', 'Brien', 'Stahl')
x = np.lexsort((first_names, last_names))
print(x)


# In[ ]:


Q64. Write the NumPy program to get the values and indices of the 
get_ipython().set_next_input('elements that are bigger than 10 in the given array');get_ipython().run_line_magic('pinfo', 'array')


# In[5]:


import numpy as np
x = np.array([[0, 10, 20], [20, 30, 40]])
print("Original array: ")
print(x)
print("Values bigger than 10 =", x[x>10])
print("Their indices are ", np.nonzero(x > 10))


# In[ ]:


Q65. Write the NumPy program to find the memory size of a NumPy 
get_ipython().run_line_magic('pinfo', 'array')


# In[6]:


import numpy as np
n = np.zeros((4,4))
print("%d bytes" % (n.size * n.itemsize))


# In[ ]:


Q66. Write the NumPy program to create an array of ones and an array 
get_ipython().set_next_input('of zeros');get_ipython().run_line_magic('pinfo', 'zeros')


# In[7]:


import numpy as np
print("Create an array of zeros")
x = np.zeros((1,2))
print("Default type is float")
print(x)
print("Type changes to int")
x = np.zeros((1,2), dtype = np.int)
print(x)
print("Create an array of ones")
y= np.ones((1,2)) 
print("Default type is float")
print(y)
print("Type changes to int")
y = np.ones((1,2), dtype = np.int)
print(y)


# In[ ]:


get_ipython().set_next_input('Q67. Write the NumPy program to change the dimension of an array');get_ipython().run_line_magic('pinfo', 'array')


# In[8]:


import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])
print("6 rows and 0 columns")
print(x.shape)

y = np.array([[1, 2, 3],[4, 5, 6],[7,8,9]])
print("(3, 3) -> 3 rows and 3 columns ")
print(y)

x = np.array([1,2,3,4,5,6,7,8,9])
print("Change array shape to (3, 3) -> 3 rows and 3 columns ")
x.shape = (3, 3)
print(x)


# In[ ]:


Q68. Write the NumPy program to create a new shape to an array 
without changing its data ?


# In[9]:


import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])
y = np.reshape(x,(3,2))
print("Reshape 3x2:")
print(y)
z = np.reshape(x,(2,3))
print("Reshape 2x3:")
print(z)


# In[ ]:


Q69. Write the NumPy program to create a new array of 3*5, filled with 
2?


# In[1]:


import numpy as np
#using no.full
x = np.full((3, 5), 2, dtype=np.uint)
print(x)
#using no.ones
y = np.ones([3, 5], dtype=np.uint) *2
print(y)


# In[ ]:


Q70. Write the NumPy program to create a 3-D array with ones on a 
get_ipython().set_next_input('diagonal and zeros elsewhere');get_ipython().run_line_magic('pinfo', 'elsewhere')


# In[ ]:


import numpy as np
x = np.eye(3)
print(x)


# In[ ]:


Q71. Write the NumPy program to split an array of 14 elements into the 
3 arrays and each of which has 2, 4, and 8 elements in original 
get_ipython().run_line_magic('pinfo', 'order')


# In[2]:


import numpy as np
x = np.arange(1, 15)
print("Original array:",x)
print("After spliting:")
print(np.split(x, [2, 6]))


# In[ ]:


Q72. Write the NumPy program to split of an array of shape 4x4 it into 
two arrays along the second axis ?


# In[3]:


import numpy as np
x = np.arange(16).reshape((4, 4))
print("Original array:",x)
print("After splitting horizontally:")
print(np.hsplit(x, [2, 6]))


# In[ ]:


Q73. Write the NumPy program to create a 5x5 matrix with row values 
ranging from 0 to 4?


# In[4]:


import numpy as np
x = np.zeros((5,5))
print("Original array:")
print(x)
print("Row values ranging from 0 to 4.")
x += np.arange(5)
print(x)


# In[ ]:


Q74. Write the NumPy program to create an array of zeros and three 
column types (integer, float, character)?


# In[5]:


import numpy as np
x = np.zeros((3,), dtype=('i4,f4,a40'))
new_data = [(1, 2., "Albert Einstein"), (2, 2., "Edmond Halley"), (3, 3., "Gertrude B. Elion")]
x[:] = new_data
print(x)


# In[ ]:


Q75. Write the NumPy program to remove the negative values in the
numpy array with 0?


# In[6]:


import numpy as np
x = np.array([-1, -4, 0, 2, 3, 4, 5, -6])
print("Original array:")
print(x)
print("Replace the negative values of the said array with 0:")
x[x < 0] = 0
print(x)


# In[ ]:


Q76. Write the NumPy program to compute the histogram of a set of 
get_ipython().run_line_magic('pinfo', 'data')


# In[7]:


import numpy as np    
import matplotlib.pyplot as plt
plt.hist([1, 2, 1], bins=[0, 1, 2, 3, 5])
plt.show()


# In[ ]:


Q77. Write the NumPy program to compute the line graph of a set of 
get_ipython().run_line_magic('pinfo', 'data')


# In[8]:


import numpy as np    
import matplotlib.pyplot as plt
arr = np.random.randint(1, 50, 10)
y, x = np.histogram(arr, bins=np.arange(51))
fig, ax = plt.subplots()
ax.plot(x[:-1], y)
fig.show()


# In[ ]:


Q78. Write the NumPy program to extracts all the elements from second 
get_ipython().set_next_input('row from given (4x4) array');get_ipython().run_line_magic('pinfo', 'array')


# In[9]:


import numpy as np
arra_data = np.arange(0,16).reshape((4, 4))
print("Original array:")
print(arra_data)
print("\nExtracted data: Second row")
print(arra_data[1,:])


# In[ ]:


Q79. Write the NumPy program to extract first element of the second
row and fourth element of fourth row from a given (4x4) array? 


# In[10]:


import numpy as np
arra_data = np.arange(0,16).reshape((4, 4))
print("Original array:")
print(arra_data)
print("\nExtracted data: First element of the second row and fourth element of fourth row  ")
print(arra_data[[1,3], [0,3]])


# In[ ]:


Q80. Write the NumPy program to add two arrays A and B of sizes (3,3) 
and (,3)?


# In[11]:


import numpy as np
A = np.ones((3,3))
B = np.arange(3)
print("Original array:")
print("Array-1")
print(A)
print("Array-2")
print(B)
print("A + B:")
new_array = A + B
print(new_array)


# In[ ]:


Q81. Write the NumPy program to copy data from a given array to 
get_ipython().set_next_input('another array');get_ipython().run_line_magic('pinfo', 'array')


# In[12]:


import numpy as np
x = np.array([24, 27, 30, 29, 18, 14])
print("Original array:")
print(x)
y = np.empty_like (x)
y[:] = x
print("\nCopy of the said array:")
print(y)


# In[ ]:


Q82. Write the NumPy program to calculate the sum of all columns of 
get_ipython().set_next_input('the 2D numpy array');get_ipython().run_line_magic('pinfo', 'array')


# In[13]:


import numpy as np
num = np.arange(36)
arr1 = np.reshape(num, [4, 9])
print("Original array:")
print(arr1)
result  = arr1.sum(axis=0)
print("\nSum of all columns:")
print(result)


# In[ ]:


Q83. Write the NumPy program to calculate averages without NaNs 
get_ipython().set_next_input('along the given array');get_ipython().run_line_magic('pinfo', 'array')


# In[14]:


import numpy as np
arr1 = np.array([[10, 20 ,30], [40, 50, np.nan], [np.nan, 6, np.nan], [np.nan, np.nan, np.nan]])
print("Original array:")
print(arr1)
temp = np.ma.masked_array(arr1,np.isnan(arr1))
result = np.mean(temp, axis=1)
print("Averages without NaNs along the said array:")
print(result.filled(np.nan))


# In[ ]:


Q84. Create two arrays of six elements. Write the NumPy program to 
count the number of instances of a value occurring in one array on 
the condition of another array.


# In[15]:


import numpy as np
x = np.array([10,-10,10,-10,-10,10])
y = np.array([.85,.45,.9,.8,.12,.6])
print("Original arrays:")
print(x)
print(y)
result = np.sum((x == 10) & (y > .5))
print("\nNumber of instances of a value occurring in one aray on the condition of another array:")
print(result)


# In[ ]:


Q87. Write the NumPy program to multiply the matrix by another matrix 
of complex numbers and create a new matrix of complex 
get_ipython().run_line_magic('pinfo', 'numbers')


# In[16]:


import numpy as np
x = np.array([1+2j,3+4j])
print("First array:")
print(x)
y = np.array([5+6j,7+8j])
print("Second array:")
print(y)
z = np.vdot(x, y)
print("Product of above two arrays:")
print(z)


# In[ ]:


Q88. Write a NumPy program to generate the matrix product of two 
get_ipython().run_line_magic('pinfo', 'Arrays')


# In[17]:


import numpy as np
x = [[1, 0], [1, 1]]
y = [[3, 1], [2, 2]]
print("Matrices and vectors.")
print("x:")
print(x)
print("y:")
print(y)
print("Matrix product of above two arrays:")
print(np.matmul(x, y))


# In[ ]:


Q89. Write the NumPy program to find roots of the following 
get_ipython().run_line_magic('pinfo', 'Polynomials')


# In[18]:


import numpy as np
print("Roots of the first polynomial:")
print(np.roots([1, -2, 1]))
print("Roots of the second polynomial:")
print(np.roots([1, -12, 10, 7, -10]))


# In[ ]:


Q90. Write the NumPy program to calculate inverse of sine, cosine,
and inverse tangent for all elements in a given array? 


# In[19]:


import numpy as np
x = np.array([-1., 0, 1.])
print("Inverse sine:", np.arcsin(x))
print("Inverse cosine:", np.arccos(x))
print("Inverse tangent:", np.arctan(x))


# In[ ]:


Q91. Write the NumPy program to calculate the difference between in
get_ipython().set_next_input('neighbouring elements, element-wise of a given array');get_ipython().run_line_magic('pinfo', 'array')


# In[20]:


import numpy as np
a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test a given array element-wise for finiteness :")
print(np.isfinite(a))


# In[ ]:


Q92. Write the Python program to find the maximum and the minimum 
get_ipython().set_next_input('value of a given flattened array');get_ipython().run_line_magic('pinfo', 'array')


# In[21]:


import numpy as np
a = np.arange(4).reshape((2,2))
print("Original flattened array:")
print(a)
print("Maximum value of the above flattened array:")
print(np.amax(a))
print("Minimum value of the above flattened array:")
print(np.amin(a))


# In[ ]:


Q93. Write the NumPy program to calculate the difference between in 
the maximum and the minimum values of a given array along the second axis ?


# In[22]:


import numpy as np
x = np.arange(12).reshape((2, 6))
print("\nOriginal array:")
print(x)
r1 = np.ptp(x, 1)
r2 = np.amax(x, 1) - np.amin(x, 1)
assert np.allclose(r1, r2)
print("\nDifference between the maximum and the minimum values of the said array:")
print(r1)


# In[ ]:


Q94. Write the NumPy program to compute the weighted of the given 
array ?


# In[23]:


import numpy as np
x = np.arange(5)
print("\nOriginal array:")
print(x)
weights = np.arange(1, 6)
r1 = np.average(x, weights=weights)
r2 = (x*(weights/weights.sum())).sum()
assert np.allclose(r1, r2)
print("\nWeighted average of the said array:")
print(r1)


# In[ ]:


Q95. Write the NumPy program to compute the mean, standard 
deviation, and the variance of a given array along the second 
get_ipython().run_line_magic('pinfo', 'axis')


# In[24]:


import numpy as np
x = np.arange(6)
print("\nOriginal array:")
print(x)
r1 = np.mean(x)
r2 = np.average(x)
assert np.allclose(r1, r2)
print("\nMean: ", r1)
r1 = np.std(x)
r2 = np.sqrt(np.mean((x - np.mean(x)) ** 2 ))
assert np.allclose(r1, r2)
print("\nstd: ", 1)
r1= np.var(x)
r2 = np.mean((x - np.mean(x)) ** 2 )
assert np.allclose(r1, r2)
print("\nvariance: ", r1)


# In[ ]:


Q96. Write the Numpy program to compute the covariance matrix of the 
get_ipython().set_next_input('two given arrays');get_ipython().run_line_magic('pinfo', 'arrays')


# In[25]:


import numpy as np
x = np.array([0, 1, 2])
y = np.array([2, 1, 0])
print("\nOriginal array1:")
print(x)
print("\nOriginal array1:")
print(y)
print("\nCovariance matrix of the said arrays:\n",np.cov(x, y))


# In[ ]:


Q97. Write a NumPy program to compute the cross-correlation of two 
given arrays ?


# In[26]:


import numpy as np
x = np.array([0, 1, 3])
y = np.array([2, 4, 5])
print("\nOriginal array1:")
print(x)
print("\nOriginal array1:")
print(y)
print("\nCross-correlation of the said arrays:\n",np.cov(x, y))


# In[ ]:


Q98. Write the NumPy program to compute Pearson product-moment 
get_ipython().set_next_input('correlation coefficients of two given arrays');get_ipython().run_line_magic('pinfo', 'arrays')


# In[27]:


import numpy as np
x = np.array([0, 1, 3])
y = np.array([2, 4, 5])
print("\nOriginal array1:")
print(x)
print("\nOriginal array1:")
print(y)
print("\nPearson product-moment correlation coefficients of the said arrays:\n",np.corrcoef(x, y))


# In[ ]:


Q99. Write the python program to count the number of occurrences of 
get_ipython().set_next_input('each value in a given array of non-negative integers');get_ipython().run_line_magic('pinfo', 'integers')


# In[28]:


import numpy as np
array1 = [0, 1, 6, 1, 4, 1, 2, 2, 7] 
print("Original array:")
print(array1)
print("Number of occurrences of each value in array: ")
print(np.bincount(array1))


# In[ ]:


Q100. Write a Numpy program to compute the histogram of nums 
get_ipython().set_next_input('against the bins');get_ipython().run_line_magic('pinfo', 'bins')


# In[29]:


import numpy as np
import matplotlib.pyplot as plt
nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])
print("nums: ",nums)
print("bins: ",bins)
print("Result:", np.histogram(nums, bins))
plt.hist(nums, bins=bins)
plt.show()


# In[ ]:


Q101. Write the Python program to add, subtract, multiply and divide 
two pandas series ?


# In[30]:


import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2
print("Add two Series:")
print(ds)
print("Subtract two Series:")
ds = ds1 - ds2
print(ds)
print("Multiply two Series:")
ds = ds1 * ds2
print(ds)
print("Divide Series1 by Series2:")
ds = ds1 / ds2
print(ds)


# In[ ]:


Q102. Write a Python program to convert a dictionary to the Pandas 
get_ipython().run_line_magic('pinfo', 'Series')


# In[31]:


# import the pandas lib as pd 
import pandas as pd 

# create a dictionary 
dictionary = {'A' : 10, 'B' : 20, 'C' : 30} 

# create a series 
series = pd.Series(dictionary) 

print(series) 


# In[ ]:


Q103. Write a python program to change the data type of given a 
get_ipython().set_next_input('column or a Series');get_ipython().run_line_magic('pinfo', 'Series')


# In[32]:


import pandas as pd
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s1)
print("Change the said data type to numeric:")
s2 = pd.to_numeric(s1, errors='coerce')
print(s2)


# In[ ]:


Q104. Write the python pandas program to convert the first column of a 
get_ipython().set_next_input('DataFrame as a Series');get_ipython().run_line_magic('pinfo', 'Series')


# In[33]:


import pandas as pd
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
s1 = df.ix[:,0]
print("\n1st column as a Series:")
print(s1)
print(type(s1))


# In[ ]:


Q105. Write a pandas program to create the mean and standard 
get_ipython().set_next_input('deviation of the data of a given Series');get_ipython().run_line_magic('pinfo', 'Series')


# In[34]:


import pandas as pd
s = pd.Series(data = [1,2,3,4,5,6,7,8,9,5,3])
print("Original Data Series:")
print(s)
print("Mean of the said Data Series:")
print(s.mean())
print("Standard deviation of the said Data Series:")
print(s.std())


# In[ ]:


Q106. Write a pandas program to get powers of an array values 
get_ipython().set_next_input('element-wise');get_ipython().run_line_magic('pinfo', 'wise')


# In[35]:


import pandas as pd
df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print(df)


# In[ ]:


Q107. Write the pandas program to get the first 3 rows of a given 
get_ipython().run_line_magic('pinfo', 'DataFrame')


# In[36]:


import pandas as pd
import numpy as np

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("First three rows of the data frame:")
print(df.iloc[:3])


# In[ ]:


Q108: Write the pandas program to select the specified columns and
 get_ipython().set_next_input(' the rows from a given data frame');get_ipython().run_line_magic('pinfo', 'frame')


# In[37]:


import pandas as pd
import numpy as np

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("Select specific columns and rows:")
print(df.iloc[[1, 3, 5, 6], [1, 3]])


# In[ ]:


Q109. Write the pandas program to calculate mean score for each 
get_ipython().set_next_input('different student in DataFrame');get_ipython().run_line_magic('pinfo', 'DataFrame')


# In[38]:


import pandas as pd
import numpy as np
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("\nMean score for each different student in data frame:")
print(df['score'].mean())


# In[ ]:


Q108: Write the pandas program to select the specified columns and
 get_ipython().set_next_input(' the rows from a given data frame');get_ipython().run_line_magic('pinfo', 'frame')


# In[39]:


import pandas as pd
import numpy as np

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("Select specific columns and rows:")
print(df.iloc[[1, 3, 5, 6], [1, 3]])


# In[ ]:


Q109. Write the pandas program to calculate mean score for each 
get_ipython().set_next_input('different student in DataFrame');get_ipython().run_line_magic('pinfo', 'DataFrame')


# In[40]:


import pandas as pd
import numpy as np
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("\nMean score for each different student in data frame:")
print(df['score'].mean())


# In[ ]:


Q110. Write the Pandas program to rename columns of a given 
DataFrame ?


# In[41]:


# Import pandas package 
import pandas as pd 

# Define a dictionary containing ICC rankings 
rankings = {'test': ['India', 'South Africa', 'England', 
							'New Zealand', 'Australia'], 
			'odi': ['England', 'India', 'New Zealand', 
							'South Africa', 'Pakistan'], 
			't20': ['Pakistan', 'India', 'Australia', 
							'England', 'New Zealand']} 

# Convert the dictionary into DataFrame 
rankings_pd = pd.DataFrame(rankings) 

# Before renaming the columns 
print(rankings_pd) 

rankings_pd.rename(columns = {'test':'TEST'}, inplace = True) 

# After renaming the columns 
print("\nAfter modifying first column:\n", rankings_pd.columns) 


# In[ ]:


Q111. Write a pandas program to count city-wise number of people from 
a given of data set (city, name of the person)?


# In[42]:


import pandas as pd
df1 = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})
g1 = df1.groupby(["city"]).size().reset_index(name='Number of people')
print(g1)


# In[ ]:


Q112. Write a pandas program to widen output display to see more 
get_ipython().run_line_magic('pinfo', 'columns')


# In[ ]:


Q113. Write a pandas program to convert the data frame column type 
get_ipython().set_next_input('from string to DateTime');get_ipython().run_line_magic('pinfo', 'DateTime')


# In[43]:


# importing pandas as pd 
import pandas as pd 

# Creating the dataframe 
df = pd.DataFrame({'Date':['11/8/2011', '04/23/2008', '10/2/2019'], 
				'Event':['Music', 'Poetry', 'Theatre'], 
				'Cost':[10000, 5000, 15000]}) 

# Print the dataframe 
print(df) 

# Now we will check the data type 
# of the 'Date' column 
df.info() 


# In[ ]:


Q114. Write a pandas program to append the data to an empty 
get_ipython().run_line_magic('pinfo', 'DataFrame')


# In[44]:


import pandas as pd
import numpy as np
df = pd.DataFrame()
data = pd.DataFrame({"col1": range(3),"col2": range(3)})
print("After appending some data:")
df = df.append(data)
print(df)


# In[ ]:


Q115. Write a pandas program to count the number of columns of a 
get_ipython().run_line_magic('pinfo', 'DataFrame')


# In[45]:


import pandas as pd
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
print("\nNumber of columns:")
print(len(df.columns))


# In[ ]:


Q116. Write a Pandas program to remove the last n rows of a given 
DataFrame ?


# In[1]:


import pandas as pd
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
print("\nAfter removing last 3 rows of the said DataFrame:")
df1 = df.iloc[:3]
print(df1)


# In[ ]:


Q117. Write a Pandas program to import excel data (coalpublic2013.xlsx 
) into a Pandas data frame.


# In[ ]:


import pandas as pd
import numpy as np
df = pd.read_excel('E:\coalpublic2013.xlsx', skiprows = 20)
df


# In[ ]:


Q118. Write a Pandas program to import excel data (coalpublic2013.xlsx 
) into a data frame and find details where "Mine Name" starts with 
"P.


# In[ ]:


import pandas as pd
import numpy as np
df = pd.read_excel('E:\coalpublic2013.xlsx')    
df[df["Mine_Name"].map(lambda x: x.startswith('P'))].head()


# In[ ]:


Q119. Write a Pandas program to import excel data (employee.xlsx )
into a Pandas dataframe and find the list of employees where 
hire_date> 01-01-07.


# In[ ]:


import pandas as pd
import numpy as np
df = pd.read_excel('E:\employee.xlsx')
df[df['hire_date'] >='20070101']


# In[ ]:


Q120. Write a Pandas program to import excel data (employee.xlsx ) 
into a Pandas dataframe and find a list of the employees of a specified 
year


# In[ ]:


import pandas as pd
import numpy as np
df = pd.read_excel('E:\employee.xlsx')
df2 = df.set_index(['hire_date'])
result = df2["2005"]
result


# In[ ]:


Q121. Write a pandas program to import three datasheets from a given 
excel data (coalpublic2013.xlsx ) in to a single dataframe.


# In[ ]:


import pandas as pd
import numpy as np
df1 = pd.read_excel('E:\employee.xlsx',sheet_name=0)
df2 = pd.read_excel('E:\employee.xlsx',sheet_name=1)
df3 = pd.read_excel('E:\employee.xlsx',sheet_name=2)
df = pd.concat([df1, df2, df3])
print(df)


# In[ ]:


Q 122. Write a pandas program to import three datasheets from a given 
excel data (employee.xlsx ) into a single data frame and export the 
result into new Excel file.


# In[ ]:


import pandas as pd
import numpy as np
df1 = pd.read_excel('E:\employee.xlsx',sheet_name=0)
df2 = pd.read_excel('E:\employee.xlsx',sheet_name=1)
df3 = pd.read_excel('E:\employee.xlsx',sheet_name=2)
df = pd.concat([df1, df2, df3])
df.to_excel('e:\output.xlsx', index=False)


# In[ ]:


Q123. Write a pandas program to create the Pivot table with multiple 
indexes from the data set of the titanic.csv.


# In[ ]:


import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
result = pd.pivot_table(df, index = ["sex","age"], aggfunc=np.sum)
print(result)


# In[ ]:


Q124. Write a Pandas program to create the Pivot table and find survival 
get_ipython().set_next_input('rate by gender');get_ipython().run_line_magic('pinfo', 'gender')


# In[ ]:


import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
age = pd.cut(df['age'], [0, 20, 55])
result = df.pivot_table('survived', index=['sex', age], columns='class')
print(result)


# In[ ]:


Q125. Write a pandas program to make partition each of the passengers 
into 4 categories based on their age.


# In[ ]:


Q126. Write a pandas program to create the Pivot table and find survival 
rate by the gender, age of the different categories of various 
classes.


# In[ ]:


import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
age = pd.cut(df['age'], [0, 20, 55])
result = df.pivot_table('survived', index=['sex', age], columns='class')
print(result)


# In[ ]:


Q127. Write a pandas program to create the Pivot table and calculate 
number of women and men were in a particular cabin class.


# In[ ]:


import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
result = df.pivot_table(index=['sex'], columns=['pclass'], values='survived', aggfunc='count')
print(result)


# In[ ]:


Q128. Write a pandas program to create the Pivot table and separate 
the gender according to whether they travelled alone or not to get 
the probability of survival


# In[ ]:


import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
result = df.pivot_table( 'survived' , [ 'sex' , 'alone' ] , 'class' )
print(result)


# In[ ]:


Q129. Write a pandas program to create the Pivot table and find the 
probability of survival by class, gender, solo boarding, and the port 
of embarkation.


# In[ ]:


import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
result = df.pivot_table('survived', ['sex' , 'alone' ], [ 'embark_town', 'class' ])
print(result)


# In[ ]:


Q130. Write a pandas program to get current date, oldest date and 
number of days between Current date and the oldest date of Ufo 
dataset.


# In[ ]:


import pandas as pd
df = pd.read_csv(r'ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
print("Original Dataframe:")
print(df.head())
print("\nCurrent date of Ufo dataset:")
print(df.Date_time.max())
print("\nOldest date of Ufo dataset:")
print(df.Date_time.min())
print("\nNumber of days between Current date and oldest date of Ufo dataset:")
print((df.Date_time.max() - df.Date_time.min()).days)


# In[ ]:


Q131. Write a pandas program to get all sighting days of the 
unidentified flying object (ufo) between 1950-10-10 and 1960-10-
10.


# In[ ]:


import pandas as pd
df = pd.read_csv(r'ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
print("Original Dataframe:")
print(df.head())
print("\nSighting days of the unidentified flying object (ufo) between 1949-10-10 and 1960-10-10:")
selected_period = df[(df['Date_time'] >= '1950-01-01 00:00:00') & (df['Date_time'] <= '1960-12-31 23:59:59')]
print(selected_period)


# In[ ]:


Q132. Write a Pandas program to extract the year, month, day, hour,
minute, second, and weekday from unidentified flying object (UFO) 
reporting date.


# In[ ]:


import pandas as pd
df = pd.read_csv(r'ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
print("Original Dataframe:")
print(df.head())
print("\nYear:")
print(df.Date_time.dt.year.head())
print("\nMonth:")
print(df.Date_time.dt.month.head())
print("\nDay:")
print(df.Date_time.dt.day.head())
print("\nHour:")
print(df.Date_time.dt.hour.head())
print("\nMinute:")
print(df.Date_time.dt.minute.head())
print("\nSecond:")
print(df.Date_time.dt.second.head())
print("\nWeekday:")
print(df.Date_time.dt.weekday_name.head())


# In[ ]:


Q133. Write a pandas program to count year-country wise frequency of
reporting dates of the unidentified flying object(UFO).


# In[ ]:


import pandas as pd
df = pd.read_csv(r'ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
print("Original Dataframe:")
print(df.head())
df['Year'] = df['Date_time'].apply(lambda x: "%d" % (x.year))
result = df.groupby(['Year', 'country']).size()
print("\nCountry-year wise frequency of reporting dates of UFO:")
print(result)


# In[ ]:


Q134. Write a pandas program to get the difference (in days) between 
documented date and reporting date of unidentified flying object 
(UFO).


# In[ ]:


Q135. Write a pandas program to generate sequences of fixedfrequency dates and time spans.


# In[ ]:


import pandas as pd
dtr = pd.date_range('2018-01-01', periods=12, freq='H')
print("Hourly frequency:")
print(dtr)
dtr = pd.date_range('2018-01-01', periods=12, freq='min')
print("\nMinutely frequency:")
print(dtr)
dtr = pd.date_range('2018-01-01', periods=12, freq='S')
print("\nSecondly frequency:")
print(dtr)
dtr = pd.date_range('2018-01-01', periods=12, freq='2H')
print("nMultiple Hourly frequency:")
print(dtr)
dtr = pd.date_range('2018-01-01', periods=12, freq='5min')
print("\nMultiple Minutely frequency:")
print(dtr)
dtr = pd.date_range('2018-01-01', periods=12, freq='BQ')
print("\nMultiple Secondly frequency:")
print(dtr)
dtr = pd.date_range('2018-01-01', periods=12, freq='w')
print("\nWeekly frequency:")
print(dtr)
dtr = pd.date_range('2018-01-01', periods=12, freq='2h20min')
print("\nCombine together day and intraday offsets-1:")
print(dtr)
dtr = pd.date_range('2018-01-01', periods=12, freq='1D10U')
print("\nCombine together day and intraday offsets-2:")
print(dtr)


# In[ ]:


Q136. Write a pandas program to manipulate and convert date times 
with timezone information.


# In[4]:


from datetime import datetime
datetime_object = datetime.now()
print(datetime_object)
print('Type :- ',type(datetime_object))


# In[ ]:


Q136. Write a pandas program to manipulate and convert date times 
with timezone information.


# In[ ]:


Q137. Write a pandas program to create the graphical analysis of UFO 
(unidentified flying object) Sightings year.


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r'ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
df["ufo_yr"] = df.Date_time.dt.month
months_data = df.ufo_yr.value_counts()
months_index = months_data.index  # x ticks
months_values = months_data.get_values()
plt.figure(figsize=(15,8))
plt.xticks(rotation = 60)
plt.title('UFO sighted by Month')
plt.xlabel("Months")
plt.ylabel("Number of sighting")
months_plot = sns.barplot(x=months_index[:60],y=months_values[:60], palette = "Oranges")


# In[ ]:


Q138. Write a pandas program to create a comparison of the top 10 
years in which the (UFO) was sighted VS each Month.


# In[ ]:


Q139. Write a pandas program to create a heatmap (rectangular data as
a colour-encoded matrix) for comparison of top 10 years in 
which (UFO ) was sighted VS each Month.


# In[ ]:


Q140. Write a pandas program to create a Timewheel of Hour VS Year
comparison of the top 10 years in which the (UFO) was sighted.


# In[ ]:


Q141. Write a python program to draw the line using given axis values 
with the suitable label in the x-axis, y-axis, and a title.


# In[ ]:


import matplotlib.pyplot as plt
with open("test.txt") as f:
    data = f.read()
data = data.split('\n')
x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[1] for row in data]
plt.plot(x, y)
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title 
plt.title('Sample graph!')
# Display a figure.
plt.show()


# In[ ]:


Q142. Write a python program to draw the line charts of the financial 
data of the Alphabet Inc., between October.


# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('fdata.csv', sep=',', parse_dates=True, index_col=0)
df.plot()
plt.show()


# In[ ]:


Q143. Write a Python program to plot two or more lines on same plot 
with the suitable legends of each line.


# In[ ]:


import matplotlib.pyplot as plt
# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
# plotting the line 1 points 
plt.plot(x1, y1, label = "line 1")
# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
# plotting the line 2 points 
plt.plot(x2, y2, label = "line 2")
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title of the current axes.
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()


# In[ ]:


Q144. Write a python programming to display a bar chart of the 
popularity of programming languages.


# In[6]:


import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color=(0.4, 0.6, 0.8, 1.0))
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
# Rotation of the bars names
plt.xticks(x_pos, x, rotation=90)
# Custom the subplot layout
plt.subplots_adjust(bottom=0.4, top=.8)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# In[ ]:


Q145. Write a python programming to display a horizontal bar chart of 
the popularity of programming languages.


# In[7]:


import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color='green')
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.yticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# In[ ]:


Q146. Write a python programming to display a bar chart of the 
Popularity of programming languages. Increase bottom margin.


# In[ ]:


Q147. Write a python program to create the bar plot from a DataFrame.


# In[8]:


from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

a=np.array([[4,8,5,7,6],[2,3,4,2,6],[4,7,4,7,8],[2,6,4,8,6],[2,4,3,3,2]])
df=DataFrame(a, columns=['a','b','c','d','e'], index=[2,4,6,8,10])

df.plot(kind='bar')
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

plt.show()


# In[ ]:


Q148. Write a python program to draw the scatter plot comparing two 
subject marks of Mathematics and Science. Use marks of 10 students.


# In[9]:


import matplotlib.pyplot as plt
import pandas as pd
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(marks_range, math_marks, label='Math marks', color='r')
plt.scatter(marks_range, science_marks, label='Science marks', color='g')
plt.title('Scatter Plot')
plt.xlabel('Marks Range')
plt.ylabel('Marks Scored')
plt.legend()
plt.show()


# In[ ]:


Q149. Write a python program to draw the scatter plot for three different 
groups comparing weights and heights.


# In[ ]:


import matplotlib.pyplot as plt
import numpy as np 
weight1=[67,57.2,59.6,59.64,55.8,61.2,60.45,61,56.23,56]
height1=[101.7,197.6,98.3,125.1,113.7,157.7,136,148.9,125.3,114.9] 
weight2=[61.9,64,62.1,64.2,62.3,65.4,62.4,61.4,62.5,63.6]
height2=[152.8,155.3,135.1,125.2,151.3,135,182.2,195.9,165.1,125.1] 
weight3=[68.2,67.2,68.4,68.7,71,71.3,70.8,70,71.1,71.7]
height3=[165.8,170.9,192.8,135.4,161.4,136.1,167.1,235.1,181.1,177.3]
weight=np.concatenate((weight1,weight2,weight3))
height=np.concatenate((height1,height2,height3))
plt.scatter(weight, height, marker='*', color=['red','green','blue'])
plt.xlabel('weight', fontsize=16)
plt.ylabel('height', fontsize=16)
plt.title('Group wise Weight vs Height scatter plot',fontsize=20)
plt.show()


# In[ ]:


Q150. Write a python program to draw a scatter plot to find sea-level 
rise in past 100 years.


# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('data.csv')
year = data['year']
sea_levels = data['CSIRO_sea_level']
plt.scatter(year, sea_levels, edgecolors='g')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sealevel')
plt.show()

