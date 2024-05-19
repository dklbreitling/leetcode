class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def rec(s):
            if s in mem:
                return False

            if not s:
                return True

            s_len = len(s)
            for word in wordDict:
                if s_len >= len(word):
                    if s[:len(word)] == word:
                        if rec(s[len(word):]):
                            return True

            mem.add(s)
            return False
        
        mem = set()
        return rec(s)
