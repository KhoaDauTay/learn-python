# Section 05: Learn Exception Handling & File Handling In Python
## Lesson overview
- Errors and Exceptions:
- Exceptions
- The try statement works as follows
- File handling in python
- The open Function
- Syntax
### Errors & exceptions in Python
- The exception is errors that may arise during program execution.
    - Access variable does not exist
    - Open file does not exist
    - Converts an invalid string to a number
    - Access exceeds the index of the List
    - Key access does not exist in Dictionary
    - ...
- When an error occurs, if not handled, Python will issue an error message and stop the program.
    - Example :
    ```
    print(int('a'))
    ```
    The above program, when running, will give the following notice:
    ```diff
    - ValueError: invalid literal for int() with base 10: 'a'
    ```

### Exception handling in Python
- How to handle exceptions in Python:
    ```
    try:
        # do something
    except:
        print("Exception occurred")
    ```
- When an exception occurs, the program will run into the block below the except: line, then the next segment of the try / except block will continue to execute.
- To handle each exception exception individually, the exception type can be specified in the except declaration
    ```
    try:
        # do something
    except ErrorType1:
        print("Error type 1")
    except ErrorType2:
        print("Error type 2")
    except:
        print("Other exception")
   ``` 
   Example
   ```
    try:
        x = int('a')
    except ValueError:
        print("Invalid input number")
    except:
        print("Other exception")   
   ```

### Finally block
- In case you want to perform an action after finishing a job regardless of the exception that occurred during the execution of that job, the structure can be used:
    ```
    try:
    # do something
    except:
    print("Exception occurred")
    finally:
    print('After try/except finished')
    ```
### File handling
- Open file in Python :
    ```
    f = open (<file_name>, <mode>, encoding = <encoding>)
    ```
- Inside :
    - <file_name>: the file name to open
    - mode: File open mode, commonly used values:
        - 'r': Open file for reading, this is the default value
        - 'rb': Open file for reading in binary format
        - 'w': Create a new file for writing
        - 'wb': Create a new file for writing in binary format
        - 'a': Open file for appending (append)
        - 'ab': Open the file to add the end of it in binary format

    - encoding: Encoding mode with text file
        - None: the default value, depending on the system
        - 'utf-8': Unicode encoding in UTF-8
### Reading data from file
- Read the entire file content:
    ```
    data = f.read ()
    ```
    If the file is opened in text mode ('r'), the file reading is a string variable. If the file is opened in binary mode ('rb'), the file read result is a variable with a data type of bytes.
- Read the entire lines of the file (with text files):
    If the file is opened in text mode ('r'), the file contents can be read line by line with the command:
    ```
    lines = f.readlines ()
    ```
    The result is a List, each element is a string containing the contents of the file's lines
- Read each line of the file:
    If the file is opened in text mode ('r'), it is possible to read file by line with the structure:
    ```
    for line in f:
        # process line
    ```
### Adding data to the file
- For text files, the data to write to the file requires a string type
    ```
    f.write (<string>)
    ```
    For example:
    ```
    f = open ('test.txt', 'w')
    f.write ('hello')
    f.close ()
    ```

- For binary files, the data written to the file needs to be of type bytes
    ```
    f.write (<bytes>)
    ```
    For example:
    ```
    f = open ('test.dat', 'wb')
    f.write ('hello'.encode ())
    f.close ()
    ```
### Appending to a file
- After opening the file with the open command, close the file with the close command to avoid missing the file contents at the end of the program. To avoid forgetting to close the file after opening, you can use the with structure:
    ```
    with open (<file_name>, <mode>, <encoding>) as f:
        # Process file
    ```
- With the with structure, the file is automatically closed when the program has finished running the block inside the with.
    For example:
    ```
    with open ('test.txt', 'w') as f:
        f.write ('Line1 \ n')
        f.write ('Line2 \ n')
    ```
### Quiz 4: Quiz For Section 5:
- The code in the finally block is executed: No matter if the exception occurs or not
- Appending to a file: Keeps previous contents of the file
- Writing data to the file: Removes/ discards previous contents
- Following blocks can be used to accept exceptions: Both try and except block
### Coding challenge 5
- Write a function which would divide two numbers, design the function in a manner that it handles the divide by zero exception.
### Coding challenge 5 solution
    ```
    def divide(a,b):
        try:
            return a/b
        except ZeroDivisionError:
            print("There is a divide by zero error")
            return 0
    
    x = float(input('Enter a number'))
    y = float(input('Enter value by which you want to divide the number'))
    result = divide(x, y)
    print(result)
    ```
### Coding challenge 6
- Write Python code to open a file named demo.txt and write some random data into it.

- Open the file, read the contents and display them as output.

- Write python code to add additional text to the existing file on a new line without deleting the previous contents.
### Coding challenge 6 solution
    ```
    f= open('demo.txt', 'w')
    f.write("hello there")
    f.close()
    
    #reading data from the file
    
    f= open('demo.txt','r')
    print(f.read())
    f.close()
    
    #adding additional contents
    
    f= open('demo.txt','a')
    f.write('\n Hello again')
    f.close()
    ```
### Notes & Summary For Section 5