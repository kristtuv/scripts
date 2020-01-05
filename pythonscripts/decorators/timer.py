import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func_result = func(*args, **kwargs)
        print(time.time() - start)
        return func_result
    return wrapper


if __name__=='__main__':
    @timer
    def test():
        for i in range(5):
            print(i)
            time.sleep(1)

    test()
