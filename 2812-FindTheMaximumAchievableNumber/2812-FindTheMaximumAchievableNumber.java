// Last updated: 8/11/2026, 4:03:17 PM
class Solution {
    public static int theMaximumAchievableX(int num, int t) {
        return num + 2 * t;
    }

    public static void main(String[] args) {
        System.out.println(theMaximumAchievableX(4, 1)); 
        System.out.println(theMaximumAchievableX(3, 2)); 
    }
}
