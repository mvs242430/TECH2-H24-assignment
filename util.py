from numbers import Number
from _collections_abc import Sequence


def mean_loops(values):
    """
    Compute the mean of the list of number using loops.

    Parameters
    ----------
    values: Sequence of numbers for which mean would be computed

    Returns
    -------
    sd : float
        Mean of the list of numbers.

    Notes
    -----
    This function calls `validate_numbers` to check if the input is a valid sequence of numbers.
    """

    validate_numbers(values)

    sum = 0
    num_count = 0
    for number in values:
        sum += number
        num_count += 1
    return sum / num_count


def mean_sqrt_loops(values):
    """
    Compute the mean of squares of the list of numbers using loops.

    Parameters
    ----------
    values: Sequence of numbers for which mean squares would be computed

    Returns
    -------
    sd : float
        Mean squares of the list of numbers.

    Notes
    -----
    This function calls `validate_numbers` to check if the input is a valid sequence of numbers.
    """

    validate_numbers(values)

    sum = 0
    num_count = 0
    for number in values:
        sum += number**2
        num_count += 1
    return sum / num_count


def validate_numbers(values):
    """
    Validates that the input is not empty sequence containing only numeric elements.

    Parameters
    ----------
    values: Sequence of numbers to be validated
        The sequence can be of types such as list, tuple, range, numpy.ndarray, or
        pandas.Series. Strings are not considered valid sequences.

    Raises
    -------
    ValueError
        If input is not a sequence or is a string.
        If sequence is empty.
        If any element in a siquence is not a numerical type.

    """
    if not isinstance(values, Sequence) or isinstance(values, str):
        raise ValueError("Oh, looks like what I got is not a sequence of numbers")
    if not values:
        raise ValueError(
            "Found no numbers. Make sure you are not giving me an empty list"
        )
    if not all(isinstance(value, Number) for value in values):
        raise ValueError("I can work with a lists that contain only numbers")
