class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # iterate ove the array while keeping track of the last done operation in a stack
        stack = []
        for i in range(len(tokens)):
            if is_integer(tokens[i]):
                stack.append(tokens[i])
            else:
                RHS = int(stack.pop())
                LHS = int(stack.pop())
                if tokens[i] == "+":
                    last_operation = LHS + RHS
                    stack.append(last_operation)
                elif tokens[i] == "-":
                    last_operation = LHS - RHS
                    stack.append(last_operation)
                elif tokens[i] == "*":
                    last_operation = LHS * RHS
                    stack.append(last_operation)
                elif tokens[i] == "/":
                    last_operation = LHS / RHS
                    stack.append(last_operation)
        return int(stack[0])

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
