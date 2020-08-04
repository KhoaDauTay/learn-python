# Section 07: Functional Programming in Python
## Lesson overview
- Functional programming in python
- Lambdas in Python
- The map() Function
- Filtering
### Functional programming
- Functional programming is a programming paradigm in which we try to bind everything in pure mathematical functions style. 
    - It is a declarative type of programming style.
    - Its main focus is on “what to solve” in contrast to an imperative style where the main focus is “how to solve“.
    - It uses expressions instead of statements.
    - An expression is evaluated to produce a value whereas a statement is executed to assign variables.
- Python too supports Functional Programming paradigms without the support of any special features or libraries.
    Pure Functions
    - As Discussed above, pure functions have two properties.
    - It always produces the same output for the same arguments. For example, 3+7 will always be 10 no matter what.
    - It does not change or modifies the input variable.

    Example:
    ```
    def pure_func(List): 
        New_List = [] 
        for i in List: 
            New_List.append(i**2) 
        return New_List 
    Original_List = [1, 2, 3, 4] 
    Modified_List = pure_func(Original_List) 
    print("Original List:", Original_List) 
    print("Modified List:", Modified_List) 
    ```
    Output:
    ```
    Original List: [1, 2, 3, 4]
    Modified List: [1, 4, 9, 16]
    ```
### Lambdas in Python
- A lambda function is a small anonymous function.
- A lambda function can take any number of arguments, but can only have one expression.
- Syntax : ```lambda arguments : expression```
- The expression is executed and the result is returned
- Example:
    ```
    x = lambda a : a + 10
    print(x(5))
    ```

### Map in Python
- The map() function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.
- Syntax : ```map(function, iterables)```
    Example:
    ```
    list_old = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]
    list_new = list(map(lambda a: a*2 , list_old))
    print(list_old)
    ```
    Output:
    ```
    [20, 18, 16, 14, 12, 2, 4, 6, 8, 10]
    ```
### Filters in Python
- The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
- Syntax : ```filter(function, iterable)```
    Example:
    ```
    ages = [5, 12, 17, 18, 24, 32]
    def myFunc(x):
    if x < 18:
        return False
    else:
        return True
    adults = filter(myFunc, ages)
    for x in adults:
    print(x)
    ```
    Output:
    ```
    18
    24
    32
    ```
### Generators in Python
- Generator is a great means to create an infinite stream of data. These infinite streams do not need to be stored entirely in memory because the generator only generates one element at a time, so it can represent infinite data flow.
    ```
    def all_even():
        n = 0f
        while True:
            yield n
            n += 2
    ```
### Coding challenge 9
- Assume you want to build two functions for discounting products on a website.
    - Function number 1 is for student discount which discounts the current price to 10%.
    - Function number 2 is for additional discount for regular buyers which discounts an additional 5% on the current student discounted price.
- Depending on the situation, we want to be able to apply both the discounts on the products.

Design the above two mentioned functions and apply them both simultaneously on the price.
### Coding challenge 9 solution
    ```
    def student_discount(price):
        price = price - (price * 10) / 100
        return price
    
    def additional_discount(newprice):
        newprice = newprice - (newprice * 5) / 100
        return newprice
    
    selling_price = 100
    
    #applying both discounts simultaneously
    
    print(additional_discount(student_discount(selling_price)))
    ```
### Coding challenge 10
- Calculate the value of mathematical expression x*(x+5)^2 where x= 5 using lambda expression.
### Coding challenge 10 solution
    ```
    result = (lambda x: x*(x+5)**2)(5)
    print(result)
    ```
### Coding challenge 11
- Consider a list in Python which includes prices of all the items in a store.
- Build a function to discount the price of all the products by 10%.
- Use map to apply the function to all the elements of the list so that all the product prices are discounted
### Coding challenge 11 solution
    ```
    def discount(price):
        price = price - (price * 10) / 100
        return price
    
    product_prices = [100, 200, 300, 400, 500]
    
    updated_prices = list(map(discount,product_prices))
    
    print(updated_prices)
    ```

