class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # initialize a result list that will be appended to
        res = []
        # sort the existing array of numbers
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]: # prevent dupes
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[i] == nums[i - 1] and l < r:
                        l += 1

        return res



