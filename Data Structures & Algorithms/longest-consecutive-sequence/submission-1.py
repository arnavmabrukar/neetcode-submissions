class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet=set(nums)
        longest = 0

        for i in range(len(nums)):
            if (nums[i]-1) not in numsSet: # a sequence will only start once there is no left neighbor
                length=0
                while(nums[i]+length in numsSet):
                    length+=1
                longest = max(longest,length)
        return longest

