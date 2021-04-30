# Easy 1021 - remove-outermost-parentheses - Success

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        temp = 0
        output = []
        for chr in S:
            if chr == '(':
                temp += 1
            if temp != 1:
                output.append(chr)
            if chr == ')':
                temp -= 1

        return "".join(output)


Sol = Solution()
print(Sol.removeOuterParentheses(
    "()()"
))
