class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        
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
    }
}
