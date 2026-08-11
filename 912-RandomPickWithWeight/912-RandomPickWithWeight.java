// Last updated: 8/11/2026, 4:06:39 PM

class Solution {

    int[] prefix;
    int total;
    Random rand;

    public Solution(int[] w) {
        prefix = new int[w.length];
        prefix[0] = w[0];

        for (int i = 1; i < w.length; i++) {
            prefix[i] = prefix[i - 1] + w[i];
        }

        total = prefix[w.length - 1];
        rand = new Random();
    }

    public int pickIndex() {
        int target = rand.nextInt(total) + 1;

        int left = 0, right = prefix.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (prefix[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}