var selectionSort = (array) =>{
    for(let i = 0;i<array.length;i++){
        for(let j = i+1;j<array.length;j++){
            if(array[i]>array[j]){
                temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
    return array;
}

console.log(selectionSort([2,3,1,2,5,3,7]))