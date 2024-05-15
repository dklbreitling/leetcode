class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i, n in enumerate(nums):
            if n in seen:
                return True
            
            seen.add(n)

        return False

