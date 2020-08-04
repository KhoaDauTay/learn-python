# Section 06: Some more types in Python
## Lesson overview
- Dictionaries in Python
- Updating Dictionary
- Delete Dictionary Elements
- Built-in Dictionary Functions & Methods
- Tuples in Python
- Accessing Values in Tuples

### Dictionaties
- The Dictionary data type is used to store a 1-1 conversion table between two sets:
    - Source set (or key set) (key): contains the information to look up
    - Target set (or value set): contains information of each key from the source set
- Syntax of Dictionary-type declaration in Python:
    ```
    d = {
        <key1>: <value1>,
        <key2>: <value2>,
        ...
    }
    ```
    For example:
    ```
    d = {"one": 1, "two": 2, "three": 3}
    ```
- To access the key element in Dictionary, Python uses the [] operation:
    ```
    d [<key>]
    ```
    For example:
    ```
    >>> d = {"one": 1, "two": 2, "three": 3}
    print (d ['a'])
    1
    ```
- In case if the value key is not in the Dictionary's source file, Python will issue an Exception message:
    ```
    >>> d = {"one": 1, "two": 2, "three": 3}; print (d ['four'])
    ```
    ```
    Traceback (most recent call last):
    File "<pyshell # 118>", line 1, in <module>
        d = {"one": 1, "two": 2, "three": 3}
        print (d ['four'])
    KeyError: 'four'
    ```
- To avoid this error, you can use the get function of Dictionary to pass the default value in case key is not in the source of Dictionary:
    ```
    d.get (<key>, <gia_tri_mac_dinh>)
    ```
    For example:
    ```
    >>> d = {"one": 1, "two": 2, "three": 3}
    print (d.get ('four', -1))
    -1
    ```
- Some illustrative examples
    - Example 1: Count the frequency of words in a sentence
    ```
    text = 'One year has twelve months, February has twenty-eight days, the remaining months have thirty or thirty-one days'
    text = text.lower ()
    for c in ['.', ',', ':']:
        text = text.replace (c, '')
    words_count = {}
    for word in text.split ():
        words_count [word] = words_count.get (word, 0) + 1
    for word in words_count:
        print (word, ':', words_count [word])
    ```
    - Example 2: Converts the Vietnamese pronunciation of a number in the range 1-99 into that numerical value. For example: eighty-five → 85
    ```
    bang_so1 = {'một' : 1, 'hai' : 2, 'ba' : 3, 'bốn' : 4, 'năm' : 5, 'sáu' : 6, 'bảy' : 7, 'tám' : 8, 'chín' : 9, 'mười' : 10}
    bang_so2 = {'một' : 1, 'hai' : 2, 'ba' : 3, 'bốn' : 4, 'lăm' : 5, 'sáu' : 6, 'bảy' : 7, 'tám' : 8, 'chín' : 9}
    bang_so3 = {'mươi' : 0, 'mốt' : 1, 'hai' : 2, 'ba' : 3, 'bốn' : 4, 'tư' : 4, 'lăm' : 5, 'sáu' : 6, 'bảy' : 7, 'tám' : 8, 'chín' : 9}

    text = input('text=')
    words = text.lower().split()
    N = len(words)

    if N == 1:
        if words[0] in bang_so1:
            print(bang_so1[words[0]])        
    else:
        print('Không tồn tại số')
    exit()

    chuc, donvi = -1, -1
    if (N == 3 and words[1] == 'mươi') or N == 2:
        chuc = bang_so1.get(words[0], -1)
        donvi = bang_so3.get(words[-1], -1)
    if N == 2 and words[0] == 'mười':
        chuc = 1
        donvi = bang_so2.get(words[1], -1)
    if chuc >= 0 and donvi >= 0:
        print(10 * chuc + donvi)
    else:
        print('Không tồn tại số')
    ```
### Dictionaries Function
- dict.clear (): Delete all data inside the object
statue
- dict.copy (): Returns a copy of the object
- dict.fromkeys (seq [, value]): Create an object with
list key from seq and if passed value then get
That makes the values for the elements.
- dict.has_key (key): check if a key exists in
object or not.
- dict.keys (): Returns a List containing the keys
- dict.values (): Returns a List containing values
### Tuples
- Tuple data is similar to List type, except that it cannot be edited (added, deleted). Elements of group data are enclosed in ()
    ```
    num_list = (1, 3, 5, 7, 9)
    list_fresher = ("Khoa", "Vinh", "Toàn","Quân")
    ```
- Calculations on Tuple
    The calculations on Tuple are nearly the same as the List calculations, but Tuple only supports reading of Tuple information, not calculations that change the contents of Tuple.
    - len(): returns the number of elements of a Tuple
    - Addition of 2 Tuples: returns a new Tuple by joining 2 Tuples together
    - in: Check if an element is in the Tuple
    - not in: Checks whether an element is not in the Tuple
    - index(): Find the position of an element in Tuple
    - min(): Returns the minimum value of a Tuple
    - max(): Returns the maximum value of a Tuple
    - Access the element via index: same as List
### List Slicing
- Access to each element of the List
    Similar to the String type, the List type can also access each element or retrieve sub-fragments using structures:
    - lst [i]: the i-th element of List
    - lst [start: end]: The child list contains elements from start to end-1
    - lst [start:]: The child list contains elements from the start index to the end of the List
    - lst [: end]: The child list contains elements from index 0 to end-1
### List Comprehension
- Syntax:
    ```
    *result* = [ *transform* *iteration* *filter* ]
    ```
    Example: Create list
    ```
    name_of_list = [ item_to_append for item in list ]
    ```
    Then, create condition for create list
    ```
    name_of_list = [ item_to_append for item in list if condition ]
    ```
### String formatting
- To combine multiple string values into one, you can use the string addition as shown above:
    ```
    x = 1
    y = 2
    z = 3
    st = 'The sum of' + str (x) + 'and' + str (y) + 'is' + str (z)
    print (st)
    ``` 
- However, adding multiple strings makes it difficult for the program to track, so you can use the format function of the string data type to concatenate multiple strings (and other data types) together.
    ```
    x = 1
    y = 2
    z = 3
    st = 'The sum of {} and {} is {}'. format (x, y, z)
    print (st)
    ```
- Each {} pair in the string template will correspond to a variable / expression inside the format function.
- Alternatively, you can write the name of the variable / expression right inside the {} pair if using the prefix f before the string template, how to do the following:
    ```
    x = 1
    y = 2
    z = 3
    st = f'The sum of {x} and {y} is {z}'
    print(st)
    ```
### String functions
- str(): converts from other data types to string data
    ```
    >>> age = 1
    >>> print(type(age))
    <class 'int'>
    >>> age= str(age)
    >>> print(type(age))
    <class 'str'>
    ```
- lower(): converts string values to lowercase
    ```
    >>> a = 'KHOA'
    >>> print(a.lower())
    khoa
    ```
- upper(): converts string values to uppercase
    ```
    >>> 'khoa'.upper()
    KHOA
    ```
- replace(): Replace the value of a sub-paragraph in a string with another value
    ```
    >>> 'Tôi sống ở Đà Nẵng'.replace('Đà Nẵng', 'Hà Nội')
    'Tôi sống ở Hà Nội'
    ```
- split(): Split a string value into several paragraphs
    ```
    >>> 'Hà Nội'.split()
    ['Hà', 'Nội']
    >>> 'Hà Nội, Việt Nam'.split(',')
    ['Hà Nội', ' Việt Nam']
    ```
- strip(): Removes leading and trailing characters:
    ```
    >>> '   Hà Nội    '.strip()
    'Hà Nội'
    ```
- len(): returns the number of characters of a string value 
    ```
    >>> len('Khoa')
    4
    ```
### Numeric functions
- abs()
- max()
- min()
- https://www.tutorialspoint.com/python/python_numbers.html
### Quiz 5: Quiz For Section 5:
- Dictionaries are represented in: {}
- Tuples are similar to lists, but they are : immutable
### Coding challenge 7
- Write Python code which accepts name of a product and in turn returns their respective prices.
- Make sure to use dictionaries to store products and their respective prices.
- The dictionary should include at least 5 elements.
### Coding challenge 7 solution
    ```
    products = {"Chair":40, "Sofa": 500, "Table": 90, "Monitor": 100 , "Carpet": 200}
    newproduct = input('Enter product name')
    if(newproduct in products):
        print(products.get(newproduct))
    else:
        print('Product Not Found')
    ```
### Coding challenge 8
- List out  all the odd numbers from 1 to 100 using lists in Python.
### Coding challenge 8 solution
```
new_list = list(range(1, 100))
for x in new_list:
    if x % 2 != 0:
        print (x)
```
