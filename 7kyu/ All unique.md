# CodeWars Python Solution

---

## All Unique 

Write a program to determine if a string contains only unique characters. 
Return true if it does and false otherwise.

The string may contain any of the 128 ASCII characters. 
Characters are case-sensitive, e.g. 'a' and 'A' are considered different characters.


---

### Solution
```python
def has_unique_chars(s):
    return len(s) == len(set(s))
```

---


[See on CodeWa,com](https://www.codewars.com/kata/553e8b195b853c6db4000048)