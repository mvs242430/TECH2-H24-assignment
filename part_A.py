"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
import util
from math import sqrt, pow

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

   
    variance = util.mean_sqrt_loops(values=x) - pow(util.mean_loops(values=x), 2)
    result = sqrt(variance)
    return result
   



def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    
    util.validate_numbers(values=x)
 
    mean = sum(x)/len(x)
    mean_sqrt = sum(number ** 2 for number in x)/len(x)
    variance = mean_sqrt - pow(mean,2)
    result = sqrt(variance)
    return result


