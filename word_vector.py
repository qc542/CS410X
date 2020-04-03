from typing import List

Vector = List[float]
# A type alias in Python 3; makes the interpreter treat Vector and List[float] as interchangeable equivalents


class Word:
    def __init__(self, text: str, vector: Vector) -> None:
        # Python 3 optionally allows declaring the return type by inserting "->"
        self.text = text
        self.vector = vector


def load_vector(filename: str) -> dict:
    text_stream = io.open(filename, 'r', encoding = 'utf-8', errors = 'ignore'\
            , newline = '\n')
    n, d = text_stream.readline().split()

    """ The first line in the vector file says the total number of words
    included and the dimension of each vector, separated by a whitespace
    character. In the case of the 300-dimensional Wikinews vector file,
    the first line reads "999994 300", meaning it contains 999994 word 
    vectors, each of which contains 300 dimensions."""

    """ These two numbers are extraneous for the purpose of this function,
     but this first line of the vector file needs to be read so that the 
     text stream will move onto the next line, which contains the first 
     word vector in the file."""

    vector_dict = {}
    """ A Python dictionary in which each word entry is a key and a list 
    of the vector's components is the value."""

    for line in text_stream:
        items = line.rstrip().split(' ')
        """ Each line in the vector begins with a word entry, followed by 
        a single whitespace character and then the three-hundred values 
        for all of the particular vector's dimensions. Each value is also 
        followed by a single whitespace character.

        Running the for loop over the text stream breaks it down line by 
        line, which is pointed to by the string variable "line". The 
        rstrip method of a Python string removes all characters contained 
        in the argument. In this case, not passing an argument makes the 
        method remove all trailing whitespace. The split method breaks 
        down the string by referring to the argument as the delimiter 
        and returns a list of all consequent substrings. In this case 
        it returns a list in which the word entry is the first item 
        and the rest are components of the entry's vector."""

        vector_dict[items[0]] = map(float, items[1:])
        """ items[0] is the word entry. The map function type-casts 
        all following items in the list, which are vector components 
        represented as strings, to floating point numbers. """

    return vector_dict


def lookup_vector(w: str, vector_dict: dict) -> Vector:
    """ Given a word entry and a previously-generated dictionary as 
    the parameters, the function looks up the entry in the 
    dictionary and returns the correspond Vector object."""

    if w in vector_dict: return vector_dict[w]
    else:
        print("The word " + w + " could not be found in the \
                given dictionary.")
        return None
    """ vector_dict[w] is a list of floating numbers, which is 
    previously defined as equivalent to a Vector object."""

def construct_word(w: str, vector_dict: dict) -> Word:
    """ Given a word entry and a previously-generated dictionary as 
    the parameters, the function calls the lookup_vector function 
    and creates an instance of the Word class if the entry is 
    found."""

    vec = lookup_vector(w, vector_dict)
    if not vec:
        word_obj = Word(w, vec)
    else: return None
    """ If lookup_vector does not return None, instantiate a Word 
    object with the given word and the Vector object returned. If 
    lookup_vector returned None, an error message would have been 
    printed, so there is no need to print again here."""


def vector_len(v: Vector) -> float:
    # Python 3 optionally allows declaring the parameter type by inserting
    # the type after a colon

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

    return sorted(tuple_list, key=lambda t:t[0], reverse=True)
