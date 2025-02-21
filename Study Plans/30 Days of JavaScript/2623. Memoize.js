/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    var inputArgs = {}
    return function(...args) {
        if (args in inputArgs){
            // console.log('in')
            return inputArgs[args]
        }
        else {
            // console.log('out')
            inputArgs[args] = fn(...args);
            return inputArgs[args]
        }
    }
}



let callCount = 0;
const memoizedFn = memoize(function (a, b) {
    callCount += 1;
    return a + b;
})
console.log(memoizedFn(0, 0)) // 5
console.log(memoizedFn(0, 0)) // 5
console.log(callCount) // 1
