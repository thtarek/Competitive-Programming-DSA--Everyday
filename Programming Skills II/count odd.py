class Solution:
    def countOdds(self, low: int, high: int):
        count = 0
        if low == 0 and high == 0:
            return count
        for i in range(low, high+1):
            if i % 2 != 0:
                count += 1
        return count


obj = Solution()
res = obj.countOdds(800445804, 979430543)
print(res)



