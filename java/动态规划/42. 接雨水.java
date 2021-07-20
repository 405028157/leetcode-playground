class Solution {
    public int trap(int[] height) {
        int n = height.length;

        if (n <= 1)
            return 0;
        
        int[] leftMax = new int[n];
        int[] rightMax = new int[n];
        int ans = 0;

        for (int i = 1; i < n; i++) {
            leftMax[i] = Math.max(leftMax[i - 1], height[i - 1]);
        }

        for (int i = n - 2; i >= 0; i--) {
            rightMax[i] = Math.max(rightMax[i + 1], height[i + 1]);
        }

        for (int i = 1; i < n - 1; i++) {
            int maxHeight = Math.min(leftMax[i], rightMax[i]);
            ans += Math.max(maxHeight - height[i], 0);
        }

        return ans;
    }
}