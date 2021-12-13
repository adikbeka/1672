class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = []
        ans1 = []
        for i in range(len(accounts)):
            n = 0
            n = sum(accounts[i])
            ans.append(n)
            ans1 = max(ans)
        return ans1