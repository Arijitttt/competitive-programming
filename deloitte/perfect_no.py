def perfect_no(num):
    """
    Checks if a given number is a perfect number or not.

    A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.

    Parameters
    ----------
    num : int
        The number to check.

    Yields
    ------
    bool
        True if the number is perfect, False otherwise.
    """
    s = 0
    for i in range(1,int(num/2)+1):
        if num%i == 0:
            s += i
    if s == num:
        return True
    else:
        return False
num = 28
if perfect_no(num):
    print("perfect no")
else:
    print("not")