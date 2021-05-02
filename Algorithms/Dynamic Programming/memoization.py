def add_to_80(n):
    print('runs long time')
    return n + 80


def memoized_add_to_80():
    cache = {}
    def add_to_cache(n):
        if n not in cache:
            cache[n] = n + 80
            print('runs long time')
        return cache[n]
    return add_to_cache

print('First program')
print(add_to_80(5))
print(add_to_80(5))
print(add_to_80(5))


memoized = memoized_add_to_80()
print('Second program')
print(memoized(5))
print(memoized(5))
print(memoized(5))