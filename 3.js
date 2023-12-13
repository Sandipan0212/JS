//push, concat

const arr4 = [1,2,3,4,5]

const ar1 = [6,7,8]

//arr.push(ar1)
ar4 = arr4.concat(ar1)

//console.log(arr)
//console.log(ar2)

const arr3 = [...arr4,...ar1]
console.log(arr3)

console.log(Array.isArray([1,2,3,4])) // true if it is an array
console.log(Array.from("Hitesh")) // converts to array
console.log(Array.from({name: "Hitesh"}))// returns empty array