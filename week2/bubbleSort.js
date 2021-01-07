var bubbleSort = (array) =>{
        swapped = true;
        while(swapped){
        swapped = false;
        for(let i = 0;i<array.length-1;i++){    
            if(array[i]>array[i+1]){
                temp = array[i]; 
                array[i] = array[i+1];  
                array[i+1] = temp;   
                swapped = true;  
            }
            
    }
        
    }
    return array;

}
console.log(bubbleSort([3,1,5,4,1,9]));