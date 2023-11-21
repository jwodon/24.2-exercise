def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    lower_phrase = phrase.lower()
    vowels = set('aeiou')
    frequency = {}

    for word in lower_phrase:
        if word in vowels:
            frequency[word] = frequency.get(word, 0) + 1

    return frequency
            
