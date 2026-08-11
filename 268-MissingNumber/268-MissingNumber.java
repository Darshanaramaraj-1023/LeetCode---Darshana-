// Last updated: 8/11/2026, 4:09:54 PM
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int x = n * (n + 1) / 2;
        int actual = 0;
        for (int num : nums) {
            actual += num;
        }
        return x - actual;
    }
}