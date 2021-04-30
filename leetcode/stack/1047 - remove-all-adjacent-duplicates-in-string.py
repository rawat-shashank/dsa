# Easy 1047 - remove-all-adjacent-duplicates-in-string - Success

class Solution:
    def removeDuplicates(self, S: str) -> str:
        res = []
        for chr in S:
            if len(res) and res[-1] == chr:
                res.pop()
            else:
                res.append(chr)
        return "".join(res)


Sol = Solution()
print(Sol.removeDuplicates(
    "abbaca"
))
