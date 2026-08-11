// Last updated: 8/11/2026, 4:10:50 PM
class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        //int row=grid.length;
        //int col=grid.length;
        // for (int i = 0; i < col; i++)
        for (int i = 0; i < grid.length; i++) {
            // for (int j=0;J<col;j++)
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }
    private void dfs(char[][] grid, int i, int j) {
        if (i < 0 || j < 0 ||
            i >= grid.length ||
            j >= grid[0].length ||
            grid[i][j] == '0') {
            return;
        }
        grid[i][j] = '0';
        dfs(grid, i + 1, j);
        dfs(grid, i - 1, j);
        dfs(grid, i, j + 1);
        dfs(grid, i, j - 1);
    }
}