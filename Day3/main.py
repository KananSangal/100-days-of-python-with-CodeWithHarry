import pandas  # This is an example of external module
import hashlib  # This is an example of built in module

print("Hi")

# Dont worry about how to use these modules or FileNotFoundError because the CSV doesn't exist just yet!
pandas.read_csv("one.csv")
m = hashlib.sha256()