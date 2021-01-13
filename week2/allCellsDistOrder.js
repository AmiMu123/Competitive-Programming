var allCellsDistOrder = function(R, C, r0, c0) {
    let mat = []
    for(let i = 0;i<R;i++){
        for(let j = 0;j<C;j++){
            mat.push([i,j])
}
}
    let {abs} = Math;
    let result = mat.sort(([a1,a2],[b1,b2])=>
                          (abs(a1-r0)+abs(a2-c0))- 
                          (abs(b1-r0)+abs(b2-c0)));
    return result;    
};


