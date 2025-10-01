from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(i.bit_count())
        return ans

        # dp = [0] * (n+1)
        # for i in range(n+1):
        #     dp[i] = dp[i>>1] + (i&1)
        # return dp