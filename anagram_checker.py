def check_anagram(a, b):
    if a is None or b is None or len(a) != len(b):
        return "Not Anagram"
        
    return "Anagram" if sorted(a) == sorted(b) else "Not Anagram"
