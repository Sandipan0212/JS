console.log("hi")

const a = 10
let b = "44"
var c = "hello"
let d = 44
//console.table([a,b,c])

console.log(typeof b) //number
console.log(typeof null)  //object
console.log(typeof undefined) //undefined

// alert(3+3) // not allowed in node, allowed in browser 

//string to number and number to string//

//let score = Number(b) 
//let e = String(d) //caps

// similarly Boolean can be used to convert 1 => true 
// 0 => false
// empty string => false
// non empty string => true

//console.log(typeof 1+"2") //12
//console.log(typeof 1+4+"2") // 32
//console.log(typeof "1"+2+2) // 122
//console.log(typeof "2"+1) //21

let n = 100
n++ //101
++n //102
console.log(n)

//study x++ and ++x

const id = Symbol('123')
const id2 = Symbol('123') // both are different and unique 

//console.log(id === id2)

const myfun = function(){
    console.log("Hello")
}

console.log(typeof myfun)



let val;
val = 5 ?? 10
console.log(val)