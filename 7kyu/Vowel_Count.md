# CodeWars Python Solutions

---

## Vowel Count

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.

---

### Given Code


```python
def getCount(inputStr):
    num_vowels = 0
    # your code here

    return num_vowels
```

---

### Solution 1


```python
def getCount(inputStr):
    return sum([inputStr.count(c) for c in "aeiou"])
```


---


### Solution 2

```python
def getCount(inputStr):
    num_vowels = 0
    for vow in ["a", "e", "i", "o", "u"]:
        num_vowels += inputStr.count(vow)
    return num_vowels
```


---


### Solution 3
```python
def get_count(sentence):
    vowels = 'aeiou'
    vowels_count = 0
    for char in sentence:
        if char.lower() in vowels:
            vowels_count += 1
    return vowels_count
```

---


[See on CodeWars.com](https://www.codewars.com/kata/54ff3102c1bad923760001f3)
