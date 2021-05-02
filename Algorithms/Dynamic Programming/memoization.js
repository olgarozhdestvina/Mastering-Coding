function addTo80(n) {
    console.log('Runs log time');
    return n + 80;
}


// using closure
function memoizedAddTo80() {
    let cache = {};
    return function(n) {
        if (!cache.n) {
            console.log('Runs log time');
            cache.n = n + 80;
        } return cache.n;
    }
}

console.log('First program');
console.log(addTo80(5));
console.log(addTo80(5));
console.log(addTo80(5));


const memoized = memoizedAddTo80();

console.log('Second program');
console.log(memoized(5));
console.log(memoized(5));
console.log(memoized(5));