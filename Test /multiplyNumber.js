let menu = {
    width: 200,
    height: 300,
    title: "My menu"
  };

function multiplyNum(obj){
    for (const key in obj){
        if (typeof(key) === Number) {
            key = key * 2
        }
    }

    for (const values in obj){
        if (typeof(values) === Number) {
            values = values * 2
        }
    }

}

multiplyNum(menu)
console.log(menu)