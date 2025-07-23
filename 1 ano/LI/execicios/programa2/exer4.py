import pytest
import program1

text = "12335899"
print("\n inserting String \n")
print("waitng for error massage")
assert program1.fibonacci(text) == "ERROR THE NUBER ISNT INT TYPE"

n = 12
print("\n inserting Integer \n")
print("waitng for VALID massage")
program1.fibonacci(n)



#pytest exer4.py  in the terminal
