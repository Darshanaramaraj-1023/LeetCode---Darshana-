// Last updated: 8/11/2026, 4:07:19 PM
import java.util.*;

class Solution {
    public String longestWord(String[] words) {
        Arrays.sort(words);

        Set<String> built = new HashSet<>();
        String result = "";

        for (String word : words) {
            if (word.length() == 1 || built.contains(word.substring(0, word.length() - 1))) {
                built.add(word);

                if (word.length() > result.length()) {
                    result = word;
                }
            }
        }

        return result;
    }
}