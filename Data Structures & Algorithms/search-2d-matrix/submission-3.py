class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                for i in matrix[mid]:
                    if i == target:
                        return True
                return False
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False