## Python Learning Journey: Day 6 Summary

### Q1: What is a variable in Python?

**A:** A variable is simply a named container used to store data in the computer's memory. Just like a kitchen jar might hold salt, sugar, or flour, a Python variable holds values like numbers, text, or logic so you can reference and change them easily later.

```python
a = 1        # Container 'a' holds an integer
c = "Harry"  # Container 'c' holds text

```

### Q2: Why are Data Types important?

**A:** A data type tells Python exactly what *kind* of value is inside a variable. This is crucial because Python needs to know what operations it is allowed to perform. For instance, you can mathematically add two numbers, but you cannot mathematically subtract text from a number. You can check any variable's type using the built-in `type()` function:

```python
a = 1
print(type(a))  # Outputs: <class 'int'>

```

### Q3: What are the primary built-in Data Types in Python?

**A:** Python groups data into several major categories:

1. **Numeric Data:**
* `int`: Whole numbers (`3`, `-8`)
* `float`: Decimal numbers (`7.349`, `-9.0`)
* `complex`: Numbers with real and imaginary parts (`6 + 2j`) *Note: Python uses 'j' instead of 'i' for complex numbers.*


2. **Text Data (`str`):** Strings of text wrapped in quotes (`"Hello World!!!"`).
3. **Boolean Data (`bool`):** True/False logic states (`True` or `False`).

### Q4: What is the difference between a List, a Tuple, and a Dictionary?

**A:** These are "collection" data types used to hold multiple items together, but they behave differently:

* **List (`list`):** An ordered, changeable (**mutable**) collection wrapped in square brackets `[]`. It can hold different data types, including other lists.
* **Tuple (`tuple`):** An ordered, unchangeable (**immutable**) collection wrapped in parentheses `()`. Once created, you cannot modify its elements.
* **Dictionary (`dict`):** An unordered collection of **key:value** pairs wrapped in curly braces `{}`. It acts like a real-world dictionary where you look up a "key" (word) to find its "value" (definition).

```
# Quick examples of collection types
my_list = [1, "apple", 3.4]
my_tuple = ("sparrow", "hawk")
my_dict = {"name": "Sakshi", "age": 20}

```

---

The distinction between mutable (Lists) and immutable (Tuples) is a favorite topic in coding interviews!