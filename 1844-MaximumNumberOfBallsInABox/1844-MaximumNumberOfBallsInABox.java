// Last updated: 8/11/2026, 4:04:27 PM
class Solution {
    public int countBalls(int lowLimit, int highLimit) {

        int[] box = new int[50];
        int max = 0;

        for (int num = lowLimit; num <= highLimit; num++) {

            int sum = digitSum(num);

            box[sum]++;

            max = Math.max(max, box[sum]);
        }

        return max;
    }

    private int digitSum(int n) {
        int sum = 0;

        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }

        return sum;
    }
}