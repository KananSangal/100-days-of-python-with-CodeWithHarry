## Python Learning Journey: Day 11 Summary

### Q1: What is a String in Python?

**A:** A string is a sequence or array of textual data wrapped in either single quotes (`'`) or double quotes (`"`). Python treats everything inside those quotes as a series of Unicode characters.

```python
name = "Harry"
print("Hello, " + name)  # Combining strings using the + operator

```

### Q2: How do you handle quotes *inside* a string without breaking the code?

**A:** Aside from using escape sequences (`\"`), a clean trick is to alternate your outer and inner quotes. If your text contains double quotes, wrap the whole string in single quotes (and vice versa):

```python
# No syntax errors because the outer quotes are single quotes
print('He said, "I want to eat an apple".')

```

### Q3: How do we create multi-line strings?

**A:** If you need a string to span across multiple lines, you wrap the entire block in triple single quotes (`'''`) or triple double quotes (`"""`). This preserves all the line breaks exactly how you type them.

### Q4: What does it mean that a string is an "array of characters"?

**A:** It means Python assigns a positional number—called an **index**—to every single character in the string, starting from **0**. You can pull out individual characters using square brackets `[]` containing that index number.

```python
name = "Harry"
print(name[0])  # Outputs: H
print(name[1])  # Outputs: a

```

### Q5: How can we inspect every character in a string automatically?

**A:** Because strings are sequences, you can use a `for` loop to step through them character by character. The loop will automatically start at index `0` and stop when it hits the end of the string:

```python
name = "Harry"

# This reads: "For every single letter in the variable name, print it"
for character in name:
    print(character)

```

### Output:

```text
H
a
r
r
y

```
