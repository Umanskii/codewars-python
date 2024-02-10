"""
Complete the function caffeineBuzz, which takes a non-zero integer as it's one argument.

If the integer is divisible by 3, return the string "Java".

If the integer is divisible by 3 and divisible by 4, return the string "Coffee"

If the integer is one of the above and is even, add "Script" to the end of the string.

Otherwise, return the string "mocha_missing!"

caffeineBuzz(1)   => "mocha_missing!"
caffeineBuzz(3)   => "Java"
caffeineBuzz(6)   => "JavaScript"
caffeineBuzz(12)  => "CoffeeScript"
"""

def caffeine_buzz(n): 
    if n%3==0 and n%4==0 and n%2==0: return 'CoffeeScript'
    if n%3==0 and n%2==0: return 'JavaScript'
    if n%3==0 and n%4==0: return 'Coffee'
    if n%3==0: return 'Java'
    else: return 'mocha_missing!'