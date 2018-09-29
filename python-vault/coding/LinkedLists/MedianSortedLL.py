#!/bin/python3

import sys
import os

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None

def _insert_node_into_singlylinkedlist(head, tail, val):
    if head == None:
        head = LinkedListNode(val)
        tail = head
    else:
        node = LinkedListNode(val)
        tail.next = node
        tail = tail.next
    return tail


# Complete the function below.

#For your reference:
#LinkedListNode {
#    int val
#    LinkedListNode next
#}

# Need to find if it is increasing or decreasing order or has equal values
def findorder(ptr):
    
    # 1 for increasing
    # -1 for decreasing
    # 0 for equal
    head = ptr 
    inccount = 0
    deccount = 0
    eqcount = 0
    #print("head:{} ptr.next:{}".format(head.val,ptr.next.val))
    while head != ptr.next:
        #print("head:{} ptr.next:{}".format(head.val,ptr.next.val))
        if ptr.val - ptr.next.val >0:
            deccount += 1 
        elif ptr.val - ptr.next.val <0:
            inccount +=1 
        else:
            eqcount += 1 
            
        ptr = ptr.next 
        
    #print("deccount:{} inccount:{} eqcount:{}".format(deccount,inccount,eqcount))    
    if deccount > inccount and deccount > inccount:
        return -1
    elif inccount>deccount and inccount> deccount:
        return 1 
    elif eqcount > deccount and eqcount > inccount:
        if deccount == 0 and inccount == 0:
            return 0
        elif deccount > inccount:
            return -1
        elif inccount >= deccount:
            return 1 
    
    
        
    

def find_median(ptr):
    
    #handle 1 element lists
    if ptr == ptr.next:
        return ptr.val
    
    
    orderval = findorder(ptr)
    #print("orderval:{}".format(orderval))
    # first find the actual head of list that maintains the sorting order
    # which means find the point where the next value decreases
    # This is assuming the list is in ascending order
    # if order is not guaranteed then we need to find the order too, by comparing 
    # atleast two elements
    if orderval != 0:
        ptrnext = None 
        while ptr is not None:
            #print("while ptr:{}".format(ptr.val))
            ptrnext = ptr.next
            if ptrnext is not None:
                if orderval == 1 and ptr.val > ptrnext.val:
                    break
                elif orderval == -1 and ptr.val < ptrnext.val:
                    break
                elif orderval == 0 and ptr.val != ptrnext.val:
                    break
                
                ptr = ptrnext
                
             
        
    #print("ptr:{}".format(ptr.val))
    #print("ptr.next.val:{}".format(ptr.next.val))
    ptrnext = ptr.next 
    ptr.next = None
    head = ptrnext 
    #print("head:{}".format(head.val))
    
    sptr = head
    fptr = head
    lsptr = None 
    while fptr is not None and fptr.next is not None:
        if fptr.next.next is None:
            fptr = fptr.next 
            # which implies even number of nodes 
            lsptr = sptr 
            sptr = sptr.next
            #print("lsptr:{} sptr:{}".format(lsptr.val,sptr.val))
        else:
            fptr = fptr.next.next 
            sptr = sptr.next 
            
    med = None 
    if lsptr is not None:
        med = (lsptr.val + sptr.val) //2
    else:
        med = sptr.val
    #print("sptr:{} fptr:{}".format(sptr.val,fptr.val))
    
    return med


if __name__ == "__main__":
    f = sys.stdout

    ptr = None
    ptr_tail = None
    ptr_size = int(input())
    ptr_i = 0
    while ptr_i < ptr_size:
        ptr_item = int(input())

        ptr_tail = _insert_node_into_singlylinkedlist(ptr, ptr_tail, ptr_item)
        if ptr_i == 0:
            ptr = ptr_tail
        ptr_i += 1

    #----added manually----
    ptr_tail.next = ptr
    arbitrary_shift = int(input())
    while (arbitrary_shift > 0):
        arbitrary_shift -= 1
        ptr = ptr.next
    #--------
        
    res = find_median(ptr)
    f.write(str(res) + "\n")


    f.close()
