BRUTE FORCE SOLUTION

TIME COMPLEXITY : O(n^2)
SPACE COMPLEXITY: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]



HASH MAP SOLUTION


Initialize a Dictionary: Use a dictionary to store the value of an element as the key and its index as the value.
Iterate Over the Array: For each element in the array, calculate the difference between the target and that element. This difference is what you need to find in the array.
Check the Dictionary: If the difference is already a key in the dictionary, you've found the two elements that sum up to the target.
Update Dictionary: If the difference is not found in the dictionary, add the current element and its index to the dictionary.


TIME COMPLEXITY : O(n)
SPACE COMPLEXITY: O(n)

class Solution:
  def twoSum(nums, target):
      # Create a dictionary to store the value and its index
      num_dict = {}
  
      # Iterate over the list
      for index, num in enumerate(nums):
          difference = target - num
          if difference in num_dict:
              return [num_dict[difference], index]
          num_dict[num] = index

