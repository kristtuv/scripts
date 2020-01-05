def run_once(func):
    """
    Decorator checking if a method has been
    run before. Used for methods that will
    add duplicates in the datamaterial.
    """
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return func(*args, **kwargs)
        else:
            return None
    wrapper.has_run = False
    return wrapper

if __name__=='__main__':
    @run_once
    def test():
        print( 'Foo' )
    test()
    test()
