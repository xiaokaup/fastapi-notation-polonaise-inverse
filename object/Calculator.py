class Calculator:
    def get_expression_result(self, expression: str) -> int:
        stack = []

        # clean space in expression string
        expression = "".join(expression.split(" "))
        # Loop through the expression without spaces
        while len(expression) > 0:
            character = expression[0]

            if character.isdigit():
                stack.append(int(character))
            elif character in ["+", "-", "*", "/"]:
                if len(stack) < 2:
                    raise ValueError(
                        "Error: There are not enough numbers to perform the operation"
                    )

                first_number = stack.pop()
                second_number = stack.pop()

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

                stack.append(one_number_result)
            else:
                raise ValueError("Error: The character is not valid")

            expression = expression[1:]

        if len(stack) != 1:
            raise ValueError("Error: The expression is not valid")

        return stack[0]
