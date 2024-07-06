import java.util.Arrays;

class Solution {
    public int minDifference(int[] nums) {
        if (nums.length <= 4) return 0;
        Arrays.sort(nums);
        int answer = (int) 2e9;
        for (int i = 0; i < 4; ++i) answer = Math.min(answer, nums[nums.length - 1 - i] - nums[3 - i]);
        return answer;
    }
}