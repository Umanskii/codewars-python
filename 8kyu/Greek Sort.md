# CodeWars Python Solution

---

## Greek Sort - 8kyu

Write a comparator for a list of phonetic words for the letters of the greek alphabet.

### A comparator is:

"a custom comparison function of two arguments (iterable elements) which should 
return a negative, zero or positive number depending on whether the first argument 
is considered smaller than, equal to, or larger than the second argument"

(source: https://docs.python.org/2/library/functions.html#sorted)

The greek alphabet is preloded for you as greek_alphabet:

```python
greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')
```

### Examples
```python
greek_comparator('alpha', 'beta')   <  0
greek_comparator('psi', 'psi')      == 0
greek_comparator('upsilon', 'rho')  >  0
```

### Solution

```python
def greek_comparator(lhs, rhs):
    return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)
```

---

[See on CodeWars.com](https://www.codewars.com/kata/56bc1acf66a2abc891000561)

