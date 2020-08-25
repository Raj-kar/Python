# also RED - GREEN test , [TDD - test driven development]
# Red means error, Green means no error !

def add(num1, num2):
    """Add two number and returns !
    >>> add(1, 2)
    3
    >>> add(200,300)
    500
    >>> add(8, 'hi')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>> add('hi', 8)
    Traceback (most recent call last):
        ...
    TypeError: can only concatenate str (not "int") to str
    >>> add('hi','hi')
    'hihi'
    """
    return num1 + num2
    # return num1 * num2 [test case fails]


def doubles(values):
    """ Double the values and return !
    >>> doubles([1, 2, 3, 4])
    [2, 4, 6, 8]
    >>> doubles([])
    []
    >>> doubles(['a', 'b'])
    ['aa', 'bb']
    >>> doubles((['a', 1, 'b']))
    ['aa', 2, 'bb']
    >>> doubles(1,2)
    Traceback (most recent call last):
        ...
    TypeError: doubles() takes 1 positional argument but 2 were given
    """
    return [2 * num for num in values]


def say_hello():
    """Print Hello !
    >>> say_hello()
    'hello'
    >>> say_hello(9)
    Traceback (most recent call last):
        ...
    TypeError: say_hello() takes 0 positional arguments but 1 was given
    """
    return 'hello'
    # return "Hello"    # that's wrong, because we expected 'hello' and "hello",


def say_true():
    """Return True!
    >>> say_true()
    True
    >>> say_true(9)
    Traceback (most recent call last):
        ...
    TypeError: say_true() takes 0 positional arguments but 1 was given
    """
    return True


def cubes(val):
    """ Returns the cube of a number !
    >>> cubes(2)
    8
    >>> cubes()
    Traceback (most recent call last):
        ...
    TypeError: cubes() missing 1 required positional argument: 'val'
    >>> cubes('hi')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
    >>> cubes(1,2)
    Traceback (most recent call last):
        ...
    TypeError: cubes() takes 1 positional argument but 2 were given
    """
    return val ** 3

# you can put anything in place of ...(dot dot dot) , here ...(dot dot dot) refers to there extra stuff that doesn't
# matter ! compiler checks the 1st and last line
