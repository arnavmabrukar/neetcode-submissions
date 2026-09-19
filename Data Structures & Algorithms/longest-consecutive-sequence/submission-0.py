class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # temp var = current item +1
        # if the temp is empty just input the value and increment the seq counter

        temp = None
        seq_count = 0
        for i in range(len(nums)):
            if temp is None:
                temp = nums[i]+1 #insert the first element + 1
                seq_count += 1 #update counter
            else:
                if temp == nums[i]:
                    temp = nums[i]+1
                    seq_count += 1
                else:
                    seq_count = 0 #reset the counter
            print('item: '+nums[i]+', temp: '+temp+', seq_count: '+{seq_count})
        return seq_count