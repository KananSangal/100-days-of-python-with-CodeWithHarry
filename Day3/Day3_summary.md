## Python Learning Journey: Day 3 Summary

### Q1: What exactly is a "Module" in Python?

**A:** A module is a pre-written code library that you can import into your project. Instead of writing everything from scratch, you "borrow" someone else's code to add advanced features—like data analysis or web scraping—instantly.

### Q2: What is the difference between Built-in and External modules?

**A:** Python splits its modules into two categories:

* **Built-in Modules:** These ship right out of the box with Python (like `random` or `math`). You don't need to download anything; you just `import` them and go.
* **External Modules:** These are third-party tools written by the community. They don't come with Python automatically, so you have to download and install them yourself.

### Q3: What is `pip` and how do you use it?

**A:** `pip` is Python's official package manager. Think of it like an App Store for code. If you want to install an external library—for example, the popular data tool **pandas**—you open your terminal and run:

```bash
pip install pandas

```

### Q4: How do you actually use an installed module in a script?

**A:** You bring it into your file using the `import` keyword. Once imported, you can use any of its built-in tools. For example, using `pandas` to read a data file looks like this:

```python
import pandas

# Reading a CSV data file using pandas
df = pandas.read_csv('words.csv')
print(df)

```

