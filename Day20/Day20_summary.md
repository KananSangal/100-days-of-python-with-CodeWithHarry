## Python Learning Journey: Day 20 Summary

### Q1: What is a Function in Python and why do we use them?

**A:** A function is a reusable block of self-contained code designed to perform a specific task. As programs grow large and complex, functions help break the codebase down into smaller, modular chunks. This prevents code repetition (the DRY principle: *Don't Repeat Yourself*) and makes the entire program structure neat and organized.

### Q2: What is the difference between Built-in and User-defined functions?

**A:** Python splits functions into two main categories:

* **Built-in Functions:** Pre-coded functions that come bundled directly inside Python. You can use them immediately without defining them yourself (e.g., `print()`, `len()`, `type()`, `max()`, `sum()`).
* **User-defined Functions:** Custom functions created manually by the programmer to handle unique, specific workflows tailored to their project's requirements.

### Q3: How do you define and structurally layout a function in Python?

**A:** You declare a function using the `def` keyword, followed by a unique function name, parentheses `()` for optional inputs, and a colon `:`. The code statements inside the function must be indented to show they belong to that function's scope.

```python
# Defining a user-defined function
def function_name(parameters):
    # Core logic goes here
    pass  # 'pass' acts as a placeholder to prevent empty block errors

```

### Q4: What is the difference between defining a function and calling a function?

**A:** * **Defining a function:** This is merely writing the layout blueprint. Python reads it and stores the instructions in memory but **does not execute** the code inside it yet.

* **Calling a function:** This is triggering the function to run. You do this by writing the function's name followed by parentheses containing any required values.

```python
# 1. Definition (Blueprint created)
def greet_user(fname, lname):
    print("Hello,", fname, lname)

# 2. Execution Call (The code runs now)
greet_user("Sam", "Wilson")  # Outputs: Hello, Sam Wilson

```

### Q5: What are the golden rules for naming a function?

**A:** Function naming rules follow the exact same guidelines as naming variables (Day 6):

1. Names must start with a letter (`a-z`, `A-Z`) or an underscore (`_`).
2. Names cannot start with a number (`0-9`).
3. Names can only contain alphanumeric characters and underscores (`a-z`, `A-Z`, `0-9`, and `_`).
4. Names are case-sensitive (`calculate_total` and `Calculate_Total` are different).
5. You cannot use Python reserved keywords (like `def`, `if`, `while`, `print`) as function names.