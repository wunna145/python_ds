def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    obj = {}
    for letter in phrase:
        if not letter in obj:
            obj[letter] = 1
        else:
            obj[letter] += 1
    return obj