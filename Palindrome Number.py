https://leetcode.com/problems/palindrome-number/description/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
Time complexity: o(n)
Space complexity: o(n)

class Solution:
    def isPalindrome(self, x: int) -> bool:

        #check the x is negative number and x ends with 0 (not the number 0 itself)

        if x < 0 or (x%10 == 0 and x!= 0):
            return False
        
        reverseNum = 0
        while x > reverseNum:
            reverseNum = reverseNum*10 + x%10
            x = x//10

        return x==reverseNum or x == reverseNum//10

Time complexity: log(n)
Space complexity: o(1)
