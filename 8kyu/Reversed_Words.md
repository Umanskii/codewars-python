# CodeWars Python Solutions

---

## Reversed Words

Complete the solution so that it reverses all of the words within the string passed in.

Examples:

```python
reverseWords("The greatest victory is that which requires no battle")
# should return "battle no requires which that is victory greatest The"
```


---

### Given Code


```python
def reverseWords(str):
    pass
```

---

### Solution 1


```python
def reverseWords(str):
    return " ".join(w for w in str.split()[::-1])
```


-----

### Solution 2


```python
def reverse_words(s):
    parts = s.split()
    res = ""
    for i in reversed(range(len(parts))):
        res += parts[i]
        if i != 0:
            res += " "
    return res
```


---
[See on CodeWars.com](https://www.codewars.com/kata/51c8991dee245d7ddf00000e/)
