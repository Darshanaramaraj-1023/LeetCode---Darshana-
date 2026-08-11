// Last updated: 8/11/2026, 4:10:45 PM
class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> seen = new HashSet<>();
        int sum, d;

        while (n != 1) {
            if (seen.contains(n)) {
                return false;
            }
            seen.add(n);

            sum = 0;
            while (n > 0) {
                d = n % 10;
                sum += d * d;
                n /= 10;
            }
            n = sum;
        }
        return true;
    }
}
