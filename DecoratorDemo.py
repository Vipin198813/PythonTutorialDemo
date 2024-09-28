import time

def timer_func(func):
    def time_test_func():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return time_test_func

@timer_func
def test():
    print(2345634*4534534)

test()