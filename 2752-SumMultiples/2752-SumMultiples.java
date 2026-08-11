// Last updated: 8/11/2026, 4:03:20 PM
class Solution {
    public static int sumOfMultiples(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) {
                sum += i;
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        int n = 10;
        System.out.println(sumOfMultiples(n));
    }
}
