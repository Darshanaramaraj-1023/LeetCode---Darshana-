// Last updated: 8/11/2026, 4:02:41 PM
import java.util.*;

class Solution {
    public int[] queryResults(int limit, int[][] queries) {

        HashMap<Integer, Integer> ballColor = new HashMap<>();
        HashMap<Integer, Integer> colorFreq = new HashMap<>();

        int n = queries.length;
        int[] result = new int[n];

        for (int i = 0; i < n; i++) {

            int ball = queries[i][0];
            int newColor = queries[i][1];

            if (ballColor.containsKey(ball)) {

                int oldColor = ballColor.get(ball);

                colorFreq.put(oldColor,
                        colorFreq.get(oldColor) - 1);

                if (colorFreq.get(oldColor) == 0) {
                    colorFreq.remove(oldColor);
                }
            }

            ballColor.put(ball, newColor);

            colorFreq.put(newColor,
                    colorFreq.getOrDefault(newColor, 0) + 1);

            result[i] = colorFreq.size();
        }

        return result;
    }
}