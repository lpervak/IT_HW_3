import time


def decor(func):
    def wrap(*args, **kwargs):
        t1 = time.time()
        print("Start time: " + str(t1))
        result = func(*args, **kwargs)
        t2 = time.time()
        print("End time: " + str(t2))
        print("Program ran for " + str(t2-t1) + " second(s)")
        return result
    return wrap


@decor
def func_():
    while True:
        a = int(input("Enter number: "))
        if a == 0:
            break


func_()
