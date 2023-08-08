import time


def show_begin_end(func):
    def deco_func(*args, **kwargs):
        print("== start")
        result = func(*args, **kwargs)
        print("== end")
        return result

    return deco_func


def sleep_for_a_while():
    print("sleeping")
    time.sleep(2)
    print("done sleeping")


decorated_sleep = show_begin_end(sleep_for_a_while)

decorated_sleep()
