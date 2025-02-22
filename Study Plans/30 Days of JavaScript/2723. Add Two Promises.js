/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {

    let result1 = await promise1.then((value) => {return value});
    let result2 = await promise2.then((value) => {return value});
    return new Promise(resolve => {
        resolve(result1 + result2)
    })
};


addTwoPromises(Promise.resolve(2), Promise.resolve(2))
   .then(console.log); // 4
