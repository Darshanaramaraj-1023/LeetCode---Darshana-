// Last updated: 8/11/2026, 4:12:04 PM
class Solution {
    public boolean hasCycle(ListNode head) {

        if (head == null) return false;

        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                return true; // cycle detected
            }
        }

        return false; // no cycle
    }
}