/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if(l1!=null && l2==null)
            return l1;
        else if(l1==null && l2!=null)
            return l2;
        int carry=0;
        int sum = 0;
        int l3ans = 0;
        boolean head = false;
        ListNode l3Node = new ListNode(0);
        ListNode prev = l3Node;
        ListNode l3Head = l3Node;
        while( (l1!=null) || (l2!=null) || (carry!=0)){
            if(l1!=null && l2!=null)
                sum = l1.val+l2.val+carry;
            else if(l1!=null)
                sum = l1.val+carry;
            else if(l2!=null)
                sum = l2.val+carry;
            else
                sum = carry;            
            
            if (sum>9){                
                l3ans = sum%10;
                carry = sum/10;
                //System.out.println("l3ans:"+l3ans+" carry:"+carry);
            }         
            else{
                l3ans = sum;
                carry=0;
            }
            
            if (head== false){
                //System.out.println("in head");
                l3Node.val = l3ans;
                l3Node.next = null;
                l3Head = l3Node;                
                head = true;
            }
            else{
                //System.out.println("in head else l3ans:"+l3ans);
                prev = l3Node;
                l3Node = new ListNode(l3ans);
                l3Node.next = null;
                prev.next = l3Node;
                
            }   
            if(l1!=null)
                l1 = l1.next;
            if(l2!=null)
                l2 = l2.next;                
            
        }
        return l3Head;
    }
}
