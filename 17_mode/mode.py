def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    most_common_num = 0
    most_count = 0
    count = 0
    for num1 in nums:
        for num2 in nums:
            if num1 == num2:
                count += 1
        if count > most_count:
            most_count = count
            most_common_num = num1
        count = 0
    return most_common_num
            
