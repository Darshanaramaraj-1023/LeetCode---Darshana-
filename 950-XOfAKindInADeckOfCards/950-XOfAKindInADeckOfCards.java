// Last updated: 8/11/2026, 4:06:28 PM
import java.util.*;

class Solution {
    public boolean hasGroupsSizeX(int[] deck) {
        Map<Integer, Integer> count = new HashMap<>();

        for (int card : deck) {
            count.put(card, count.getOrDefault(card, 0) + 1);
        }

        int gcdValue = 0;

        for (int freq : count.values()) {
            gcdValue = gcd(gcdValue, freq);
        }

        return gcdValue >= 2;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}