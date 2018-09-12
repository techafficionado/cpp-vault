/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
/*Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
*/
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
                
        ListNode runNode = head;
        ListNode behindNode = null;
        ListNode behindNodePrev = null;
        int count = 0;
       
        
        while(runNode!=null){
            if(count == n-1){
                behindNode = head;
                behindNodePrev = null;
            }
            runNode = runNode.next;
            if(runNode == null)
                break;
            count++;
            
            if(behindNode != null){
                behindNodePrev = behindNode;
                behindNode = behindNode.next; 
            }
        }
        
        //System.out.println(" behindNode Val:"+behindNode.val);
        if(behindNode == null)
            return null;
        
        if (behindNodePrev == null) // eg. case [1,2] , n=2
            head = behindNode.next;
        else
            behindNodePrev.next = behindNode.next;
        behindNode = null;
        return head;
    }
}
