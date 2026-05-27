## Python Learning Journey: Day 10 Summary

### Q1: How do we capture user inputs in Python?

**A:** We use the built-in `input()` function. When Python hits this function, it pauses the execution of the script and waits for the user to type something in the console and hit Enter. The typed value is then returned and should be captured inside a variable:

```python
# Pauses and waits for the user to type something
user_response = input() 

```

### Q2: What is the most critical rule to remember about the `input()` function?

**A:** The `input()` function **always returns data as a string (`str`)**, no matter what the user types. Even if a user enters `45`, Python reads it as the text `"45"`.

### Q3: How do we handle numerical inputs from a user?

**A:** Because inputs default to strings, you must combine the `input()` function with **explicit typecasting** (from Day 9) if you intend to perform mathematical operations. You can wrap the entire input statement inside a conversion function like `int()` or `float()`:

```python
# Converts the string input into an integer immediately
age = int(input())

# Converts the string input into a decimal number
price = float(input())

```

> **Warning:** If the user types text (like `"banana"`) when you are expecting an integer, the program will crash with a `ValueError`.

### Q4: How can we prompt the user with a message before they type?

**A:** You can pass a string directly inside the parentheses of the `input()` function. This serves as a prompt or a question, making the console interface much cleaner and more user-friendly:

```python
# Displaying a prompt message while capturing the input
username = input("Enter your name: ")
print("Welcome to Python,", username)

```

### Output Example:

```text
Enter your name: Harry
Welcome to Python, Harry

```

