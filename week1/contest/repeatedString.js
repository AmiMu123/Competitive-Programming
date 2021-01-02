function repeatedString(s, n) {
    var count_a = 0
    var remainder = n % s.length; 
    var div = Math.floor(n/s.length);
    if(s === 'a'){
        return n;
    }
    for(var i = 0;i<s.length;i++){
        if(s[i] ==='a'){
            count_a++;
        }
    }
    var full_rep = count_a * div;
    for(var i = 0;i<=remainder;i++){
        if(s[i] ==='a'){
            full_rep ++;
        }
    }
    return full_rep;

    
   }