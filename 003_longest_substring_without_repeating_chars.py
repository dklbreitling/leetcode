class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        cur_len = 0
        seen = set()
        
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                cur_len += 1
                right += 1
                max_len = max(cur_len, max_len)

            else:
                seen.remove(s[left])
                left += 1
                cur_len -= 1

        return max_len

