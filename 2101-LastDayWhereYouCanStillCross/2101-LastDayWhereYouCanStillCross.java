// Last updated: 8/11/2026, 4:04:04 PM
import java.util.*;
class Solution {
    int[] dr = {1, -1, 0, 0};
    int[] dc = {0, 0, 1, -1};
    public int latestDayToCross(int row, int col, int[][] cells) {
        int left = 0, right = cells.length;
        int answer = 0;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (canCross(row, col, cells, mid)) {
                answer = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return answer;
    }
    private boolean canCross(int row, int col, int[][] cells, int day) {
        int[][] grid = new int[row][col];
        for (int i = 0; i < day; i++) {
            grid[cells[i][0] - 1][cells[i][1] - 1] = 1;
        }
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[row][col];
        for (int c = 0; c < col; c++) {
            if (grid[0][c] == 0) {
                q.offer(new int[]{0, c});
                visited[0][c] = true;
            }
        }
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];
            if (r == row - 1) return true;
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                if (nr >= 0 && nr < row && nc >= 0 && nc < col &&
                    !visited[nr][nc] && grid[nr][nc] == 0) {
                    visited[nr][nc] = true;
                    q.offer(new int[]{nr, nc});
                }
            }
        }
        return false;
    }
}
