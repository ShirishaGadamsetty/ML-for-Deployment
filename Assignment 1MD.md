
## Task 1:

1. Install Jupyter notebook and run the first program and share the screenshot of the output


```python
1+2
```




    3



2. Write a program which will find all such numbers which are divisible by 7 but are not a  multipleof 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.


```python
list = []
for i in range(2000,3200):
    if i%7==0 :
        if i%5!=0:
            list.append(i)
# print(list)
s = [str(i) for i in list] 
print(",".join(s))
```

    2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199
    

3. Write a Python program to accept the user's first and last name and then getting them      printed in the the reverse order with a space between first name and last name.



```python
# print("Enter your first name")
firstname = input("Enter your first name")
lastname = input("enter your last name")
print(firstname[::-1] + " " + lastname[::-1])

```

    Enter your first nameshirisha
    enter your last nameraghunath
    ahsirihs htanuhgar
    

4. Write a Python program to find the volume of a sphere with diameter 12 cm.
   Formula: V=4/3 * π * r3


```python
r=12
pi = 3.1415926535897931
v = 4/3 * pi* r**3
print(v)
```

    7238.229473870882
    

# Task 2:
1. Write a program which accepts a sequence of comma-separated numbers from console and
   generate a list.



```python
values = input("enter comma seperated values")
list = values.split(",")

print('List : ',list)
```

    enter comma seperated values1,2,3,4,5,6
    List :  ['1', '2', '3', '4', '5', '6']
    

2. Create the below pattern using nested for loop in Python.



```python
for i in range(0,5):
    for j in range(0,i+1):
        print("* ",end="") #end:   string appended after the last value, default a newline.
    print("\r")  
for i in range(5,0,-1):
    for j in range(0,i+1):
        print("* ",end="") #end:   string appended after the last value, default a newline.
    print("\r")      
```

    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    * * * * * * 
    * * * * * 
    * * * * 
    * * * 
    * * 


3. Write a Python program to reverse a word after accepting the input from the user.
   Sample Output:
   Input word: AcadGild
   Output: dilGdacA


```python
s = input("enter your word ")
def reverse_slicing(s):
    return s[::-1]
print(reverse_slicing(s))

```

    enter your word shirisha
    ahsirihs
    


```python
s = input("enter your word")
s[::-1]
```

    enter your wordshirisha
    




    'ahsirihs'



4. Write a Python Program to print the given string in the format specified in the sample output.
   WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens


```python
print("WE, THE PEOPLE OF INDIA\n\thaving solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\tand to secure to all its citizens \n")  

```

    WE, THE PEOPLE OF INDIA
    	having solemnly resolved to constitute India into a SOVEREIGN,! 
    		SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC 
    		and to secure to all its citizens 
    
    
