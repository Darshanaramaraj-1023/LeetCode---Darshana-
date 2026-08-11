// Last updated: 8/11/2026, 4:14:07 PM
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] freq = new int[256];
        int left = 0, maxLen = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            freq[c]++;
            while (freq[c] > 1) {
                freq[s.charAt(left)]--;
                left++;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
