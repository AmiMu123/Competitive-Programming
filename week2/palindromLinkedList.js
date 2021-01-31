/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */

var isPalindrome = function(head) {
    let slow = head;
    let fast = head;
    // let right_array = [];
    let left_array = []
    while(fast){
        left_array.push(slow.val)
        slow = slow.next;
        fast = fast.next
    }
    if(left_array.length ===0){
        return true;
    }
    for(let i = 0;i<left_array.length;i++){
        if(left_array[i] !== left_array[(left_array.length-1)-i]){
            return false;
}
        
    }
    return true
    
};