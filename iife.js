// Immediately Invoked Function Expressions (IIFE)


// (function chai(name){
//     // named IIFE
//     console.log(`DB CONNECTED TWO ${name}`);
// })('sandip');

( (name) => {
    console.log(`DB CONNECTED TWO ${name}`);
} )('hitesh');

(function ch(){
    // named IIFE
    console.log(`DB CONNECTED TWO`);
})();

// for ending an iife you must give ; 