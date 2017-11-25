from scipy.interpolate import interp1d
import numpy as np
def deco(func):
        def wrapper():
            print("before myfunc() called.")
            func()
            print("  after myfunc() called.")
        return wrapper

@deco
def myfunc():
    print(" myfunc() called.")

myfunc()
