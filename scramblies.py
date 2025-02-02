def scramble(s1, s2):
    #return true if string one can be rearranged to match string 2
    #loop through letters of string 2
    from collections import Counter
    
    #count occurrences of each letter in s1 and s2
    count_s1 = Counter(s1)
    count_s2 = Counter(s2)
    
    #check if s1 has enough of each letter to match s2
    for letter in count_s2:
        if count_s2[letter] > count_s1.get(letter, 0):
            return False
    return True
    
scramble("otinocumwlruw", "woinolcwmm")