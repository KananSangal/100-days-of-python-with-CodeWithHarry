## Python Learning Journey: Day 18 Summary

### Q1: What is a `while` loop and how does it differ from a `for` loop?

**A:** A `while` loop is a **condition-controlled loop**. While a `for` loop is usually built to run a predetermined number of times, a `while` loop executes its block of code continuously *while* a given condition evaluates to `True`. The moment that condition flips to `False`, the loop instantly stops.

```python
count = 5
# The loop keeps checking this condition before every single round
while count > 0:
    print(count)
    count = count - 1  # Crucial: Updating the counter

```

### Q2: What happens if you forget to update the condition variable inside a `while` loop?

**A:** You will create an **infinite loop**. Because the control variable never changes, the condition stays `True` permanently, and the program will run forever (or until your computer runs out of memory or you force-quit the terminal).

### Q3: How does the `else` statement work when paired with a `while` loop?

**A:** In Python, you can attach an `else` block directly to a loop. The code inside the `else` block executes **exactly once**, immediately after the loop's main condition successfully becomes `False` and the loop terminates naturally.

```python
x = 5
while x > 0:
    print(x)
    x = x - 1
else:
    print('Counter has hit 0!')  # Runs seamlessly after the loop finishes

```

### Q4: Does Python have a native `do-while` loop?

**A:** No, Python does not feature a built-in, native `do-while` keyword structure like C++ or Java. A standard `while` loop is an **entry-controlled loop** (checks the condition *before* running), whereas a `do-while` loop is an **exit-controlled loop** (runs the code first, then checks the condition at the end, guaranteeing it runs at least once).

### Q5: How do you emulate a `do-while` loop structure in Python?

**A:** You can mimic this exact behavior by intentionally creating an infinite loop using `while True:` to guarantee the code runs the first time. Inside the loop, after running your core logic, you insert an `if` condition paired with a `break` statement to exit the loop if the condition fails.

```python
# Emulating an exit-controlled do-while loop
while True:
    number = int(input("Enter a positive number: "))
    print(number)
    
    # Checking the exit condition at the very bottom of the loop
    if not number > 0:
        break  # Forces an immediate exit from the infinite loop

```