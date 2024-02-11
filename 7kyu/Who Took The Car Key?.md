# CodeWars Python Solution

---

## Who Took The Car Key?

DESCRIPTION:
You woke up from a massive headache and can't seem to find your car key. You find a note with a clue that says:

"If you're reading this then I have left the state and am well on my way to freedom. Just to make things interesting, I have also provided something for you to track me with. Let the chase begin..."

## Given an array of binary numbers, figure out and return the culprit's message to find out who took the missing car key.

['01000001', '01101100', '01100101', '01111000', '01100001', '01101110', '01100100', '01100101', '01110010'] => 
'Alexander'

---

### Solution

```python
def who_took_the_car_key(m):
    r = []
    for i in m:
        i = int(i, 2)
        r.append(chr(i))
    return ''.join(r)
```

### Solution 2

```python
def who_took_the_car_key(message):
    return "".join(chr(int(c, 2)) for c in message)
```


----


[See on CodeWars.com](https://www.codewars.com/kata/57a23c2acf1fa514d0001034)