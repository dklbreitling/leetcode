class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            possible_lengths = [1]
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    possible_lengths.append(1 + lis[j])
            lis[i] = max(possible_lengths)

        return max(lis)

