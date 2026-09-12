class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)

        prefix = 1
        for i in range(0,len(nums)-1): #forward pointer
            result[i+1] = result[i+1]*nums[i]*prefix
            prefix = nums[i]*prefix

        postfix = 1
        for i in range(len(nums)-1, 0, -1): #backwards pointer
            result[i-1] = result[i-1]*nums[i]*postfix
            postfix = nums[i]*postfix

        return result


