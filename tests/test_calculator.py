"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        # Arrange
        calc = Calculator()
        a = 6
        b = 3
        expected = 2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected


class TestInvalidInput:
    """Tests for invalid inputs and boundary checks."""

    def test_input_above_max_raises(self):
        """Inputs greater than MAX_VALUE should raise InvalidInputException."""
        # Arrange
        calc = Calculator()

        # Act / Assert
        with pytest.raises(InvalidInputException):
            calc.add(calc.MAX_VALUE + 1, 0)

    def test_input_below_min_raises(self):
        """Inputs less than MIN_VALUE should raise InvalidInputException."""
        # Arrange
        calc = Calculator()

        # Act / Assert
        with pytest.raises(InvalidInputException):
            calc.subtract(calc.MIN_VALUE - 1, 0)

    def test_non_numeric_raises(self):
        """Non-numeric inputs should raise InvalidInputException."""
        # Arrange
        calc = Calculator()

        # Act / Assert
        with pytest.raises(InvalidInputException):
            calc.multiply("not-a-number", 2)

    def test_boundary_values_allowed(self):
        """Operations using MIN_VALUE and MAX_VALUE should be allowed."""
        # Arrange
        calc = Calculator()
        a = calc.MAX_VALUE
        b = calc.MIN_VALUE

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(a + b)

    def test_divide_by_zero_raises_value_error(self):
        """Dividing by zero should raise ValueError (not InvalidInputException)."""
        # Arrange
        calc = Calculator()

        # Act / Assert
        with pytest.raises(ValueError):
            calc.divide(1, 0)


class TestBoundaryAndMutation:
    """Additional boundary and mutation-resistant tests to improve coverage."""

    @pytest.mark.parametrize(
        "a,b",
        [
            (1, 2),
            (2.5, 3.5),
            (0, 0),
            (Calculator.MAX_VALUE, -1),
        ],
    )
    def test_add_commutativity(self, a, b):
        """Addition should be commutative for valid numeric inputs."""
        calc = Calculator()
        assert calc.add(a, b) == calc.add(b, a)

    @pytest.mark.parametrize(
        "a,b",
        [
            (1, 2),
            (2.5, 3.0),
            (0, 5),
        ],
    )
    def test_multiply_commutativity(self, a, b):
        """Multiplication should be commutative for valid numeric inputs."""
        calc = Calculator()
        assert calc.multiply(a, b) == calc.multiply(b, a)

    def test_input_float_above_max_raises(self):
        """Floating point inputs slightly above MAX_VALUE should raise."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(calc.MAX_VALUE + 0.1, 0)

    def test_input_float_below_min_raises(self):
        """Floating point inputs slightly below MIN_VALUE should raise."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(calc.MIN_VALUE - 0.1, 0)

    def test_multiply_by_zero(self):
        """Multiplying by zero should return zero and be allowed."""
        calc = Calculator()
        assert calc.multiply(0, calc.MAX_VALUE) == 0
        assert calc.multiply(calc.MIN_VALUE, 0) == 0

    def test_result_exceeds_max_allowed_when_inputs_valid(self):
        """If inputs are within allowed range, large results are currently allowed.
        This checks mutation that would incorrectly enforce result bounds instead of input bounds.
        """
        calc = Calculator()
        a = 800
        b = 2
        # inputs are within [-1000000, 1000000] so operation should succeed even if result > MAX_VALUE
        assert calc.multiply(a, b) == 1600

    def test_subtract_result_below_min_allowed_when_inputs_valid(self):
        """Similar to the above: inputs valid but result below MIN should be produced."""
        calc = Calculator()
        a = -800
        b = 500
        assert calc.subtract(a, b) == -1300

    @pytest.mark.parametrize(
        "a,b,op,expected",
        [
            (5, 3, "add", 8),
            (5, 3, "subtract", 2),
            (5, 3, "multiply", 15),
            (6, 3, "divide", 2),
            (2.5, 0.5, "divide", 5.0),
        ],
    )
    def test_parametrized_operations(self, a, b, op, expected):
        """Parametrized smoke tests for basic operations to increase coverage."""
        calc = Calculator()
        if op == "add":
            assert calc.add(a, b) == pytest.approx(expected)
        elif op == "subtract":
            assert calc.subtract(a, b) == pytest.approx(expected)
        elif op == "multiply":
            assert calc.multiply(a, b) == pytest.approx(expected)
        elif op == "divide":
            assert calc.divide(a, b) == pytest.approx(expected)


class TestMutationHardening:
    """Targeted tests to kill survived mutants reported by mutmut."""

    def test_bool_inputs_treated_as_int(self):
        """bool inputs should be accepted and behave like ints (True==1, False==0)."""
        calc = Calculator()
        assert calc.add(True, 2) == 3
        assert calc.add(False, 2) == 2
        assert calc.multiply(True, 5) == 5
        assert calc.multiply(False, 5) == 0
        assert calc.subtract(True, 1) == 0
        assert calc.divide(True, 1) == 1

    def test_reject_complex_type(self):
        """Complex numbers are not allowed by validation and should raise InvalidInputException."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(1 + 2j, 1)

    def test_reject_string_and_list_types(self):
        """Strings and lists should be rejected by the validator."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add("1", 2)
        with pytest.raises(InvalidInputException):
            calc.multiply([1, 2], 3)

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (5, 3, 8),
            (5, -3, 2),
            (-5, 3, -2),
            (1.5, 2.25, 3.75),
        ],
    )
    def test_add_varied_inputs(self, a, b, expected):
        """More addition cases to catch operator-replacement mutations."""
        calc = Calculator()
        assert calc.add(a, b) == pytest.approx(expected)

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (5, 3, 2),
            (3, 5, -2),
            (2.5, 1.25, 1.25),
        ],
    )
    def test_subtract_varied_inputs(self, a, b, expected):
        """More subtraction cases to catch mutations that swap operators."""
        calc = Calculator()
        assert calc.subtract(a, b) == pytest.approx(expected)

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (5, 3, 15),
            (-5, 3, -15),
            (2.5, 0.4, 1.0),
        ],
    )
    def test_multiply_varied_inputs(self, a, b, expected):
        """More multiplication cases to catch operator-replacement mutations."""
        calc = Calculator()
        assert calc.multiply(a, b) == pytest.approx(expected)

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (7, 2, 3.5),
            (5, 2, 2.5),
            (2.5, 0.5, 5.0),
        ],
    )
    def test_divide_varied_inputs(self, a, b, expected):
        """More division cases including non-integer quotients to catch mutations."""
        calc = Calculator()
        assert calc.divide(a, b) == pytest.approx(expected)


class TestMutationKillSpecific:
    """Targeted tests to kill specific survived mutants reported by mutmut."""

    def test_non_numeric_message_and_second_arg_checked_add(self):
        calc = Calculator()
        # first arg non-numeric
        with pytest.raises(InvalidInputException) as e1:
            calc.add("x", 1)
        assert str(e1.value) == "Inputs must be int or float"

        # second arg non-numeric (catches mutants that validate only first arg)
        with pytest.raises(InvalidInputException) as e2:
            calc.add(1, "y")
        assert str(e2.value) == "Inputs must be int or float"

    def test_non_numeric_message_and_second_arg_checked_subtract(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException) as e1:
            calc.subtract("x", 1)
        assert str(e1.value) == "Inputs must be int or float"
        with pytest.raises(InvalidInputException) as e2:
            calc.subtract(1, "y")
        assert str(e2.value) == "Inputs must be int or float"

    def test_non_numeric_message_and_second_arg_checked_multiply(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException) as e1:
            calc.multiply("x", 1)
        assert str(e1.value) == "Inputs must be int or float"
        with pytest.raises(InvalidInputException) as e2:
            calc.multiply(1, "y")
        assert str(e2.value) == "Inputs must be int or float"

    def test_divide_validates_both_args_and_zero_message(self):
        calc = Calculator()
        # non-numeric numerator
        with pytest.raises(InvalidInputException) as e1:
            calc.divide("x", 1)
        assert str(e1.value) == "Inputs must be int or float"
        # non-numeric denominator
        with pytest.raises(InvalidInputException) as e2:
            calc.divide(1, "y")
        assert str(e2.value) == "Inputs must be int or float"
        # divide by zero message must be exact
        with pytest.raises(ValueError) as ei:
            calc.divide(1, 0)
        assert str(ei.value) == "Cannot divide by zero"

    def test_range_message_exact(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException) as e1:
            calc.add(calc.MAX_VALUE + 1, 0)
        assert "outside allowed range" in str(e1.value)
        with pytest.raises(InvalidInputException) as e2:
            calc.add(calc.MIN_VALUE - 1, 0)
        assert "outside allowed range" in str(e2.value)
