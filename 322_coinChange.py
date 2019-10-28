class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not amount: return 0
        min_coins = [0] + [float('inf')] * amount
        print(min_coins)
        for c in coins:
            for i in range(c, amount + 1):
                min_coins[i] = min(min_coins[i], min_coins[i - c] + 1)

        return min_coins[-1] if min_coins[-1] != float('inf') else -1
