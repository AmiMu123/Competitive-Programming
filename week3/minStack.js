/**
 * initialize your data structure here.
 */
var MinStack = function() {
    this.container = [];
     this.temp = []
     
 };
 
 /** 
  * @param {number} x
  * @return {void}
  */
 MinStack.prototype.push = function(x) {
     if(this.isEmpty()){
         this.container.push(x);
         this.temp.push(x);
         
 }
     else{
         this.container.push(x);
         if(x>this.temp[this.temp.length-1]){
         this.temp.push(this.temp[this.temp.length-1])
 }
         else if( x < this.temp[this.temp.length-1]){
            
             this.temp.push(x);
 }
      else{
         this.temp.push(x);
 }
         
 }
     
 };
 
 /**
  * @return {void}
  */
 MinStack.prototype.pop = function() {
     if(this.temp.length !==0){
         this.temp.pop();
     }
     if(this.container.length !==0){
         this.container.pop();
     }
     
 };
 
 /**
  * @return {number}
  */
 MinStack.prototype.top = function() {
     return this.container[this.container.length-1]
 
     
 };
 
 
 /**
  * @return {number}
  */
 MinStack.prototype.getMin = function() {
     
       return this.temp[this.temp.length-1];
     
     
 };
 MinStack.prototype.isEmpty = function(){
     return this.container.length == 0;
 }
 
 
 /** 
  * Your MinStack object will be instantiated and called as such:
  * var obj = new MinStack()
  * obj.push(x)
  * obj.pop()
  * var param_3 = obj.top()
  * var param_4 = obj.getMin()
  */