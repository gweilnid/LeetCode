class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            print("Index: " + str(i) + "Num: " + str(num))
            looking_for = target - num
            if looking_for in nums:
                print(num, looking_for)
                index_pos = nums.index(looking_for)
                if index_pos is not i:
                    return [i, index_pos]
            