class Solution:
    def isValid(self, s: str) -> bool:
        shape_stack = []
        shapes ={'(': ')', '{': '}', '[' :']' }
        for shape in s:
            if shape in shapes.keys():
                shape_stack.append(shapes[shape])
            elif shape_stack and shape_stack[-1] == shape:
                shape_stack.pop()
                continue
            else:
                return False
        if shape_stack:
            return False
        return True