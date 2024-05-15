class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [n for n in nums]

        answer[0] = 1
        answer[-1] = 1
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer

