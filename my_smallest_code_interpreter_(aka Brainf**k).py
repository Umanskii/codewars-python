"""
Inspired from real-world Brainf**k, we want to create an interpreter of that language which will support the following instructions:

> increment the data pointer (to point to the next cell to the right).
< decrement the data pointer (to point to the next cell to the left).
+ increment (increase by one, truncate overflow: 255 + 1 = 0) the byte at the data pointer.
- decrement (decrease by one, treat as unsigned byte: 0 - 1 = 255 ) the byte at the data pointer.
. output the byte at the data pointer.
, accept one byte of input, storing its value in the byte at the data pointer.
[ if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.
] if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.
The function will take in input...

the program code, a string with the sequence of machine instructions,
the program input, a string, possibly empty, that will be interpreted as an array of bytes using each character's ASCII code and will be consumed by the , instruction
... and will return ...

the output of the interpreted code (always as a string), produced by the . instruction.
Implementation-specific details for this Kata:

Your memory tape should be large enough - the original implementation had 30,000 cells but a few thousand should suffice for this Kata
Each cell should hold an unsigned byte with wrapping behavior (i.e. 255 + 1 = 0, 0 - 1 = 255), initialized to 0
The memory pointer should initially point to a cell in the tape with a sufficient number (e.g. a few thousand or more) of cells to its right. For convenience, you may want to have it point to the leftmost cell initially
You may assume that the , command will never be invoked when the input stream is exhausted
Error-handling, e.g. unmatched square brackets and/or memory pointer going past the leftmost cell is not required in this Kata. If you see test cases that require you to perform error-handling then please open an Issue in the Discourse for this Kata (don't forget to state which programming language you are attempting this Kata in).
"""
def brain_luck(code, program_input):
    from collections import defaultdict
    input1 = [ord(i) for i in program_input]
    cell = defaultdict(int)
    res = run(code, cell, input1, 0)
    return ''.join([chr(i) for i in res])
    
def run(code, cell, input1, i):
    n = 0
    while n < len(code):
        if code[n] == ',':
            cell[i] = input1.pop()
            n += 1
        elif code[n] == '.':
            input1.append(cell[i])
            n += 1
        elif code[n] == '>':
            i += 1
            n += 1
        elif code[n] == '<':
            i -= 1
            n += 1
        elif code[n] == '+':
            cell[i] = 0 if cell[i] == 255 else cell[i] + 1
            n += 1
        elif code[n] == '-':
            cell[i] = 255 if cell[i] == 0 else cell[i] - 1
            n += 1
        elif code[n] == '[':
            if cell[i] == 0:
                mark = 0
                m = n
                while True:
                    m += 1
                    if code[m] == '[':
                        mark += 1
                    elif code[m] == ']' and mark:
                        mark -= 1
                    elif code[m] == ']' and not mark:
                        n = m + 1
                        break
            else:
                n += 1
                pass
        elif code[n] == ']':
            if cell[i] == 0:
                n += 1
                pass
            else:
                mark = 0
                m = n
                while True:
                    m -= 1
                    if code[m] == ']':
                        mark += 1
                    elif code[m] == '[' and mark:
                        mark -= 1
                    elif code[m] == '[' and not mark:
                        n = m + 1
                        break
    return input1