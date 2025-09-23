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
