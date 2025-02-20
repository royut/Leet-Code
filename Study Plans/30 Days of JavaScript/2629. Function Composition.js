/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        if (functions.length === 0){
            return x
        }
        let index = functions.length - 1;
        let f = functions[index](x);
        index -= 1
        while(index >= 0) {
            let func = functions[index];
            f = func(f)
            index -= 1;
        }
        return f
    }
};


const fn = compose([x => x + 1, x => 2 * x])
console.log(fn(4)) // 9
console.log(fn(4)) // 9
