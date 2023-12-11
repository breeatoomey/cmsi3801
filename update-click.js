// Closure
var updateClickCount = (function () {
    var counter = 0; 
    return function () {
        counter++;
        return counter;
    }
})()

console.log(updateClickCount())
console.log(updateClickCount())
console.log(updateClickCount())
console.log(updateClickCount())
