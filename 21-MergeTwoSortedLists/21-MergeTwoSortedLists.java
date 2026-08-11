// Last updated: 8/11/2026, 4:13:39 PM
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) { //if list is smaller
                current.next = list1; //add list 1
                list1 = list1.next;
            } else {
                current.next = list2; //if list 2 is smaller
                list2 = list2.next;//add 12
            } 
            current = current.next; //we have to add next element to newly added 
        }

        if (list1 != null) {
            current.next = list1;
        } else {
            current.next = list2;
        }

        return dummy.next;
    }
}
