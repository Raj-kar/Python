from functools import wraps


def enforce(*types):
    def decorator(f):
        @wraps(f)
        def new_func(*args, **kwargs):
            """ convert args into something mutable   """
            new_args = []
            for (a, t) in zip(args, types):
                new_args.append(t(a))  # feel free to have more elaborated conversion
            return f(*new_args, **kwargs)

        return new_func

    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)


@enforce(float, float)
def divide(a, b):
    print(a / b)


repeat_msg("hello", '5')
divide(1, '4')
