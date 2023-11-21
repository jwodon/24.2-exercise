def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    str_num1, str_num2 = str(num1), str(num2)

    if len(str_num1) == len(str_num2):
        return False

    freq_dict1 = {}
    freq_dict2 = {}

    for num in str_num1:
        freq_dict1[num] = freq_dict1.get(num, 0) + 1 

    for num in str_num2:
        freq_dict2[num] = freq_dict2.get(num, 0) + 1 

    return freq_dict1 == freq_dict2