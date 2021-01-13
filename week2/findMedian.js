function findMedian(arr) {
    let sorted = arr.sort(function(a,b){return (a-b)})
    var middle = Math.floor(arr.length/2)
    return sorted[middle]
}
