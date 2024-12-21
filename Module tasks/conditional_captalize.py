def preLetterCase(s, letter):
    index = s.find(letter)
    if index == -1:  
        return s.lower()  
    before = s[:index].lower()
    after = s[index:].upper()
    return before + after

print(preLetterCase("CAtCHa", "A"))  
print(preLetterCase("Preteen", "e"))  
print(preLetterCase("You've got this", "m"))  
print(preLetterCase("Keep trying", "K")) 
