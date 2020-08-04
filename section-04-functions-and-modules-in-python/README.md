# Section 04: Basic Python Concepts
## Lesson overview
- Returning a value from a function
- Passing functional arguments to functions
- Modules in Python
### Passing arguments to functions in Python
- You can call a function by using the following types of formal arguments:
    - Required arguments
    - Keyword arguments
    - Default arguments
    - Variable-length arguments
- Required arguments
    Required arguments are the arguments passed to a function in correct positional order. Here, the number of arguments in the function call should match exactly with the function definition.
    To call the function printme(), you definitely need to pass one argument, otherwise it gives a syntax error as follows
    ```
    # Function definition is here
    def printme( str ):
    "This prints a passed string into this function"
    print str
    return;

    # Now you can call printme function
    printme()
    ```
    When the above code is executed, it produces the following result
    ```
    Traceback (most recent call last):
        File "test.py", line 11, in <module>
            printme();
    TypeError: printme() takes exactly 1 argument (0 given)
    ```
- Keyword arguments
    Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name.

    This allows you to skip arguments or place them out of order because the Python interpreter is able to use the keywords provided to match the values with parameters. You can also make keyword calls to the printme() function in the following ways
    ```
    def printme( str ):
    "This prints a passed string into this function"
    print str
    return;

    # Now you can call printme function
    printme( str = "My string")
    ```
    When the above code is executed, it produces the following result
    ```
    My string
    ```
    The following example gives more clear picture. Note that the order of parameters does not matter.
    ```
    # Function definition is here
    def printinfo( name, age ):
    "This prints a passed info into this function"
    print "Name: ", name
    print "Age ", age
    return;

    # Now you can call printinfo function
    printinfo( age=50, name="miki" )
    ```
    When the above code is executed, it produces the following result
    ```
    Name:  miki
    Age  50
    ```
- Default arguments
    A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument. The following example gives an idea on default arguments, it prints default age if it is not passed
    ```
    # Function definition is here
    def printinfo( name, age = 35 ):
        "This prints a passed info into this function"
        print "Name: ", name
        print "Age ", age
        return
    # Now you can call printinfo function
    printinfo( age=50, name="miki" )
    printinfo( name="miki" )
    ```
    When the above code is executed, it produces the following result
    ```
    Name:  miki
    Age  50
    Name:  miki
    Age  35
    ```
- Variable-length arguments
    You may need to process a function for more arguments than you specified while defining the function. These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.
    Syntax for a function with non-keyword variable arguments is this
    ```
    def functionname([formal_args,] *var_args_tuple ):
        "function_docstring"
        function_suite
        return [expression]
    ```
    An asterisk (*) is placed before the variable name that holds the values of all nonkeyword variable arguments. This tuple remains empty if no additional arguments are specified during the function call. Following is a simple example
    ```
    # Function definition is here
    def printinfo( arg1, *vartuple ):
        "This prints a variable passed arguments"
        print "Output is: "
        print arg1
        for var in vartuple:
            print var
        return
    # Now you can call printinfo function
    printinfo( 10 )
    printinfo( 70, 60, 50 )
    ```
    When the above code is executed, it produces the following result
    ```
    Output is:
    10
    Output is:
    70
    60
    50
    ```
### Making function return value in Python
- A return statement is used to end the execution of the function call and “returns” the result (value of the expression following the return keyword) to the caller. The statements after the return statements are not executed. If the return statement is without any expression, then the special value None is returned.

- Note: Return statement can not be used outside the function.
- Syntax :
    ```
    def fun():
        statements
        .
        .
        return [expression]
    ```
    Example:
    ```
    def add(a, b): 
        # returning sum of a and b 
        return a + b 
    def is_true(a): 
        # returning boolean of a 
        return bool(a) 
    # calling function 
    res = add(2, 3) 
    print("Result of add function is {}".format(res)) 
    res = is_true(2<5) 
    print("\nResult of is_true function is {}".format(res)) 
    ```
    Output:
    ```
    Result of add function is 5

    Result of is_true function is True
    ```
### Passing functions as arguments in Python
- A function can take multiple arguments, these arguments can be objects, variables(of same or different data types) and functions. Python functions are first class objects. In the example below, a function is assigned to a variable. This assignment doesn’t call the function. It takes the function object referenced by shout and creates a second name pointing to it, yell.
    ```
    def shout(text):  
        return text.upper()  
    print(shout('Hello'))  
    yell = shout  
    print(yell('Hello'))  
    ```
    Output:
    ```
    HELLO
    HELLO
    ```
### Modules in Python
- When building a large program, usually the functions will be broken down into modules for easy development and maintenance.
    Example : 
    ```
    #main.py
    def add2num(a,b):
        return a + b
    print(add2num(1,2))
    ```
    - When the program is large, instead of putting all the functions in one file, we create small files to contain processing functions, such as the add.py file with the following content:
    ```
    def add2num(a,b):
        return a + b
    ```
    -
### Quiz For Section 4
- Code reuse helps in:
    - Reducing the repetition of code
    - Optimizing the code
    - Making the code more readable
- Code reuse can be achieved by using: Functions
- A function in Python can:
    - Return values
    - Accept values
### Coding challenge 4
- Create a BMI calculator, BMI which stands for Body Mass Index can be calculated using the formula:
    BMI = (weight in Kg)/(Height in Meters)^2.
- Write python code which can accept the weight and height of a person and calculate his BMI.
    note: Make sure to use a function which accepts the height and weight values and returns the BMI value.
### Coding challenge 4 solution
    ```
    def calculate_BMI(new_weight, new_height):
        new_bmi = new_weight/(pow(new_height, 2))
        return new_bmi
    weight = float(input('Enter weight in Kgs'))
    height = float(input('Enter height in meters'))
    bmi = calculate_BMI(weight, height)
    print(bmi)
    ```

### Notes & Summary For Section 4