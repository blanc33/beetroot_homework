def in_range(start, stop=None, step=None):
    if stop is None:
        if not isinstance(start, int):
            raise TypeError("'" + start.__class__.__name__ + "' object cannot be interpreted as an integer")
        start = 0
        stop = start
        step = 1
    elif step is None:
        if not isinstance(stop, int):
            raise TypeError("'" + stop.__class__.__name__ + "' object cannot be interpreted as an integer")
        step = 1
    else:
        if not isinstance(step, int):
            raise TypeError("'" + step.__class__.__name__ + "' object cannot be interpreted as an integer")
        if step == 0:
            raise ValueError('myImplementationOfRange() arg 3 must not be zero')

    i = start
    if step > 0:  # step arg is increasing
        while i < stop:
            yield i
            i += step
        return i
    elif step < 0:  # step arg is decreasing
        while i > stop:
            yield i
            i += step  # Adding a negative to decrease
        return i

for i in in_range(0, 4):
    print(i)
