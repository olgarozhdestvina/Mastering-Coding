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

// Avoiding recusrsion
function fibonacciBottomUp(n) {
    let answer = [0,1];
    for (let i=2; i<=n; i++) {
        answer.push(answer[i-1] + answer[i-2]);
    }
    return answer.pop();
}


const fasterFib = memoizedFib();
fasterFib(20);
fibonacciBottomUp(20);
