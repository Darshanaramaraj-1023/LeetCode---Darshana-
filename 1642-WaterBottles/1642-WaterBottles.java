// Last updated: 8/11/2026, 4:04:48 PM
class Solution {
    public static int numWaterBottles(int numBottles, int numExchange) {
        int total = numBottles;
        int empty = numBottles;

        while (empty >= numExchange) {
            int newBottles = empty / numExchange;
            total += newBottles;
            empty = (empty % numExchange) + newBottles;
        }
        return total;
    }

    public static void main(String[] args) {
        System.out.println(numWaterBottles(9, 3));   // 13
        System.out.println(numWaterBottles(15, 4));  // 19
    }
}
