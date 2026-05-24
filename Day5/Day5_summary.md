## Python Learning Journey: Day 5 Summary

### Q1: What is a comment in Python, and why do we use them?

**A:** A comment is a piece of text inside your code file that Python completely ignores when running the program. Programmers use them for two main reasons:

1. **Documentation:** Leaving notes to explain what a specific block of code does.
2. **Testing:** Temporarily hiding a line of code from running without deleting it (by putting a `#` in front of it).

### Q2: How do you write single-line vs. multi-line comments?

**A:** Python gives you a couple of ways to do this:

* **Single-line:** Place a `#` at the beginning of the line. Everything after it on that line is ignored.
* **Multi-line:** You can either put a `#` at the start of every single line, or wrap the block of text inside triple quotes (`""" comment here """`).

### Q3: What is an Escape Sequence Character?

**A:** An escape sequence is a backslash (`\`) followed by a specific character. It tells Python to treat the next character as text instead of code. For example, if you want to put double quotes inside a string that already uses double quotes, you use `\"` so Python doesn't get confused and crash:

```python
# This keeps Python from breaking over the internal quotes
print("This will \"execute\" flawlessly")

```

Other common ones include `\n` to force a new line.

### Q4: What are the hidden, advanced parameters inside the `print()` function?

**A:** While we usually just pass text into `print()`, it actually has optional settings we can tweak:

* **`sep` (Separator):** Dictates how to separate multiple items passed into one print statement. The default is a blank space (`' '`), but you can change it to a hyphen, comma, etc.
* **`end`:** Dictates what gets printed at the very end of the statement. The default is a newline character (`\n`), which drops the cursor to the next line automatically. You can change this to keep the next print statement on the exact same line.

Also, # is known as "Pound" and ~ is known as "Tilde" in Programming Language.
Ctrl/Cmd + / will comment or un-comment any line or grp of line.
Alt + Arrow keys can move any line.