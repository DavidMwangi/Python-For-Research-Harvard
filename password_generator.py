import random
from string import ascii_letters, digits

def password(length):
    
    """
    
    This functions generates unique password of a specified length
    
    Input: Length of the password
    
    Output: Unique password of the specified length
    
    """ 

    pw = str()
    
    alphabet = ascii_letters
    
    numerals = digits
    
    characters = alphabet + numerals
    
    for i in range(length):
        
        pw += random.choice(characters)
        
    return pw