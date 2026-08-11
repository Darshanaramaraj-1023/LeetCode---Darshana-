// Last updated: 8/11/2026, 4:03:12 PM
class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        int fuel = mainTank;
        int extra = additionalTank;
        int distance = 0;
        int used = 0;

        while (fuel > 0) {
            fuel--;
            used++;
            distance += 10;

            if (used % 5 == 0 && extra > 0) {
                fuel++;
                extra--;
            }
        }
        return distance;
    }
}
