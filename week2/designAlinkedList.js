/**
 * Initialize your data structure here.
 */
var MyLinkedList = function (){
    this.head = null;
    this.length = 0;
};

/**
 * Get the value of the index-th node in the linked list. If the index is invalid, return -1. 
 * @param {number} index
 * @return {number}
 */
MyLinkedList.prototype.get = function(index) {
    if (index >= this.length) return -1; // >= becasue index is 0 based
    
    let currNode = this.head,
    i;
    for(i = 0;i<index;i++){
        currNode = currNode.next;
}
    return currNode.val
};

/**
 * Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtHead = function(val) { 
this.head = {
       val: val,
       next:this.head
   } 
    this.length++;
};

/**
 * Append a node of value val to the last element of the linked list. 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtTail = function(val) {
    if(this.length == 0){
        this.addAtHead(val);
        return;
    }
    let currNode = this.head;
    while(currNode.next != null){
        currNode = currNode.next;    
    }
    currNode.next = {
        val : val,
        next: null
    };
    this.length++;
};

/**
 * Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtIndex = function(index, val) {
    if(index > this.length) return;
    
    if(this.length == 0){
        this.addAtHead(val)
        return;
    }
    
     if(index === this.length){
        this.addAtTail(val);
        return;
    }
    
    let i = 0,
        currNode = this.head,
        prevNode;
    
    while(i < index){
        prevNode = currNode
        currNode = currNode.next;
        i++;     
    }
    
    let newNode = {
        val:val
    }; 
    newNode.next = currNode;
    prevNode.next = newNode;
    this.length += 1;
    return;        
};

/**
 * Delete the index-th node in the linked list, if the index is valid. 
 * @param {number} index
 * @return {void}
 */
MyLinkedList.prototype.deleteAtIndex = function(index) {
    if(index >= this.length || index < 0) return;
    
    let i = 0,
        currNode = this.head,
        prevNode;
    
    while(i < index){
        prevNode = currNode
        currNode = currNode.next;
        i++;     
    }
 
    prevNode.next = currNode.next;
    this.length--;
};

/** 
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = Object.create(MyLinkedList).createNew()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */