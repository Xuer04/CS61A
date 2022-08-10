n = 9

def make_adder(n):
    return lambda k: k + n

add_ten = make_adder(n+1)
result = add_ten(n)

"""
Q & A :
Q1: In the Global frame, the name add_ten points to a function object. What is the intrinsic name of that function object, and what frame is its parent?
Q2: What name is frame f2 labeled with (add_ten or λ)? Which frame is the parent of f2?
Q3: What value is the variable result bound to in the Global frame?

A1: The intrinsic name of the function object that add_ten points to is λ (specifically, the lambda whose parameter is k). The parent frame of this lambda is f1.
A2: f2 is labeled with the name λ the parent frame of f2 is f1, since that is where λ is defined.
A3: The variable result is bound to 19.
"""

