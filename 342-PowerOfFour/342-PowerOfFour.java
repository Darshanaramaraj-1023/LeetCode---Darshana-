// Last updated: 8/11/2026, 4:09:36 PM
class Solution {
    public boolean isPowerOfFour(int n) {
        if (n <= 0) return false;
        return (n & (n - 1)) == 0 && (n & 0x55555555) != 0;
    }
}
