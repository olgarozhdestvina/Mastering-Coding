from time import time

calculations = 0
def performance(f):
    is_evaluating = False
    def g(*args, **kwargs):
        nonlocal is_evaluating
        if is_evaluating:
            return f(*args, **kwargs)
        else:
            start_time = time()
            is_evaluating = True
            try:
                value = f(*args, **kwargs)
            finally:
                is_evaluating = False
            end_time = time()
            print('time taken: {time}'.format(time=end_time-start_time))
            return value
    return g


# Time: O(2^n)
@performance
def fib_rec(n): 
    global calculations
    calculations += 1
    if n < 2:
        return n
    return fib_rec(n-1) + fib_rec(n-2)


# Time: O(n)
@performance
def memoized_fibonacci():
    cache = {}
    def fib(n):
        global calculations
        calculations += 1
        if not n in cache:
            if n < 2:
                cache[n] = n
                return cache[n]
            else:
                cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
    return fib

#print(fib_rec(30))
#print(calculations)
# time taken: 3.564558267593384
# 832040

fibonacci = memoized_fibonacci()
print(fibonacci(30))
print(calculations)
# time taken: 0.0
# 832040