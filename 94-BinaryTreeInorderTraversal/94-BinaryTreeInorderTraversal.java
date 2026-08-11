// Last updated: 8/11/2026, 4:12:21 PM
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        inorder(root, ans);
        return ans;
    }

    void inorder(TreeNode root, List<Integer> ans) {
        if (root == null)
            return;

        inorder(root.left, ans);
        ans.add(root.val);
        inorder(root.right, ans);
    }
}