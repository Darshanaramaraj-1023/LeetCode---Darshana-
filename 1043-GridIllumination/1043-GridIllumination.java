// Last updated: 8/11/2026, 4:06:09 PM
class Solution {

    Map<Integer, Integer> row = new HashMap<>();
    Map<Integer, Integer> col = new HashMap<>();
    Map<Long, Integer> diag = new HashMap<>();
    Map<Long, Integer> antiDiag = new HashMap<>();
    Set<Long> lampsOn = new HashSet<>();

    public int[] gridIllumination(int n, int[][] lamps, int[][] queries) {

        for (int[] lamp : lamps) {
            int r = lamp[0];
            int c = lamp[1];

            long key = ((long) r << 32) | c;

            if (lampsOn.contains(key)) continue;

            lampsOn.add(key);

            row.put(r, row.getOrDefault(r, 0) + 1);
            col.put(c, col.getOrDefault(c, 0) + 1);
            diag.put((long) r - c, diag.getOrDefault((long) r - c, 0) + 1);
            antiDiag.put((long) r + c, antiDiag.getOrDefault((long) r + c, 0) + 1);
        }

        int[] ans = new int[queries.length];

        int[][] dirs = {
            {0, 0}, {-1, -1}, {-1, 0}, {-1, 1},
            {0, -1}, {0, 1},
            {1, -1}, {1, 0}, {1, 1}
        };

        for (int i = 0; i < queries.length; i++) {

            int r = queries[i][0];
            int c = queries[i][1];

            if (row.getOrDefault(r, 0) > 0 ||
                col.getOrDefault(c, 0) > 0 ||
                diag.getOrDefault((long) r - c, 0) > 0 ||
                antiDiag.getOrDefault((long) r + c, 0) > 0) {

                ans[i] = 1;
            }

            for (int[] d : dirs) {

                int nr = r + d[0];
                int nc = c + d[1];

                if (nr < 0 || nr >= n || nc < 0 || nc >= n) {
                    continue;
                }

                long key = ((long) nr << 32) | nc;

                if (!lampsOn.contains(key)) {
                    continue;
                }

                lampsOn.remove(key);

                row.put(nr, row.get(nr) - 1);
                col.put(nc, col.get(nc) - 1);
                diag.put((long) nr - nc, diag.get((long) nr - nc) - 1);
                antiDiag.put((long) nr + nc, antiDiag.get((long) nr + nc) - 1);
            }
        }

        return ans;
    }
}