class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        result = []
        for i in range(len(nums)):
            if i == 0:
                pass
            elif i == 1:
                prefixes[i] = nums[0]
            else:
                prefixes[i] = (nums[i - 1] * prefixes[i - 1])
        for i in range(len(nums) - 1,  -1, -1):
            if i == len(nums) - 1:
                pass
            elif i == len(nums) - 2:
                suffixes[i] = (nums[len(nums) - 1])
                
            else:
                suffixes[i]= (nums[i + 1] * suffixes[i + 1])
        for i in range (len(nums)):
            result.append(prefixes[i] * suffixes[i])
        return result

            
            

            

        