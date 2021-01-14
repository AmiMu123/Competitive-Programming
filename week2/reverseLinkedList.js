/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let prevNode = null;
    let currNode = head;
    let nextNode = null;
    // traversing throught the linkedlist takes O(n) time , and O(1) space
    while(currNode!==null){
        nextNode = currNode.next; // nextNode is a node next to currNode
        currNode.next = prevNode; // reversed next of current 
        prevNode = currNode;  // move prevNode one step forward
        currNode = nextNode;  // move currNode one step forward;
}
    head = prevNode;
    return head;

};