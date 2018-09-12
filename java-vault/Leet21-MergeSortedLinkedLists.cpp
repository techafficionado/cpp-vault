/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
/*
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
*/
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode anode = l1;
        ListNode bnode = l2;
        ListNode head = null;
        ListNode curnode = null;
        
        while(anode!=null && bnode!=null){
            //System.out.println("Initial values:" + anode.val+"\t" +bnode.val);
            if(anode.val<bnode.val){
                //System.out.println(anode.val+"\t");
                if(head == null){
                    head = anode;
                }
                if(curnode == null){
                    curnode = anode;
                }
                else{
                    curnode.next = anode;
                    curnode = anode;
                }
                anode = anode.next;
                
            }
            else{
                //System.out.println(bnode.val+"\t");
                if(head == null){
                    head = bnode;
                }
                if(curnode == null){
                    curnode = bnode;
                }
                else{
                    curnode.next = bnode;
                    curnode = bnode;
                }
                bnode = bnode.next;
            }
                
        }
        
        while(anode!=null){
            //System.out.println(anode.val+"\t");
            if(head == null){
                    head = anode;
                }
                if(curnode == null){
                    curnode = anode;
                }
            else{
            curnode.next = anode;
                    curnode = anode;
            }
                anode = anode.next;
        }
        
        while(bnode!=null){
            //System.out.println(bnode.val+"\t");
            if(head == null){
                    head = bnode;
                }
                if(curnode == null){
                    curnode = bnode;
                }
            else{
            curnode.next = bnode;
                    curnode = bnode;
            }
                bnode = bnode.next;
        }
        return head;
    }
}
