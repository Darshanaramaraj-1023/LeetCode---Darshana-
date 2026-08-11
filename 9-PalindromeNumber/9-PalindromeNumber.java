// Last updated: 8/11/2026, 4:13:54 PM
class Solution {
    public boolean isPalindrome(int x) {
        int temp = x;
        int rev = 0;
        while(x>0){
            int d;
            d = x % 10;
            rev = rev*10 + d;
            x = x/10;
        }
        if(temp == rev )return true;
        else return false;
    }
}