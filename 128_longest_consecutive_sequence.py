class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)

        max_len = 0
        for num in n_set:
            if num - 1 in n_set:
                continue # not start of seq
            curr_num = num
            l = 1
            while curr_num + 1 in n_set:
                l +=1
                curr_num += 1
            else:
                max_len = max(max_len, l)
        
        return max_len

