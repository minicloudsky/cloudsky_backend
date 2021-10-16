import functools
import hashlib
import pickle

from django.core.cache import cache


def _compute_key(function, args, kw):
    '''serializerd and compute md5 value'''
    return hashlib.md5(pickle.dumps((function.__name__, args, kw))).hexdigest()


def cached(timeout=600):
    def decorator(func):
        @functools.wraps(func)  # copy func metadata
        def wrapper(*args, **kwargs):
            force_updata = kwargs.pop("redis_key", False)
            key = _compute_key(func, args, kw)
            if force_updata:
                # execute func
                result = func(*args, **kwargs)
                # save func execute result
                cache.set(key, pickle.dumps(result), times)
            else:
                result = cache.get(key)
                if result:
                    result = pickle.loads(result)
                else:
                    result = function(*args, **kw)
                    cache.set(key, pickle.dumps(result), timeout)
            return result

        return wrapper

    return decorator
