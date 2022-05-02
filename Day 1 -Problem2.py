# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# 1.Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.

# my solution ( partially work)

class Solution:
    def isValid(self, s: str) :
        if (("[" in s) & ("]" in s)) | (("(" in s) & (")" in s)) | (("{" in s) & ("}" in s)):
            return True #checking for the any of the pairs are present in the string.
        # this condition will fail when bairs of the brackets are more
        else:
            return False
# Not able to find out  how to check the correct order of the brackets

# actual solution  using stack

class Solution:
    def isValid(self, s: str) :
        stack = [0]
        mapping = {0: None, '(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if mapping[stack.pop()] != c:
                    return False
        return stack == [0]

st = Solution()
print(st.isValid("{({[]})}"))


