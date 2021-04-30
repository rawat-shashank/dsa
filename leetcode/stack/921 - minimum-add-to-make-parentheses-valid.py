# Medium 921 - minimum-add-to-make-parentheses-valid - Success

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        out = []
        for x in S:
            if x == ')' and out and out[-1] == '(':
                out.pop()
            else:
                out.append(x)
        return len(out)


Sol = Solution()
print(Sol.minAddToMakeValid(
    "()))"
))
