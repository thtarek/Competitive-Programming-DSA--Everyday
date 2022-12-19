class Solution:
    def countOdds(self, low: int, high: int):
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        else:
            return (high - low) // 2 + 1


obj = Solution()
res = obj.countOdds(800445804, 979430543)
print(res)