#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.index("object-oriented programming"):str.index(" language")]
print(str + " with Python")
