// Last updated: 8/11/2026, 4:03:29 PM
class Solution {
    public int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        int sum = 0;

        int takeOnes = Math.min(numOnes, k);
        sum += takeOnes;
        k -= takeOnes;

        int takeZeros = Math.min(numZeros, k);
        k -= takeZeros;

        sum -= k;

        return sum;
    }
}
