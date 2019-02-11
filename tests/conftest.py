import pytest


class SimRedisCache(object):
    def __init__(self):
        self.backend = dict()

    def get(self, key):
        return self.backend.get(key)

    def has(self, key):
        return key in self.backend

    def add(self, key, value):
        self.backend[key] = value
        return True

    def delete(self, key):
        try:
            self.backend.pop(key)
        except KeyError:
            pass


@pytest.fixture
def redis_cache(monkeypatch):
    monkeypatch.setattr('cache.simple.RedisCache', '_client', SimRedisCache)
