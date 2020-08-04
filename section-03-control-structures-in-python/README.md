# Section 03: Basic Python Concepts
## Lesson overview
- If statements in Python
- A few important things to note about if statements
- Elif statement in Python
- Lists in Python
- List functions in Python
- Functions in Python
- Defining a function
- Calling a function
- For loop in Python
- While loop in python
### If and Elif statement in Python 
- If constructs in Python:
    ```
    if <condition>:
        <Command>
    ---
    if <condition>:
        <Command 1>
    else:
        <Command 2>
    ---
    if <condition 1>:
        <Command 1>
    elif <condition 2>:
        <Command 2>
    elif <condition 3>:
        <Command 3>
    else:
        <Command 4>
    ```
- Note:
    - At the end of the line if / elif / else statements is a colon. Python uses colons to start a child command block
    - The lines of a sub-block below if / elif / else are rewritten in some spaces (usually 4 spaces or 1 tab) compared to the parent line. The lines of a command block must be written in line with each other.
- The logical condition in an if statement
    - The logical condition in an if statement is essentially an expression, but accepts only one of two True / False values. This condition is usually created from operations:
    - The comparisons:
        - Greater than:>
        - Less than: <
        - Greater than or equal to:> =
        - Less than or equal to: <=
        - Equal: ==
        - Different:! =
    - Negative operations: not

    - Spell and: and

    - Permission or: or
- Example : Enter from the 2-digit keyboard and print the minimum value for those 2 numbers
    ```
    a = input('Số thứ nhất : ')
    a = float(a)

    b = input('Số thứ hai : ')
    b = float(b)

    if a < b:
    print(a)

    else:
    print(b)
    ```
### Introduction to lists in Python
- The List data type is used to contain a range of elements. When declaring values, the word parts of a List are enclosed in [].
    Example :
    ```
    >>> champion = ['Khoa','Huynh',3,5,2000]
    >>> address = ['Chua Lang','Ha Noi']
    >>> print(champion)
    ['Khoa','Huynh',3,5,2000]
    ```
    Elements of a List may not have the same data type.
### List operations in Python
- Similar to the String type, the List type can also access each element or retrieve sub-fragments using structures:
    - lst [i]: the i-th element of List
    - lst [start: end]: The child list contains elements from start to end-1
    - lst [start:]: The child list contains elements from the start index to the end of the List
    - lst [: end]: The child list contains elements from index 0 to end-1
- Can access each element of the array by index, part
The first element in the order is [0]
    Example :
    ```
    >>> champion = ['Khoa','Huynh',3,5,2000]
    >>> print(champion[1])
    Huynh
    >>> print(champion[0])
    Khoa
    >>> print(champion[-1])
    2000
    ```
- You can calculate series of numbers together, or do calculations on that series
    ```
    >>> a = [3,4,5]
    >>> b = [1,2,3]
    >>> x = a + b
    >>> print(x)
    [3, 4, 5, 1, 2, 3]
    >>> y = a[0] + b[1]
    >>> print(y)
    5
    ```
### List functions in Python
- Len: returns the number of elements in a List
    For example:
    ```
    >>> ds = [1, 2, 3, 4, 5];
    >>> print (len (ds))
    5
    ```
- Append: Add a new element to the List
    For example:
    ```
    >>> ds = [1, 2, 3, 4, 5]
    >>> ds.append (6)
    >>> print (ds)
    [1, 2, 3, 4, 5, 6]
    ```
- Remove function: Removes an element from the List
    For example:
    ```
    >>> ds = [1, 2, 3, 4, 5]
    >>> ds.remove (3)
    >>> print (ds)
    [1, 2, 4, 5]
    ```
- Extend function: Concatenates a child List at the end of a List
    For example:
    ```
    >>> ds = [1, 2, 3, 4, 5]
    >>> ds.extend ([6, 7])
    >>> print (ds)
    [1, 2, 3, 4, 5, 6, 7]
    ```
- Addition of 2 Lists: Returns a new List by concatenating 2 Lists together
    For example:
    ```
    >>> ds = [1, 2, 3, 4, 5]
    >>> ds + = [6, 7]
    >>> print (ds)
    [1, 2, 3, 4, 5, 6, 7]
    ```
- Reverse function: reverse a List
    For example:
    ```
    >>> ds = [1, 2, 3, 4, 5]
    >>> ds.reverse ()
    >>> print (ds)
    [5, 4, 3, 2, 1]
    ```
- Print operation: Check if an element is in the List
    For example:
    ```
    >>> ds = [1, 2, 3, 4, 5]
    >>> print (1 in ds)
    True
    ```
- The not in operation: Checks whether an element is not in the List
    For example:
    ```
    >>> ds = [1, 2, 3, 4, 5]
    >>> print (3 not in ds)
    False
    ```

- Index function: Finds the position of an element in the List
    For example:
    ```
    >>> ds = [1, 2, 3, 4, 5];0 print (ds.index (3))
    2
    ```
- Min function: Returns the minimum value of a List
    For example:
    ```
    >>> ds = [1, 3, 2, 5, 4]
    >>> print (min (ds))
    first
    ```

- Max function: Returns the maximum value of a List

    For example:
    ```
    >>> ds = [1, 3, 2, 5, 4]
    >>> print (max (ds))
    5
    ```
### Range function in Python
- The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
- Systax 
    ```
    range(start, stop, step)
    ```
- Parameter Values
    - start : Optional. An integer number specifying at which position to start. Default is 0
    - stop  : Required. An integer number specifying at which position to stop (not included).
    - step  : Optional. An integer number specifying the incrementation. Default is 1
- Example:
    - Create a sequence of numbers from 3 to 5, and print each item in the sequence:
    ```
    x = range(3, 6)
    for n in x:
    print(n)
    3
    4
    5
    ```
    - Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:
    ```
    x = range(3, 10, 2)
    for n in x:
    print(n)
    3
    5
    7
    9
    ```
### Code reuse and functions in Python
- Structure for declaring functions in Python:
    ```
    def function_name (<list_variables_name>):
        <command function>
        return <result>
    ```
    For example:
    ```
    def square (x):
    return x * x
    for i in range (1.11):
    print (f '{i} * {i} = {square (i)}')
    ```
- The function returns multiple values
    - A function can return multiple values, a list of returned values separated by commas
    For example:
    ```
    def calcAreaAndPerimeter (width, height):
        S = width * height
        P = 2 * (width + height)
        return S, P
    A, P = calcAreaAndPerimeter (5, 4)
    print ('A =', A)
    print ('P =', P)
    ```
    In this case, it is understandable that the result returned is a Tuple type value
- The default value of the parameter in the function
    - When declaring a function, it is possible to declare default values for parameters. When calling the function, if a parameter is missing but the default value has been declared in the function declaration, that parameter will be passed to the default value.
    ```
    def getAddress(street, city, country='Việt Nam'):
    return f'{street}, {city}, {country}' 
    print(getAddress('Thái Hà', 'Hà Nội'))
    ```
### For Loop in Python
- The for loop structure is used to perform a loop with known number of iterations. The for loop structure is as follows:
    ```
    for variables_name in list_variable:
        <block_code>
    ```
- How to represent repeating values set in for loop
    - List the components of a value set. For example [1, 2, 3, 4, 5]. This is essentially List-type data (described later).
    - Use structure:
    ```
    range (<end>)
    ```
    - This expression represents a set of integers from 0 to the value : end, (ie end-1).
    For example:
    ```
    range (5) → 0, 1, 2, 3, 4
    ```
    - Use structure:
    ```
    range (start, end)
    ```
    - This expression represents the set of integers from <start> to <end-1>
    For example:
    ```
    range (1, 5) → 1, 2, 3, 4
    ```
    - Use structure:
    ```
    range (start, end, increment)
    ```

    - This expression represents the set of integers from <start> to <end-1> and grows steadily with increment spacing.
    For example:
    ```
    range (0, 10, 2) → 0, 2, 4, 6, 8
    ```
- Example Code :
    - Example 1: Sum the numbers from 1 to 100
    ```
    S = 0
    for i in range (1, 101):
        S + = i
    print ('S =', S)
    ```
    - Example 2: Write a program to print the multiplication table
    ```
    for i in range (2, 10):
        for j in range (2, 10):
            print (i, '*', j, '=', i * j)
    ```
### Boolean logic in Python
- Booleans represent one of two values: True or False.
- In programming you often need to know if an expression is True or False.

- You can evaluate any expression in Python, and get one of two answers, True or False.

- When you compare two values, the expression is evaluated and Python returns the Boolean answer:
    Example:
    ```
    >>> print(10 > 9)
    True
    >>> print(10 == 9)
    False
    >>> print(10 < 9)
    False
    ```
- When you run a condition in an if statement, Python returns True or False:
    Example:
    ```
    a = 1
    b = 2
    if a > b:
        print('a > b')
    else:
        print('a < b')
    ```
### While loop in Python
- The while loop structure is used to execute a loop with an unknown number of iterations. The while loop structure is as follows:
    ```
    while(<condition>):
        <command line>
    ```
- Some illustrative examples
    - Example 1: Checks whether a number is prime
    ```
    x = int (input ('x ='))
    i = 2
    while i * i <= x:
        if x% i == 0:
            j = x // i
            print (x, '=', i, '*', j)
            exit ()
        i + = 1
    print (x, 'is prime')
    ```

    - Example 2: Converts a number from decimal to binary
    ```
    x = int (input ('x ='))
    s = ''
    while x> 0:
        i = x% 2
        s = str (i) + s
        x = int (x / 2)
    print (s)
    ```
### Quiz For Section 3
- Which of the following are the two possible boolean values: True and False
- != is a: Comparison operator
- The difference between = & == : == is a comparison operatorr and = is an assignment operator
- A list is represented in: [ ] square brackets
- A while and a for loop is used for: Repeating a set of code multiple number of times
### Coding challenge 2
- Create a list of your favorite food items, the list should have minimum 5 elements.
- List out the 3rd element in the list.
- Add additional item to the current list and display the list.
- Insert an element named tacos at the 3rd index position of the list and print out the list elements.
### Coding challenge 2 solution
```
food = ['eggs', 'pizza', 'cupcake', 'burger', 'salmon']
print(food[2])
food.append('cake')
print(food)
food.insert(3, 'tacos')
print(food)
```
### Coding challenge 3
- Task no 1: Using a for-loop and a range function, print "I am a programmer" 5 times.
- Task no 2: Create a function which displays out the square values of numbers from 1 to 9.
### Coding challenge 3 solution
- Task 1:
    ```
    for x in range(5):
        print('I am a programmer') 
    ```
- Task 2:
    ```
    def display_square():
        for x in range(1,10):
            print(x*x)
    display_square()
    ```
### Notes & Summary For Section 3
