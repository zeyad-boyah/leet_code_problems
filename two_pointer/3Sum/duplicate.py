class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_length = len(nums) -1
        main=0
        ans = []
        nums.sort()
        for main in range(nums_length-1) :
            if main >0 and nums[main] == nums[main-1]:
                continue
            left = main+1
            right = nums_length
            current_target = nums[main]
            while left < right and right > left:
                if nums[main] + nums[left] + nums[right] > 0:
                    right-=1
                elif nums[main] + nums[left] + nums[right] < 0:
                    left+=1
                else:
                    ans.append([nums[main],nums[left], nums[right]])
                    left +=1
                    while nums[left] == nums[left-1] and left<right:
                        left +=1
            main +=1
        return ans