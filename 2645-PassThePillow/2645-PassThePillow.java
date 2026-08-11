// Last updated: 8/11/2026, 4:03:41 PM
class Solution {
    public int passThePillow(int n, int time) {
        int pos = 1;
        int dir = 1;
        for (int i = 1; i <= time; i++) {
            pos += dir;
            if (pos == n || pos == 1) {
                dir = -dir;
            }
        }
        return pos;
    }
}
