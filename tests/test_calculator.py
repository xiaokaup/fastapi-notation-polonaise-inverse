from unittest import TestCase
from Calculator import Calculator


class TestCalculator(TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_get_expression_result_success(self):
        self.assertEqual(self.calculator.get_expression_result("5 1 2 + 4 * + 3 -"), 14)
        self.assertEqual(self.calculator.get_expression_result("1 2 +"), 3)
        self.assertEqual(self.calculator.get_expression_result("1 2 + 3 *"), 9)
        self.assertEqual(self.calculator.get_expression_result("1 2 + 3 * 4 /"), 2.25)
        self.assertEqual(
            self.calculator.get_expression_result("1 2 + 3 * 4 / 5 +"), 7.25
        )

    def test_get_expression_result_error_case_1_not_enough_number_for_operation(self):
        with self.assertRaises(ValueError) as e:
            self.calculator.get_expression_result("1 +")
            self.assertRaises(ValueError)
            self.assertEqual(
                str(e),
                "Error: There are not enough numbers to perform the operation",
            )

    def test_get_expression_result_error_case_2_division_by_zero(self):
        with self.assertRaises(ValueError) as e:
            self.calculator.get_expression_result("1 +")
            self.assertRaises(ValueError)
            self.assertEqual(
                str(e),
                "Error: Division by zero",
            )

    def test_get_expression_result_error_case_3_invalid_expression(self):
        # Test invalid expression
        with self.assertRaises(ValueError) as e:
            self.calculator.get_expression_result("1 +")
            self.assertRaises(ValueError)
            self.assertEqual(
                str(e),
                "Error: The expression is not valie",
            )

    def test_get_expression_result_error_case_4_invalid_character(self):
        # Test invalid character
        with self.assertRaises(ValueError) as e:
            self.calculator.get_expression_result("1 3 ~")
            self.assertRaises(ValueError)
            self.assertEqual(
                str(e),
                "Error: The character is not valid",
            )
