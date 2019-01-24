# -*- codeing:utf-8 -*-

from redis import Redis


class BaseCache(object):
    def __init__(self, key_prefix, timeout):
        self.key_prefix = key_prefix
        self.timeout = timeout

    def get(self, key):
        pass

    def has(self, key):
        pass

    def add(self, key, value):
        return True

    def set(self, key, value):
        pass

    def delete(self, key):
        pass


class RedisCache(BaseCache):
    def __init__(self, key_prefix="", timeout=60, host='localhost',
                 port=6379, password=None, db=0):
        super().__init__(key_prefix, timeout)
        self._client = Redis(host=host, port=port, password=password)

    def load(self, value):
        if isinstance(value, bytes):
            return value.decode("utf-8")
        else:
            return value

    def get(self, key):
        return self.load(self._client.get(self.key_prefix + key))

    def add(self, key, value):
        return self._client.set(self.key_prefix + key, value)

    def has(self, key):
        return self._client.exists(self.key_prefix + key)

    def delete(self, key):
        return self._client.delete(self.key_prefix + key)
