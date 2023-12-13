const user = {
    username: "hitesh",
    price: 999,

    welcomeMessage: function() {
        console.log(`${this.username} , welcome to website`);
        //console.log(this);
    }

}

//user.welcomeMessage()
user
// user.username = "sam"
// user.welcomeMessage()

// console.log(this);

// function chai(){
//     let username = "hitesh"
//     console.log(this.username);
// }

// chai()

// const chai = function () {
//     let username = "hitesh"
//     console.log(this.username);
// }

const chai =  () => {
    let username = "hitesh"
    console.log(this);  //this is empty object here
}


//chai()

// const addTwo = (num1, num2) => {
//     return num1 + num2
// }

const addTwo = (num1, num2) =>  num1 + num2

//const addTwo = (num1, num2) => ( num1 + num2 )

//const addTwo = () => ({username: "hitesh"})


//console.log(addTwo(2,5))


// const myArray = [2, 5, 3, 7, 8]
// const myfunc = function(item){
//     sum = 0
//     sum = sum + item
// }

// console.log(myArray.forEach(myfunc))