class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import math

        mem = [math.inf] * (amount + 1)
        mem[0] = 0

        for i in range(1, amount + 1):
            curr_min = math.inf
            for coin in coins:
                if i - coin >= 0:
                    curr_min = min(1 + mem[i - coin], curr_min)
            mem[i] = curr_min

        return mem[amount] if mem[amount] != math.inf else -1
        
