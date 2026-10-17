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



if __name__ == "__main__":
    unittest.main()