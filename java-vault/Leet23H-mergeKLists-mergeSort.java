/*Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
*/
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        /*
        PriorityQueue<ListNode> pq = new PriorityQueue<ListNode>(lists.length, new Comparator<ListNode>(){
            @Override
            public int compare(ListNode l1, ListNode l2){
                if(l1.val<l2.val)
                    return -1;
                else if(l1.val == l2.val)
                    return 0;
                else
                    return 1;
            }
        });
        
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for(ListNode ln:lists)
            if(ln!=null){
                System.out.println("ln val:"+ln.val);
                pq.add(ln);
            }
        
        while(!pq.isEmpty()){
            cur.next = pq.poll();
            System.out.println("cur.next val:"+cur.next.val);
            cur = cur.next;
            System.out.println("cur val:"+cur.val);
            if(cur.next!=null)
                pq.add(cur.next);
        }
        return dummy.next;    
        */
        
        if (lists.length<=0 || lists == null)
            return null;
        
        return mergeKRecursive(lists,0,lists.length-1);
    }
    
    private ListNode mergeKRecursive(ListNode[] lists, int start, int end){
        if (start == end)
            return lists[start];
        else{
            int mid = start + ((end-start)/2);
            ListNode left = mergeKRecursive(lists,start,mid);
            ListNode right = mergeKRecursive(lists,mid+1,end);
            return mergeTwoLists(left, right);
        }
    }
    
     private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
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
