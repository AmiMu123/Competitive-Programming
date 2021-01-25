function cookies(k, A) {
    A.sort((a,b)=>a-b)
    let ops = 0;


    while (A[0] < k && A.length > 1) {
        
      ops++;
      let calc = (A[0] * 1) + (A[1] * 2);
      A.splice(0, 2);
      let inserted = false
      if (A.length === 0) { // when the array is empty after splice
        A.push(calc);
      } else {
        for (var i = 0; i < A.length && !inserted; i++) {
          if (A[A.length - 1] < calc) {
            A.push(calc)
            inserted = true
          } else if (A[i] >= calc) {
            A.splice(i, 0, calc);
            inserted = true
          }
        }
      }
    }
    if (A[0] < k) {
      ops = -1;
    }
    return ops;
  }