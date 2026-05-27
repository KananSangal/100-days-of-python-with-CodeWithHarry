## Python Learning Journey: Day 12 Summary

### Q1: How do we find out how many characters are in a string?

**A:** Python provides a built-in function called `len()`. It counts every character inside the string, including spaces, numbers, and punctuation marks, and returns the total as an integer.

```python
fruit = "Mango"
print(len(fruit))  # Outputs: 5

```

### Q2: What is String Slicing?

**A:** String slicing is the method of extracting a specific portion (or "slice") of a string by specifying a range of index positions. The basic syntax uses square brackets and a colon: `string[start_index : end_index]`.

> **Crucial Rule:** The `start_index` is **inclusive** (included in the slice), but the `end_index` is **exclusive** (excluded from the slice).

### Q3: How do the shorthand shortcuts for slicing work?

**A:** If you leave out the start or end index, Python automatically fills in the blanks:

* **Leaving out the start (`[:5]`):** Python assumes you want to start from the very beginning (index `0`).
* **Leaving out the end (`[5:]`):** Python assumes you want to go all the way to the very last character.

```python
pie = "ApplePie"
print(pie[:5])   # From start to index 4 -> Outputs: Apple
print(pie[5:])   # From index 5 to the end -> Outputs: Pie
print(pie[2:6])  # From index 2 to index 5 -> Outputs: pleP

```

### Q4: How does negative index slicing work?

**A:** Python allows you to count indices backward from the end of the string using negative numbers. The last character is index `-1`, the second-to-last is `-2`, and so on.

```python
pie = "ApplePie"
# Counts 8 characters backward from the end to find the start point
print(pie[-8:])  # Outputs: ApplePie

```

### Q5: Why can we use a `for` loop on a string?

**A:** Because strings are arrays, they are classified as **iterables**. This means Python knows how to look at them as a collection of separate elements, allowing a `for` loop to step through and extract each character one by one sequentially.