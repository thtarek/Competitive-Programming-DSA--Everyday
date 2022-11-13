# Link - https://leetcode.com/problems/spiral-matrix/
# Author - Tarek Hossain
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]


def spiralOrder(matrix):
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    total_length = right*bottom

    while left < right and top < bottom:
        # get every i in the top row
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        # get every i in the right col
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1
        # if not left < right and top < bottom:
        #     break
        if total_length == len(res):
            break
        # get every i in the bottom row
        for i in range(right-1, left-1, -1):
            res.append(matrix[bottom-1][i])
        bottom -= 1
        # get every i in the left col
        for i in range(bottom-1, top-1, -1):
            res.append(matrix[i][left])
        left += 1
    return res


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))