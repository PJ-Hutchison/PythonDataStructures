def same_frequency(coll):
    counts = {}

    for x in coll:
        counts[x] = counts.get(x, 0) + 1

    return counts
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    def same_frequency(num1, num2):
        return freq_counter(str(num1)) == freq_counter(str(num2))