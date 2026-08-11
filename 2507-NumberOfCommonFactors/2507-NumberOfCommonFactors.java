// Last updated: 8/11/2026, 4:03:45 PM
class Solution {
    public static int commonFactors(int a, int b) {
        int gcd = 1;
        
        for (int i = 1; i <= Math.min(a, b); i++) {
            if (a % i == 0 && b % i == 0) {
                gcd = i;
            }
        }
        
        int count = 0;
        for (int i = 1; i <= gcd; i++) {
            if (gcd % i == 0) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(commonFactors(12, 6));   // Output: 4
        System.out.println(commonFactors(25, 30));  // Output: 2
    }
}
