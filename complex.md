## Complex

Operations with complex numbers: +, -, *, /, modulus. Override defs __eq__ and __str__. Unit tests

```python
import unittest


class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def subtract(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def multiply(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)

    def divide(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        return Complex((self.real * other.real + self.imaginary * other.imaginary) / denominator,
                       (self.imaginary * other.real - self.real * other.imaginary) / denominator)

    def modulus(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real}{self.imaginary}i"
        else:
            return f"{self.real}+{self.imaginary}i"


class TestComplex(unittest.TestCase):

    def test_add(self):
        first = Complex(1, 2)
        second = Complex(3, 4)
        third = Complex(-1, -2)

        self.assertEqual(first.add(second), Complex(4, 6))
        self.assertEqual(second.add(third), Complex(2, 2))

    def test_subtract(self):
        first = Complex(1, 2)
        second = Complex(3, 4)
        third = Complex(-2, -2)

        self.assertEqual(first.subtract(second), Complex(-2, -2))
        self.assertEqual(second.subtract(third), Complex(5, 6))

    def test_multiply(self):
        first = Complex(1, 2)
        second = Complex(3, 4)
        third = Complex(-2, -2)

        self.assertEqual(first.multiply(second), Complex(-5, 10))
        self.assertEqual(second.multiply(third), Complex(2, -14))

    def test_divide(self):
        first = Complex(1, 2)
        second = Complex(3, 4)
        third = Complex(-2, -2)

        self.assertEqual(first.divide(second), Complex(0.44, 0.08))
        self.assertEqual(second.divide(third), Complex(-1.75, -0.25))

    def test_modulus(self):
        first = Complex(1, 2)
        second = Complex(3, 4)

        self.assertEqual(first.modulus(), 5 ** 0.5)
        self.assertEqual(second.modulus(), 5.0)


if __name__ == '__main__':
    unittest.main()
```