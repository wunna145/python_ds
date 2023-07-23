def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase = phrase.lower()
    result = {}
    for ltr in phrase:
        if ltr in 'aeiou':
            if ltr in result:
                result[ltr] += 1
            else: 
                result[ltr] = 1
    return result
        