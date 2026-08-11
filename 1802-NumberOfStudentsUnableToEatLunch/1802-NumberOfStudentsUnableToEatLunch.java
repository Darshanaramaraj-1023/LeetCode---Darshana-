// Last updated: 8/11/2026, 4:04:35 PM
class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        Stack<Integer> st = new Stack<>();
        Queue<Integer> q = new LinkedList<>();
        for (int i = sandwiches.length - 1; i >= 0; i--) {
            st.push(sandwiches[i]);
        }
        for (int stud : students) {
            q.add(stud);
        }
        int t = 0;
        while (!q.isEmpty() && t < q.size()) {
            if (q.peek().equals(st.peek())) {
                q.poll();
                st.pop();
                t = 0;
            } else {
                q.add(q.poll());
                t++;
            }
        }
        return q.size();
    }
}