// Last updated: 8/11/2026, 4:04:07 PM
class Solution {
    public static boolean isThree(int n) {
        int root = (int) Math.sqrt(n);
        
        if (root * root != n) {
            return false;
        }
        
        if (root < 2) {
            return false;
        }
        
        for (int i = 2; i * i <= root; i++) {
            if (root % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isThree(2));  // false
        System.out.println(isThree(4));  // true
        System.out.println(isThree(9));  // true
        System.out.println(isThree(16)); // false
    }
}
