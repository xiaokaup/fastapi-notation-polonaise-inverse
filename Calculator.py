class Calculator:
    stack: list

    def __init__(self, stack: None | list[int] = None):
        if stack is None:
            stack = []
        self.stack = stack

    def get_expression_result(self, expression: str) -> int:
        # clean space in expression string
        expression = "".join(expression.split(" "))
        # Loop through the expression without spaces
        while len(expression) > 0:
            character = expression[0]

            if character.isdigit():
                self.stack.append(int(character))
            elif character in ["+", "-", "*", "/"]:
                if len(self.stack) < 2:
                    raise ValueError("Error: The expression is not valid")

                first_number = self.stack.pop()
                second_number = self.stack.pop()

                if character == "+":
                    one_number_result = second_number + first_number
                elif character == "-":
                    one_number_result = second_number - first_number
                elif character == "*":
                    one_number_result = second_number * first_number
                elif character == "/":
                    if first_number == 0:
                        raise ValueError("Error: Division by zero")
                    one_number_result = second_number / first_number

                self.stack.append(one_number_result)

            expression = expression[1:]

        if len(self.stack) != 1:
            raise ValueError("Error: The expression is not valie")

        return self.stack[0]
