https://leetcode.com/problems/contains-duplicate/

Create an empty set to hold unique values.
Traverse through each number in the given nums list.
If a number is already in the set, return true since it's a duplicate.
If not, add it to the set.
If you have traversed the entire list without finding any duplicates, return false.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

time complexity is O(n)
space complexity is also O(n)


<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>

Sort the nums list.
Traverse the sorted list and check if any adjacent elements are the same.
If yes, return true. Otherwise, return false at the end.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for num in range(1,len(nums)):
            if nums[num] == nums[num-1]:
                return True
        return False

time complexity for this approach is O(n * log(n))
space complexity is O(1)
