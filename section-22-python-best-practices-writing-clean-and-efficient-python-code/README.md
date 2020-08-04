# Section 22: Python Best Practices: Writing Clean & Efficient Python Code
## Lesson overview
- Learn how to write Readable code
- Learn Identation, Comments conventions
- Learn Name conventions
- Learn use Spacebar or Tab
- Learn about Programming recommendations
### Writing Clean Python Code: Best Practices part 1
- Readable code
    - Naming Conventions
    - Code Layout
- Collaboration
- Correct syntax is notenough
### Writing Clean Python Code: Best Practices part 2
- Identation
    - Tab and Space: PEP8 Recommended use space 
- Comments
    - Limit the length of comments and text strings to 72 characters.
    - Use a complete sentence, starting with capital letters.
    - Be sure to update your comment when you change your code.
### Writing Clean Python Code: Best Practices part 3
- Never use single, l, O or I names because they can be mistaken for 1 and 0
- The best way to name a variable is to describe the name it represents.
- Name conventions:
    - function: Use lowercase letters. Separate words by underscores.
        ```
        function, my_function
        ```
    - variables: Use lowercase letters. You can use one character, one word or many words. Separate words by underscores.
        ```
        x, var, my_variable
        ```
    - class: The first letter of each word is capitalized. Do not separate words with underscores. This spell is called camel case.
        ```
        Model, MyClass
        ```
    - methods: Use lowercase letters. Separate words by underscores.
        ```
        class_method, method
        ```
### Writing Clean Python Code: Best Practices part 4
- Whitespace in expressions and statements
- Whitespace around binary operators
    - Assignments (=, + ==, - =, etc.)
    - Comparison (==,! =,>, <, <=,> =) And (is, is not, not in)
    - Booleans (and, not, or)
    ```
    # Recommended
    y = x**2 + 5
    z = (x+y) * (x-y)

    # Not Recommended
    y = x ** 2 + 5
    z = (x + y) * (x - y)
    ```
### Writing Clean Python Code: Best Practices part 5
- Do not compare boolean values with True or False using equivalent operators
- Use definitions when checking empty strings in an if statement
- Using is not rather than not ... is in the If statement
- Do not use if x: when you mean if x not None
- Use .startswith () and .endswith () instead of slicing
### Notes
- If you follow all the advice of PEP 8, you can ensure that you will have clean, professional and readable code. This will benefit you as well as potential collaborators and employers.
- However, some of the PEP 8 guidelines are inconvenient in the following situations:
    - Compliance with PEP 8 will break compatibility with existing software.
    - If the code around what you are doing is not compliant with PEP 8.
    - If the code needs to remain compatible with older versions of Python.