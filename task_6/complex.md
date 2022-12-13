# Complex numbers
+ [Complex](#complex)
+ [Unit tests](#unit-tests)

## Complex
Operations with complex numbers: +, -, *, /, modulus, defs __eq__ and __str__. Unit tests

```python
class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        return Complex((self.real * other.real + self.imaginary * other.imaginary) / denominator,
                       (self.imaginary * other.real - self.real * other.imaginary) / denominator)

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other):
        return self.real != other.real or self.imaginary != other.imaginary

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real}{self.imaginary}i"
        else:
            return f"{self.real}+{self.imaginary}i"
```

## Unit tests
```python
import unittest
from complex import Complex


class TestComplex(unittest.TestCase):

    def test_add(self):
        first = Complex(1, 2)
        second = Complex(3, 4)
        third = Complex(-1, -2)

        self.assertEqual(first + second, Complex(4, 6))
        self.assertEqual(second + third, Complex(2, 2))

    def test_sub(self):
        first = Complex(1, 2)
        second = Complex(3, 4)
        third = Complex(-2, -2)

        self.assertEqual(first - second, Complex(-2, -2))
        self.assertEqual(second - third, Complex(5, 6))

    def test_mul(self):
        first = Complex(1, 2)
        second = Complex(3, 4)
        third = Complex(-2, -2)

        self.assertEqual(first * second, Complex(-5, 10))
        self.assertEqual(second * third, Complex(2, -14))

    def test_truediv(self):
        first = Complex(1, 2)
        second = Complex(3, 4)
        third = Complex(-2, -2)

        self.assertEqual(first / second, Complex(0.44, 0.08))
        self.assertEqual(second / third, Complex(-1.75, -0.25))

    def test_abs(self):
        first = Complex(1, 2)
        second = Complex(3, 4)

        self.assertEqual(abs(first), 5 ** 0.5)
        self.assertEqual(abs(second), 5.0)

    def test___eq__(self):
        first = Complex(1, 2)
        second = Complex(3, 4)
        third = Complex(1, 2)

        res_1 = first == second
        res_2 = first == third

        self.assertEqual(res_1, False)
        self.assertEqual(res_2, True)

    def test___ne__(self):
        first = Complex(1, 2)
        second = Complex(3, 4)
        third = Complex(1, 2)

        res_1 = first != second
        res_2 = first != third

        self.assertEqual(res_1, True)
        self.assertEqual(res_2, False)

    def test___str__(self):
        first = Complex(1, 2)
        second = Complex(3, -4)

        self.assertEqual(str(first), '1+2i')
        self.assertEqual(str(second), '3-4i')


if __name__ == '__main__':
    unittest.main()
```
