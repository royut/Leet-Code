/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    var counter = init;
    return {
        increment: () => {
            counter++;
            return counter;
        },
        decrement: () => {
            counter--;
            return counter;
        },
        reset: () => {
            counter = init;
            return counter;
        }
    }
};


const counter = createCounter(5)
console.log(counter.increment()); // 6
console.log(counter.reset()); // 5
console.log(counter.decrement()); // 4
