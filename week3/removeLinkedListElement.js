/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */

 
var removeElements = function(head, val) {
    while(head !==null && head.val ===val){
       head = head.next;
   }
       let curr =head;
       let prev;
       while(curr!==null && curr.next !==null){
           prev = curr;
           if(curr.next.val=== val){
             prev.next = curr.next.next;
   }
           else{
           curr = curr.next;
   }
   }
       return head;
      
   }

