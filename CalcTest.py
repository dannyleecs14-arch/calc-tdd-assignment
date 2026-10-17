import unittest

from Calc import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)

    # 1. 一般正整數減法
    def test_subtract_positive(self):
        calc = Calculator()
        result = calc.subtract(5, 1)
        self.assertEqual(result, 4)

    # 2. 減去零
    def test_subtract_zero(self):
        calc = Calculator()
        result = calc.subtract(5, 0)
        self.assertEqual(result, 5)

    # 3. 相同數字相減
    def test_subtract_same_number(self):
        calc = Calculator()
        result = calc.subtract(5, 5)
        self.assertEqual(result, 0)

    # 4. 結果為負數
    def test_subtract_negative_result(self):
        calc = Calculator()
        result = calc.subtract(2, 5)
        self.assertEqual(result, -3)

    # 5. 負數減正數
    def test_subtract_negative_positive(self):
        calc = Calculator()
        result = calc.subtract(-5, 2)
        self.assertEqual(result, -7)

    # 6. 正數減負數
    def test_subtract_positive_negative(self):
        calc = Calculator()
        result = calc.subtract(5, -2)
        self.assertEqual(result, 7)

    # 7. 負數減負數
    def test_subtract_two_negatives(self):
        calc = Calculator()
        result = calc.subtract(-5, -2)
        self.assertEqual(result, -3)

    # 8. 零減正數
    def test_subtract_from_zero(self):
        calc = Calculator()
        result = calc.subtract(0, 5)
        self.assertEqual(result, -5)

    # 9. 零減零
    def test_subtract_zero_zero(self):
        calc = Calculator()
        result = calc.subtract(0, 0)
        self.assertEqual(result, 0)

    # 10. 浮點數減法
    def test_subtract_float(self):
        calc = Calculator()
        result = calc.subtract(5.5, 2.0)
        self.assertEqual(result, 3.5)

    # 11. 浮點數負結果
    def test_subtract_float_negative(self):
        calc = Calculator()
        result = calc.subtract(2.5, 5.0)
        self.assertEqual(result, -2.5)

    # 12. 較大整數
    def test_subtract_large_number(self):
        calc = Calculator()
        result = calc.subtract(1000000, 999999)
        self.assertEqual(result, 1)


    # 1. 一般正整數乘法
    def test_multiply_positive(self):
        calc = Calculator()
        result = calc.multiply(5, 2)
        self.assertEqual(result, 10)

    # 2. 正數乘以零
    def test_multiply_by_zero(self):
        calc = Calculator()
        result = calc.multiply(5, 0)
        self.assertEqual(result, 0)

    # 3. 零乘以正數
    def test_multiply_zero_first(self):
        calc = Calculator()
        result = calc.multiply(0, 5)
        self.assertEqual(result, 0)

    # 4. 零乘以零
    def test_multiply_zero_zero(self):
        calc = Calculator()
        result = calc.multiply(0, 0)
        self.assertEqual(result, 0)

    # 5. 正數乘以一
    def test_multiply_by_one(self):
        calc = Calculator()
        result = calc.multiply(5, 1)
        self.assertEqual(result, 5)

    # 6. 正數乘負數
    def test_multiply_positive_negative(self):
        calc = Calculator()
        result = calc.multiply(5, -2)
        self.assertEqual(result, -10)

    # 7. 負數乘正數
    def test_multiply_negative_positive(self):
        calc = Calculator()
        result = calc.multiply(-5, 2)
        self.assertEqual(result, -10)

    # 8. 負數乘負數
    def test_multiply_two_negatives(self):
        calc = Calculator()
        result = calc.multiply(-5, -2)
        self.assertEqual(result, 10)

    # 9. 交換乘數順序
    def test_multiply_reversed(self):
        calc = Calculator()
        result = calc.multiply(2, 5)
        self.assertEqual(result, 10)

    # 10. 小數乘以整數
    def test_multiply_float(self):
        calc = Calculator()
        result = calc.multiply(2.5, 2)
        self.assertEqual(result, 5.0)

    # 11. 小數乘以小數
    def test_multiply_two_floats(self):
        calc = Calculator()
        result = calc.multiply(1.5, 0.5)
        self.assertEqual(result, 0.75)

    # 12. 較大整數乘法
    def test_multiply_large_number(self):
        calc = Calculator()
        result = calc.multiply(1000000, 1000)
        self.assertEqual(result, 1000000000)


    # 1. 正整數整除
    def test_divide_positive(self):
        calc = Calculator()
        self.assertEqual(calc.divide(10, 2), 5.0)

    # 2. 除不盡，產生小數
    def test_divide_fraction(self):
        calc = Calculator()
        self.assertEqual(calc.divide(7, 2), 3.5)

    # 3. 小於一的結果
    def test_divide_less_than_one(self):
        calc = Calculator()
        self.assertEqual(calc.divide(1, 4), 0.25)

    # 4. 零除以非零數
    def test_divide_zero_numerator(self):
        calc = Calculator()
        self.assertEqual(calc.divide(0, 5), 0.0)

    # 5. 負數除以正數
    def test_divide_negative_positive(self):
        calc = Calculator()
        self.assertEqual(calc.divide(-10, 2), -5.0)

    # 6. 正數除以負數
    def test_divide_positive_negative(self):
        calc = Calculator()
        self.assertEqual(calc.divide(10, -2), -5.0)

    # 7. 負數除以負數
    def test_divide_two_negatives(self):
        calc = Calculator()
        self.assertEqual(calc.divide(-10, -2), 5.0)

    # 8. 除以一
    def test_divide_by_one(self):
        calc = Calculator()
        self.assertEqual(calc.divide(5, 1), 5.0)

    # 9. 浮點數除法
    def test_divide_floats(self):
        calc = Calculator()
        self.assertEqual(calc.divide(2.5, 0.5), 5.0)

    # 10. 循環小數
    def test_divide_repeating_decimal(self):
        calc = Calculator()
        self.assertAlmostEqual(
            calc.divide(1, 3), 1 / 3
        )

    # 11. 大數除法
    def test_divide_large_number(self):
        calc = Calculator()
        self.assertEqual(
            calc.divide(1000000, 1000), 1000.0
        )

    # 12. 除以零應拋出例外
    def test_divide_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.divide(5, 0)

    def test_modulo_positive(self):
        calc = Calculator()
        self.assertEqual(calc.modulo(10, 3), 1)

    def test_modulo_negative_dividend(self):
        calc = Calculator()
        self.assertEqual(calc.modulo(-10, 3), 2)

    def test_modulo_negative_divisor(self):
        calc = Calculator()
        self.assertEqual(calc.modulo(10, -3), -2)

    def test_modulo_two_negatives(self):
        calc = Calculator()
        self.assertEqual(calc.modulo(-10, -3), -1)

    def test_modulo_zero_dividend(self):
        calc = Calculator()
        self.assertEqual(calc.modulo(0, 5), 0)

    def test_modulo_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.modulo(5, 0)

    def test_modulo_zero_negative_divisor(self):
        calc = Calculator()
        self.assertEqual(calc.modulo(0, -5), 0)

    def test_modulo_zero_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.modulo(0, 0)

    def test_modulo_floats(self):
        calc = Calculator()
        self.assertEqual(calc.modulo(5.5, 2.0), 1.5)

    def test_power_positive_integer_exponent(self):
        calc = Calculator()
        self.assertEqual(calc.power(2, 3), 8)

    def test_power_zero_exponent(self):
        calc = Calculator()
        self.assertEqual(calc.power(5, 0), 1)

    def test_power_negative_base_odd_exponent(self):
        calc = Calculator()
        self.assertEqual(calc.power(-2, 3), -8)

    def test_power_negative_base_even_exponent(self):
        calc = Calculator()
        self.assertEqual(calc.power(-2, 4), 16)

    def test_power_negative_exponent(self):
        calc = Calculator()
        self.assertEqual(calc.power(2, -3), 0.125)

    def test_power_zero_to_zero(self):
        calc = Calculator()
        self.assertEqual(calc.power(0, 0), 1)

    def test_power_zero_to_negative(self):
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.power(0, -1)

    def test_power_fractional_exponent(self):
        calc = Calculator()
        self.assertAlmostEqual(calc.power(9, 0.5), 3.0)

    def test_power_zero_base_positive_exponent(self):
        calc = Calculator()
        self.assertEqual(calc.power(0, 3), 0)

    def test_power_exponent_one(self):
        calc = Calculator()
        self.assertEqual(calc.power(2, 1), 2)


if __name__ == "__main__":
    unittest.main()
