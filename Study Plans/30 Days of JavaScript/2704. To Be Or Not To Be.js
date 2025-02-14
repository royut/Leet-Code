/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: (val2) => {
            if (val2 === val){
                return true
            }
            else {
                throw "Not Equal"
            }
        },
        notToBe: (val2) => {
            if (val2 !== val){
                return true;
            }
            else {
                throw "Equal";
            }
        }
    }
};


console.log(expect(5).toBe(5)); // true
console.log(expect(5).notToBe(5)); // throws "Equal"
// console.log(expect(5).notToBe(null))