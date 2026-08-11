// Last updated: 8/11/2026, 4:11:02 PM
class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        while (n > 0) {
            count += (n & 1);  
            n = n >>> 1;       
        }
        return count;
    }
}
