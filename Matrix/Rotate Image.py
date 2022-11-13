# Link - https://leetcode.com/problems/rotate-image/
# Author - Tarek Hossain
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
class Solution:
    def rotate(self, matrix):
        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                # save the top left
                topleft = matrix[top][left + i]
                # move bottom left in top left
                matrix[top][left + i] = matrix[bottom - i][left]
                # move bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                # move to top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                # move to top left into top right
                matrix[top + i][right] = topleft
            right -= 1
            left += 1

        return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
obj = Solution()

print(obj.rotate(matrix))
