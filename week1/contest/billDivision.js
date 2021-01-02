function billDivision(bill, k, b) {
    var refused = bill[k];
    var total = 0
    for(var i = 0;i<bill.length;i++){
        total = ((total + bill[i]));
    }
    var b_actual = (total - refused)/2;  // 7
    var over_charge = total/2; // 12
    if(b_actual === b){
        console.log('Bon Appetit')
    }
    else{
        console.log(over_charge-b_actual)
    }
    
    

}

console.log(billDivision([3,10,2,9],1,12))