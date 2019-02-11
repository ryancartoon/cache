import pytest

from mockredis import mock_redis_client
from unittest.mock import patch
from cache.simple import RedisCache


class CacheTestsBase(object):

    @pytest.fixture
    def make_cache(self):
        """Return a cache class or factory."""
        raise NotImplementedError()

    @pytest.fixture
    def c(self, make_cache):
        """Return a cache instance."""
        return make_cache()


class GenericCacheTests(CacheTestsBase):

    def test_generic_set_get(self, c):
        for i in range(3):
            assert c.set(str(i), i * i)

        for i in range(3):
            result = c.get(str(i))
            assert result == i * i

    def test_generic_get_set(self, c):
        assert c.set('foo', ['bar'])
        assert c.get('foo') == ['bar']

    def test_generic_add(self, c):
        # sanity check that add() works like set()
        assert c.add('foo', 'bar')
        assert c.get('foo') == 'bar'
        assert not c.add('foo', 'qux')
        assert c.get('foo') == 'bar'


class TestRedisCache(GenericCacheTests):

    @pytest.fixture()
    def make_cache(self):
        with patch('cache.simple.Redis', mock_redis_client):
            c = RedisCache()
            yield lambda: c
            c.clear()
