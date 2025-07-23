import pytest
from program1 import fibonacci

def TestGetFib():
    assert fibonacci(0) == "botato"
print("Testa comportamento com n < 1")

assert fibonacci(0) == [0,1]
#assert fibonacci(0) == "adf"



#if fibonacci(0) == [0,1]: #start of the sequence
#    print("test concluido")
#else:
#    print("erro")
#
#if fibonacci(1) == [0,1,1]: #start of the sequence
#    print("test concluido")
#else:
#    print("erro")
#
#if fibonacci(5) == [0,1,1,2,3,5,8]: #start of the sequence
#    print("test concluido")
#else:
#    print("erro")

