class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []

        for t in tokens:
            try:  # assume integer
                stack.append(int(t))
            except ValueError:
                b = stack.pop()
                a = stack.pop()
                match t:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":
                        stack.append(a * b)
                    case "/":
                        stack.append(int(float(a) / b))  # truncate towards zero

        return stack[0]
