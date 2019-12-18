import inspect

def check_types(*correct_types):
    """
    Decorator for checking types of function arguments
    """
    def is_method(func):
        if inspect.getargspec(func).args[0] == 'self':
            return True
        else: 
            return False

    def decorator(func):
        def wrapper(*inputs):
            if is_method(func):
                inputs_copy = (inputs[1:])
            else:
                inputs_copy = inputs
            for correct_type, inp in zip(correct_types, inputs_copy):
                if correct_type is not type(inp) and type(inp) is not type(None) :
                    raise TypeError('See documentation for argument types')
            wrapper.__name__ = func.__name__
            return func(*inputs)
        return wrapper
    return decorator



if __name__=='__main__':
    @check_types(int, float, list)
    def test(a, b, c):
        return a, b, c

    class A:
        @check_types(int, float, list)
        def method(self, a, b, c):
            return a, b, c

    test(1, 2.0, [1])
    A().method(1, 2.0, [1])





