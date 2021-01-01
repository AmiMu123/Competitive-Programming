var reverse = function(x) {
    var arr = []
    var strX = String(x);
    
    if(x ===0 ){
        return 0;
    }
    if(strX[strX.length-1]==='0'){
        strX = strX.slice(0,strX.length-1);
    }
     if (strX[0] === '-'){
        strX = strX.substring(1).concat('-')
        
    }

    for(var i = 0;i<strX.length;i++){
        arr.push(strX[i]);
    }
    arr.reverse()
    var reverted= String(arr).split(',').join('');

     reverted = parseInt(reverted);
     if(reverted >=(2**31)-1 ||  reverted<= -(2**31)){
        return 0;
    }
    return reverted;

};

