var countValley = (arr) =>{
    var countVal = 0;
    var seaLevel = 0;
    for(var i = 0;i<arr.length;i++){
        if(arr[i] === 'U'){
            seaLevel++;
        }
        else if(arr[i] === 'D'){
            seaLevel--;
    }
        if(arr[i] === 'U' && seaLevel ===0){
            countVal++
        }

}
    return countVal;
}

// console.log(checkValley('DDUUUUDD'))