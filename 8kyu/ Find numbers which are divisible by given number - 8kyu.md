# CodeWars Python Solution

---

##  Find numbers which are divisible by given number - 8kyu

Complete the function which takes two arguments and returns all numbers which are 
divisible by the given divisor. First argument is an array of numbers and the second 
is the divisor.

### Example(Input1, Input2 --> Output)
[1, 2, 3, 4, 5, 6], 2 --> [2, 4, 6]


### Solution
```python
def divisible_by(numbers, divisor):
    return [x for x in numbers if x%divisor == 0]
```


---

[See on Codewars.com](https://www.codewars.com/kata/55edaba99da3a9c84000003b)