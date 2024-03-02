class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k is 0:
            return []
        k = k%len(nums)
        temp = nums[-k:]
        # k=2 1,2,3,4  =>  4 1 2 3  =>  3 4 1 2
        for i in reversed(range(0, len(nums)-k)):
            nums[i+k] = nums[i]
        for i in range(0, len(temp)):
            nums[i] = temp[i]
        return nums