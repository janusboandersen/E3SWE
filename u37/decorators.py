"""
Example for using a decorator
"""


def check(f):
    """
    checks the function arguments and either returns a function with implemented checks
    """
    def inside(a, b):
        """
        The inside function is returned upon decoration. This inside function
        """
        if b == 0:
            print("Can't divide by zero.")
            return

        return f(a, b)
    return inside

@check
def div(a, b):
    return a / b

print( div(10, 3) )