from typing import List

Vector = List[float]


# A type alias in Python 3; makes the interpreter treat Vector and List[float] as interchangeable equivalents

class Word:
    def __init__(self, text: str, vector: Vector) -> None:
        # Python 3 optionally allows declaring the return type by inserting "->"
        self.text = text
        self.vector = vector


def vector_len(v: Vector) -> float:
    # Python 3 optionally allows declaring the parameter type by inserting
    # the type after a colon

    # The length of a vector is the square root of the sum of
    # each of its component squared
    # Function returns a floating point number
    return math.sqrt(sum([x * x for x in v]))


def dot_product(v1: Vector, v2: Vector) -> float:
    assert len(v1) == len(v2), "Lengths of vectors are unequal."
    # The assert statement evaluates the succeeding expression and 
    # raises an AssertionError exception when the assertion fails
    # The specified message will be printed in case of a failure

    # len(v1) does not invoke the vector_len function defined above
    # It simply returns the number of components in v1

    # The dot product equals the sum of each component in v1 multiplied
    # by the corresponding component in v2 at the same index
    return sum([x * y for (x, y) in zip(v1, v2)])


def cosine_similarity(v1: Vector, v2: Vector) -> float:
    # The cosine of the angle between v1 and v2 equals their dot product
    # divided by the product of their lengths (as in Euclidean norm)

    return dot_product(v1, v2) / (vector_len(v1) * vector(v2))


def sorted_by_similarity(words: List[Word], base_vector: Vector) \
        -> List[tuple]:
    """ List[Word] refers to the Word class defined above, which contains the word vector's components represented as a list of floating point numbers,
    along with the word itself.
    base_vector is simply a given word represented as floating point numbers, which the function compares each target word against to yield a ranking
    of similarity. """

    # Returns a list of tuples in the form of cosine similarity followed by the output word itself
    # List is sorted by cosine similarity, from most to least similar
    tuple_list = [(cosine_similarity(base_vector, w.vector), w) for w in words]

    """ Python 3 contains two sort functions:
    sort(), which modifies the original list in-place
    sorted(), which takes an iterable as input and returns a newly-created list upon sorting
    The second kind is used for the purpose of the sorted_by_similarity function.
    The parameter "key" is defined as an anonymous function, lambda, with a single argument t, the list of tuples passed in as the preceding parameter.
    t[0] indicates the lambda function returns the first element in each tuple in the list, which becomes the key for sorting.
    Enabling the reverse option makes the list sorted in descending order, which matches the order of most to least similar. """

    return sorted(tuple_list, key=lambda t: t[0], reverse=True)
