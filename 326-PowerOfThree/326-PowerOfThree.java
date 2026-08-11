// Last updated: 8/11/2026, 4:09:37 PM
class Solution {
    public boolean isPowerOfThree(int n) {
        int maxPower = 1162261467; 
        if (n <= 0) return false;
        return maxPower % n == 0;
    }
}
