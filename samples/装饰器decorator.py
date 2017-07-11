#
import functools

def log(func_str):
    if isinstance(func_str, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (func_str, func.__name__))
                _func =func(*args, **kw)
                print('%s end %s()' % (func_str, func.__name__))
                return _func
            return wrapper
        return decorator
    else:
        @functools.wraps(func_str)
        def wrapper(*args, **kw):
            print('begin call %s():' % func_str.__name__)
            _func = func_str(*args, **kw)
            print('end call %s()' % func_str.__name__)
            return _func
        return wrapper


@log
def now():
    print('2015-3-25 func')
now()


@log('execute')
def now():
    print('2017-7-11 text')
now()
