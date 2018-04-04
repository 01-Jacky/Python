import timeit
import time


def timing(func):
    """ Prints the time it took to run the passed function in seconds """
    def wrapper(*args, **kw):
        t1 = time.time()
        result = func(*args, **kw)
        t2 = time.time()
        print("Time to run {}: {} ".format(func.__name__, str((t2 - t1))))
        return result

    return wrapper


def singleton(cls):
    """
    Defines a singleton. Usage:
        @singleton
        class MyClass:
            ...
    """
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


def attrs(**kwds):
    """
    Attach attributes to functions(like C#?). Usage:
        @attrs(author="pepe", version="0.1")
        def mymethod(f):
            ...
    """
    def decorate(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        return f
    return decorate


def accepts(*types):
    """
    Enforce function argument.
        @accepts(int, (int,float))
        def func(arg1, arg2):
            return arg1 * arg2
    """
    def check_accepts(f):
        assert len(types) == f.func_code.co_argcount
        def new_f(*args, **kwds):
            for (a, t) in zip(args, types):
                assert isinstance(a, t), \
                       "arg %r does not match %s" % (a,t)
            return f(*args, **kwds)
        new_f.func_name = f.func_name
        return new_f
    return check_accepts


def returns(rtype):
    """
    Enforce return types.
        @returns((int,float))
        def func(arg1, arg2):
            return arg1 * arg2
    """
    def check_returns(f):
        def new_f(*args, **kwds):
            result = f(*args, **kwds)
            assert isinstance(result, rtype), \
                   "return value %r does not match %s" % (result,rtype)
            return result
        new_f.func_name = f.func_name
        return new_f
    return check_returns


# Sample decorator template
def my_decorator(some_function):

    def wrapper(n):
        print("Decorator: Doing stuff via decorator before function is called")

        if n % 2 == 0:
            print("Decorator: doing something with function param here... e.g. n is even!")
        else:
            print("Decorator: doing something with function param here... e.g. n is odd!")

        some_function(n)

        print("Decorator: Doing stuff via decorator after function arg is called")

    return wrapper


@my_decorator
def some_func(n):
    print("This is some func with param: {0}".format(n))

@timing
def add_n_nums(n):
    nums = [i for i in range(n)]
    sum(nums)


if __name__ == "__main__":
    sum = add_n_nums(9999999)
    print(sum)