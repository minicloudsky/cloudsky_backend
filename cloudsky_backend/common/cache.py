import functools
import hashlib
import pickle

from django.core.cache import cache


def _compute_key(function, args, kw):
    '''serializerd and compute md5 value'''
    return hashlib.md5(pickle.dumps((function.__name__, args, kw))).hexdigest()


def function_caches(times=600):
    def _memoize(function):
        @functools.wraps(function)  # auto copy func
        def __memoize(*args, **kw):
            force_updata = kw.pop("redis_key", False)
            key = _compute_key(function, args, kw)
            if force_updata:
                # execute
                result = function(*args, **kw)
                # save result
                cache.set(key, pickle.dumps(result), times)
            else:
                result = cache.get(key)
                if result:
                    result = pickle.loads(result)
                else:
                    result = function(*args, **kw)
                    cache.set(key, pickle.dumps(result), times)
            return result

        return __memoize

    return _memoize
