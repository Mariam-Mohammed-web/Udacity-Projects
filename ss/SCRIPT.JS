function factorial(n) {
    if (n === 0 || n === 1) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }

function temperatureConverter(temprature,from,to) {
    if (from=="c" && to =="f") {
        F = (temprature * 9/5) + 32;
        return F.toFixed(2)
    } else if(from=="c" && to =="k"){
        K = (temprature + 459.67) * 5/9;
        return K.toFixed(2)
    } else if (from =="f" && to=="c"){
        C = (temprature - 32) * 5/9;
        return C.toFixed(2)
    } else if (from=="f" && to=="k"){
        K = (temprature + 459.67) * 5/9;
        return K.toFixed(2)
    } else if (from =="k" && to=="c"){
        C = temprature - 273.5;
        return C.toFixed(2)
    } else if (from=="k"&& to=="f"){
        F = (K * 9/5) - 459.67 ;
        return F.toFixed(2)
    } else console.log("please enter c or f or k");
    }

temperatureConverter(24,"c","f")