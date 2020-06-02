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
        ListNode head = new ListNode(0);
        ListNode youbiao = head;
        int a = 0,b = 0,jin = 0,sum = 0;
        while(l1 != null || l2 != null){
            a = (l1!=null) ? l1.val : 0;
            b = (l2!=null) ? l2.val : 0;
            sum = a + b + jin;
            jin = sum / 10;
            youbiao.next = new ListNode(sum % 10);
            youbiao = youbiao.next;
            if(l1 != null)l1 = l1.next;
            if(l2 != null)l2 = l2.next;
        }
        if(jin!=0){
            youbiao.next = new ListNode(jin);
        }
        return head.next;
    }
}