"""
A simple calculator module with basic arithmetic operations.
"""


class InvalidInputException(Exception):
    """Exception raised when input values are outside the valid range."""
    pass


class Calculator:
    """Calculator class providing basic arithmetic operations."""

    # Define allowed input range
    MIN_VALUE = -1000000
    MAX_VALUE = 1000000

    def _validate_inputs(self, *args):
        """Validate that all inputs are numbers and within allowed range.

        Raises:
            InvalidInputException: If any input is not a number or out of range
        """
        for v in args:
            if not isinstance(v, (int, float)):
                raise InvalidInputException("Inputs must be int or float")
            if v < self.MIN_VALUE or v > self.MAX_VALUE:
                raise InvalidInputException(f"Input {v} outside allowed range [{self.MIN_VALUE}, {self.MAX_VALUE}]")

    def add(self, a, b):
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate_inputs(a, b)
        return a + b

    def subtract(self, a, b):
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate_inputs(a, b)
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate_inputs(a, b)
        return a * b

    def divide(self, a, b):
        """Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
            ValueError: If b is zero
        """
        self._validate_inputs(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
