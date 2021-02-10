/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        
        ListNode first = headA;
        ListNode second = headB;
        
        int firstLen = len(first);
        int secondLen = len(second);
        
        int diff = Math.abs(firstLen - secondLen);
        
        if( firstLen > secondLen){
            first = moveNode(diff, first);
        }
        else if (firstLen < secondLen) {
            second = moveNode(diff, second);
        }

        
        while(first !=null && second != null){
            if( first == second) return first;
            first = first.next;
            second = second.next;
        }

        return null;
    }
    
    private ListNode moveNode( int diff, ListNode node){
            while(diff-- > 0){
                node = node.next;
            }
        
        return node; 
    }
    
    private int len(ListNode node){
        int len = 0;
        while(node != null){
            node = node.next;
            len++;
        }
        return len;
    }
}