# Section 09: Regular expressions in Python
## Lesson overview
- Pattern syntax used in RegEx Python
- Match object
- Use the prefix r before RegEx
### Regular expressions in Python
- Regular Expression (RegEx), also known as a regular expression, is a sequence of special characters that follow certain patterns, representing a string or a set of strings.
```
^a...s$
```
- match():This function attempts to match RE *pattern* to *string* with optional flags.
    - Syntax: ```re.match(pattern, string, flags=0)```
    - ```pattern```: This is the regular expression to be matched.
    - ``string``: This is the string, which would be searched to match the pattern at the beginning of string
    - ``flags``: You can specify different flags using bitwise OR (|). These are modifiers, which are listed in the table belo
    Example:
    ```
    import re
    
    pattern = '^a...s$'
    test_string = 'abyss'
    result = re.match(pattern, test_string)
    
    if result:
        print("Match Successfully.")
    else:
        print("Can't match.")
    ```
    Output
    ```
    Match Successfully.
    ```
### Search & find all
- re.search(): This function searches for first occurrence of RE pattern within string with optional flags.
    - Syntax: ```re.search(pattern, string, flags=0)```
    - ```pattern```: This is the regular expression to be matched.
    - ```string```: This is the string, which would be searched to match the pattern anywhere in the string.
    - ```flags```: You can specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.
    ```
    import re
 
    string = "Khoa live in Ha Noi"
 
    # Check 'Khoa' is it at the beginning of the string
    match = re.search('\AKhoa', string)
 
    if match: 
        print("Found 'Khoa' is located at the top string") 
    else:
        print("Not found Khoa is located at the top string")
    ```
    Output
    ```
    Found 'Khoa' is located at the top string
    ```
- The re.findall () method returns a list of strings containing all results that match the given pattern.
    - Syntax: ```findall(partern, string)```
        - The ```pattern``` is RegEx.
        - ```string``` is the string to match.
    Example:Extract numbers from the following given string: "hello 12 hi 89. Howdy 34"
    ```
    import re   
 
    string = 'hello 12 hi 89. Howdy 34'
    pattern = '\d+'
    
    result = re.findall(pattern, string) 
    print(result)
    ```
    Output
    ```
    ['12', '89', '34']
    ```
### Find & replace
- re.sub(): This is one of the most important methods used with Regular Expression
    - re.sub () will replace all results that match the pattern in the string with another content passed in and return the modified string.
    - Syntax: ```re.sub(pattern, replace, string, count)```
    - The ```pattern```is RegEx.
    - ```replace``` is the replacement for the result string that matches the pattern.
    - ```string``` is the string to match.
    - ```count (integer)``` is the number of replacements. If left blank, Python will treat this value as 0, matching and replacing all strings that meet the criteria.
    Example: The program deletes all spaces
    ```
    import re
 
    string = 'abc 12\
    de 23 \n f45 6'
    
    pattern = '\s+'
    
    replace = ''
    
    new_string = re.sub(pattern, replace, string) 
    print(new_string)
    ```
    Output
    ```
    abc12de23f456
    ```
### The dot metacharacter
- The dot ``.`` matches any regular single character except the newline character '\ n'.
    Example:
    Expression|Example string|Description
    |---------|--------------|-----------|
    |         |```a```       |Does not match because there is only one character|
    |``..``   |```ac```      |Matches because there are two characters|
    |         |```acd```     |Matches because there are two or more characters| 
 
### Caret & dollar metacharacter
- Caret: ``^`` is used to match the beginning of a string.
    Example:
    Expression|Example string|Description
    |---------|--------------|-----------|
    |         |```a```       |Match because starting with ``a``|
    |``^a``    |```abc```     |Match because starting with ``a``|
    |         |```bac```     |Does not match because ``a`` is not in the first| 
- Dollar: ``$`` is used to match the end of a string.
    Example:
    Expression|Example string|Description
    |---------|--------------|-----------|
    |         |```a```       |Match because ending with ``a``|
    |``$a``   |```formula``` |Match because ending with ``a``|
    |         |```cab```     |Does not match because ``a`` is not in the final| 
### Character class
- The square brackets ``[]``are used to represent the set of characters you want to match.
    Example:
    Expression|Example string|Description
    |---------|--------------|-----------|
    |         |  ``a``       |Match because  with ``a``|
    |``[abc]``|``ac``        |Match because  with ``a``|
    |         |``Hey Jude``  |Does not match | 
- Here, ``[abc]`` will match if the string you pass contains any of the letters ``a``, ``b`` or ``c``.
- You can also specify a range of characters using - within the brackets
    - ``[a-e]`` is similar to ``[abcde]``.
    - ``[1-4]`` similar to ``[1234]``.
    - ``[0-39]`` similar to ``[01239]``.
### Star metacharacter
- The asterisk symbol ``*`` can match a string with or without the character defined before it. This character can be repeated many times without quantity restriction.
    Example:
    Expression|Example string|Description
    |---------|--------------|-----------|
    |         |  ``mn``      |Matches because the preceding * character may not appear|
    |         |``man``       |Matches because they appear full of characters| 
    |``ma*n`` |``maaaan``    |Matches because the preceding * character may appear more than once| 
    |         |``main``      |Mismatch because unlike pattern, n does not lie next to a| 
    |         |``woman``     |Matches because they appear full of characters|
### Group
- match.group (): The group () method returns parts of the string that match the pattern.
    ```
        import re string = '39801 356, 2102 1111' pattern = '(\d{3}) (\d{2})'
        
        match = re.search(pattern, string)
        
        if match: 
            print(match.group()) 
        else:
            print("No match")
    ```
    Output: 
    ```
    801 35
    ```
    Here, the match variable contains the match object.

    We have pattern (\ d {3}) (\ d {2}) divided into two small groups (\ d {3}) and (\ d {2}). You can get part of the string corresponding to the subgroups in this parenthesis as follows:
    ```
    >>> match.group(1)
    '801'
    
    >>> match.group(2)
    '35'
    
    >>> match.group(1, 2)
    ('801', '35')
    
    >>> match.groups()
    ('801', '35')
    ```





