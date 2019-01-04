def timeout(timeout_seconds):
    def decorator(function):
        msg = 'Function (%s) used too much time (%s sec)' % (function.__name__, timeout_seconds)

        def handler(signum, frame):
            """If the signum event happens, a TimeoutError is raised"""
            raise TimeoutError(msg)
        def _f(*args, **kwargs):
            signal.alarm(0)
            old = signal.signal(signal.SIGALRM, handler) #Store the default handler of SIGALRM
            signal.alarm(timeout_seconds) #Seconds before SIGALRM signal is set
            try:
                #Will go to finally block when SIGALRM is set
                # after timeout_seconds nr of seconds
                #because SIGLRM raises TimeoutError
                function_result = function(*args, **kwargs) 
            finally:
                signal.signal(signal.SIGALRM, old) # Reset handler to default
            signal.alarm(0) #Reset signal to default
            return function_result
        _f.__name__ = function.__name__
        return _f
    return decorator
