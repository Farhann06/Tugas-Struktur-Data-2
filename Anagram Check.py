def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    count = {}
    
    for char in s1:
        count[char] = count.get(char, 0) + 1
        
    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
            
    return True

# Contoh
print(is_anagram("listen", "silent"))