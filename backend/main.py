from class_object.Calculator import Calculator


def test(expression: str) -> int:
    calculator = Calculator()
    return calculator.get_expression_result(expression)


if __name__ == "__main__":
    print(test("5 1 2 + 4 * + 3 -"))
    print(test("1 2 +"))
