// Last updated: 8/11/2026, 4:03:11 PM
class Solution {
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        ListNode curr = head;

        while (curr != null && curr.next != null) {
            int gcdValue = gcd(curr.val, curr.next.val);

            ListNode newNode = new ListNode(gcdValue);
            newNode.next = curr.next;
            curr.next = newNode;

            curr = newNode.next;
        }

        return head;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}