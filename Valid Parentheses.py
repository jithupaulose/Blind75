
def isValid(s: str) -> bool:
    round_brackets, curly_brackets, square_brackets = 0, 0, 0

    for char in s:
        if char == '(':
            round_brackets += 1
        elif char == ')':
            round_brackets -= 1
        elif char == '{':
            curly_brackets += 1
        elif char == '}':
            curly_brackets -= 1
        elif char == '[':
            square_brackets += 1
        elif char == ']':
            square_brackets -= 1

        # Early exit: if any counter goes negative, it means closing bracket appeared before its opening bracket
        if round_brackets < 0 or curly_brackets < 0 or square_brackets < 0:
            return False

    return round_brackets == 0 and curly_brackets == 0 and square_brackets == 0





class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '{' : '}',
            '(' : ')',
            '[' : ']'
        }
        for char in s:
            if char in brackets:
                stack.append(brackets[char])
            else:
                if len(stack) == 0 or char != stack.pop():
                    return False
        return not stack
