import signal

def timeout(timeout_seconds):
    def decorator(function):
        msg = 'Function (%s) used too much time (%s sec)' % (function.__name__, timeout_seconds)

        def handler(signum, frame):
            """If the signum event happens, a TimeoutError is raised"""
            raise TimeoutError(msg)

        def signal_handler(*args, **kwargs):
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
            signal_handler.__name__ = function.__name__
            return function_result
        return signal_handler 
    return decorator

if __name__=='__main__':
    import time
    @timeout(2)
    def test():
        for i in range(10):
            print(i)
            time.sleep(1)

    def do_something():
        pass
    try:
        test()
    except TimeoutError as e:
        print(e)
        do_something()

    # print(test
