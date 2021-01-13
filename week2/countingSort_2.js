function countingSort(arr) {
    let max = Math.max(...arr)+1
    let container = new Array(max).fill(0) 
    for(let i = 0;i<arr.length;i++){
        let curr = arr[i];
        container[curr] +=1;
    }
    
    let result= []
    for(let i = 0;i<container.length;i++){
        for(let j=0;j<container[i];j++){
            result.push(i);
        }
    }
    return result

}