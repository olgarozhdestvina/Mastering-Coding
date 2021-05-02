let calculations = 0;

function fibonacciRec(n) { // O(2^n)
    calculations++;
    if (n < 2) {
        return n;
    } return fibonacciRec(n-1) + fibonacciRec(n-2);
}


function memoizedFib() { // O(n)
    let cache = {};
    return function fib(n) {
        calculations++;
        if (n in cache) {
            return cache[n];
        }
        if (!cache[n]) {
            if (n < 2) {
                return n;
            } else {
                cache[n] = fib(n-1) + fib(n-2);
                return cache[n];
            }
        } 
    }
}

const fasterFib = memoizedFib();
fasterFib(20);
console.log('We did ' + calculations)