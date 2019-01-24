

from SimpleCache import SimpleCache


def main():
    cache = SimpleCache()
    key = "key1"
    value = "value1"
    cache.set(key, value)

    print("cache for %s: is %s".format(key, cache.get(key)))


if __name__ == "__main__":
    main()
