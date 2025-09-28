tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]


class Solution(object):
    def __init__(self):
        self.stack = []
    
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        for token in tokens:
            if custom_isnumeric(token):
                self.push(int(token))
            else:
                param1= self.pop()
                param2= self.pop()
                if token == "+":
                    res = param2 + param1
                    self.push(res)
                elif token == "/":
                    res = int(param2 / param1)
                    self.push(res)
                elif token == "-":
                    res = param2 - param1
                    self.push(res)
                elif token == "*":
                    res = param2 * param1
                    self.push(res)
        print(self.stack[0])
        return self.stack[0]

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()
    


def custom_isnumeric(s):
    try:
        int(s)
        return True
    except:
        return False


ans = Solution()
ans.evalRPN(tokens)