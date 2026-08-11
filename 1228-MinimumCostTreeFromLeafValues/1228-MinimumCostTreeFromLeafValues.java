// Last updated: 8/11/2026, 4:05:33 PM
import java.util.*;

class Solution {
    public int mctFromLeafValues(int[] arr) {
        int res = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(Integer.MAX_VALUE);

        for (int num : arr) {
            while (stack.peek() <= num) {
                int mid = stack.pop();
                res += mid * Math.min(stack.peek(), num);
            }
            stack.push(num);
        }

        while (stack.size() > 2) {
            res += stack.pop() * stack.peek();
        }

        return res;
    }
}