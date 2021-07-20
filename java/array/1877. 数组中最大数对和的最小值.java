class Solution {
    public int minPairSum(int[] nums) {
        int n = nums.length;
        if (n <= 2) {
            return Arrays.stream(nums).sum();
        }
        Arrays.sort(nums);
        int max_sum = 0;

        for (int i = 0; i < n >> 1; i++) {
            max_sum = Math.max(max_sum, nums[i] + nums[n - 1 - i]);
        }

        return max_sum;
    }
}