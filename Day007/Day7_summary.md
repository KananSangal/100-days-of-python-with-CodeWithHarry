## Python Learning Journey: Day 7 Summary

### Q1: What are Arithmetic Operators in Python?

**A:** Arithmetic operators are symbols used to perform standard mathematical calculations. While addition (`+`), subtraction (`-`), and multiplication (`*`) work exactly as expected, Python introduces specific symbols for division and powers:

* ``** (Exponential):** Raises a number to a power (e.g., `53` means $5^3 = 125$).
* **`/` (Division):** Standard division that always results in a decimal floating-point number (e.g., `5/2` gives `2.5`).

### Q2: What is the difference between Modulus (`%`) and Floor Division (`//`)?

**A:** These two operators are incredibly useful for handling division leftovers:

* **Modulus (`%`):** Divides two numbers but *only* returns the **remainder**. For example, `15 % 7` is `1` because 7 goes into 15 twice with a remainder of 1.
* **Floor Division (`//`):** Divides two numbers and rounds the result *down* to the nearest whole integer, discarding the remainder entirely. For example, `15 // 7` is `2`.

### Q3: How do we construct a basic calculator script using these operators?

**A:** By storing numbers in variables, executing the operations, and printing the results dynamically. Using the hidden parameters from Day 5, we can pass multiple variables directly into a `print()` statement to make the output highly readable:

```python
# Initializing inputs
n = 15
m = 7

# Performing calculations
addition = n + m
modulus = n % m
floor_div = n // m

# Formatting and printing outputs clearly
print("Addition of", n, "and", m, "is", addition)
print("Modulus (Remainder) of", n, "and", m, "is", modulus)
print("Floor Division (Whole Part) of", n, "and", m, "is", floor_div)

```

