// Last updated: 8/11/2026, 4:09:39 PM
class Solution {
    public static int bulbSwitch(int n) {
        return (int)Math.sqrt(n);
    }

    public static void main(String[] args) {
        System.out.println(bulbSwitch(3)); 
        System.out.println(bulbSwitch(0));
        System.out.println(bulbSwitch(1)); 
        System.out.println(bulbSwitch(10)); 
    }
}
