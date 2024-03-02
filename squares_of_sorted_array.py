class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        for i in range(0, len(nums)):
            squares.append(nums[i]**2)
        squares.sort()
        return squares