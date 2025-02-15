/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let filteredArray = []
    for (let i = 0; i < arr.length; i += 1) {
        if (fn(arr[i], i) === true) {
            filteredArray.push(arr[i]);
        }
    }
    return filteredArray;
};