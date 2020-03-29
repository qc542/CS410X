from typing import List

Vector = List[float]

class Word:
    def __init__(self, text: str, vector: Vector) -> None:
        # Python allows making function annotation by inserting "->"
        self.text = text
        self.vector = vector

def vector_len(v: Vector) -> float:
    # The length of a vector is the square root of the sum of
    # each of its component squared
    # Function returns a floating point number
    return math.sqrt(sum([x*x for x in v]))

def dot_product(v1: Vector, v2: Vector) -> float:
    assert len(v1) == len(v2), "Lengths of vectors are unequal."
    # The assert statement evaluates the succeeding expression and 
    # raises an AssertionError exception when the assertion fails
    # The specified message will be printed in case of a failure
    
    # len(v1) does not invoke the vector_len function defined above
    # It simply returns the number of components in v1

    # The dot product equals the sum of each component in v1 multiplied
    # by the corresponding component in v2 at the same index
    return sum([x*y for (x,y) in zip(v1,v2)]) 

def cosine_similarity(v1: Vector, v2: Vector) -> float:
    # The cosine of the angle between v1 and v2 equals their dot product
    # divided by the product of their lengths (as in Euclidean norm)

    return dot_product(v1,v2) / (vector_len(v1) * vector(v2))
