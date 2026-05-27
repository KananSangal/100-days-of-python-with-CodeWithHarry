## Python Learning Journey: Day 14 Summary

### Q1: What is the purpose of conditional statements in programming?

**A:** Conditional statements allow a program to evaluate specific expressions to check if they are `True` or `False`. Based on the result, the program forks and runs a specific block of code while completely ignoring the alternative paths.

### Q2: How does a standard `if-else` block function?

**A:** It handles binary choices. If the condition passed to the `if` statement evaluates to `True`, the code inside the `if` block runs. If it evaluates to `False`, the program skips the `if` block entirely and runs the code nested inside the `else` block instead.

```python
apple_price = 210
budget = 200

# Since 210 <= 200 is False, the 'if' block is skipped
if apple_price <= budget:
    print("Add apples to cart.")
else:
    print("Do not add apples to cart.")  # This executes

```

### Q3: When do we use `elif` statements?

**A:** We use `elif` (short for *else if*) when we need to evaluate multiple sequential conditions. Python checks them in order from top to bottom. The moment it finds a condition that evaluates to `True`, it executes that specific block and immediately exits the entire conditional structure, ignoring any remaining `elif` or `else` checks.

```python
num = 0
if num < 0:
    print("Negative.")
elif num == 0:
    print("Zero.")      # Found True! This runs, structure exits.
else:
    print("Positive.")

```

### Q4: What are Nested Conditional Statements?

**A:** Nesting means placing an `if`, `if-else`, or `elif` block *inside* another existing conditional block. This allows you to check for secondary conditions only after a primary condition has already passed.

```python
num = 18
if num > 0:  # Primary check passed
    # Secondary nested checks begin
    if num <= 10:
        print("Between 1-10")
    elif num > 10 and num <= 20:
        print("Between 11-20")  # This executes

```

### Q5: What is the role of Indentation in Python conditions?

**A:** Unlike other languages that use curly braces `{}`, Python relies entirely on whitespace indentation (usually 4 spaces or a tab) to define the scope of a code block. If code is indented under an `if` statement, it belongs to that condition. Dropping back to the original margin tells Python the conditional block has ended.
