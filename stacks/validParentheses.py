def isValid(s: str) -> bool:
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for bracket in s:
        # opening bracket
        if bracket in pairs.values():
            stack.append(bracket)
        # closing bracket
        elif bracket in pairs:
            if not stack or stack[-1] != pairs[bracket]:
                return False
            stack.pop()
        else:
            return False

    return not stack


isValid("([)]")


"""
brute force solution
"""
# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         stack = []
#         for bracket in s:
#             if bracket == "{":
#                 stack.append("}")
#             elif bracket == "}":
#                 if not stack or stack[-1] != "}":
#                     return False
#                 else:  stack.pop()
#             elif bracket == "(":
#                 stack.append(")")
#             elif bracket == ")":
#                 if not stack or stack[-1] != ")":
#                     return False
#                 else:  stack.pop()
#             elif bracket == "[":
#                 stack.append("]")
#             elif bracket == "]":
#                 if not stack or stack[-1] != "]":
#                     return False
#                 else: stack.pop()
#         return len(stack) == 0