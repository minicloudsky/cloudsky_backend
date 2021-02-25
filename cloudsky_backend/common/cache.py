from django.core.cache import cache
import time
import math
import functools
import pickle
import hashlib
import inspect
from django.conf import settings
from django.db.models import Q

from menu.models import Menu


def _compute_key(function, args, kw):
    '''序列化并求其哈希值'''
    return hashlib.md5(pickle.dumps((function.__name__, args, kw))).hexdigest()


def function_caches(times=600):
    def _memoize(function):
        @functools.wraps(function)  # 自动复制函数信息
        def __memoize(*args, **kw):
            force_updata = kw.pop("redis_key", False)
            key = _compute_key(function, args, kw)
            if force_updata:
                # 运行函数
                result = function(*args, **kw)
                # 保存结果
                cache.set(key, pickle.dumps(result), times)
            else:
                # 是否已缓存？
                result = cache.get(key)
                if result:
                    result = pickle.loads(result)
                else:
                    # 运行函数
                    result = function(*args, **kw)
                    # 保存结果
                    cache.set(key, pickle.dumps(result), times)
            return result

        return __memoize

    return _memoize



