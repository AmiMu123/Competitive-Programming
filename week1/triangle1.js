var printTrangle = (length) =>{
    var star = ''
    for(var i = 0;i<=length;i++){
        for(var j=1;j<=i;j++ ){
            star =star+ '*'
            
        }
        star =star+ "\n"
    }
    return star+"\n"
}
console.log(printTrangle(4))

