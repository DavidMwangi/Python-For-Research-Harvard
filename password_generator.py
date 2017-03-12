import random


def password(length):
    
    """
    
    This functions generates unique password of a specified length
    
    Input: Length of the password
    
    Output: Unique password of the specified length
    
    """

    pw = str()
    
    characters = 'abcdefghijklmnopqrstuvwxyz'
    
    upperchars = characters.upper()
    
    nums = "0123456789"
    
    characters = characters + upperchars + nums
    
    for i in range(length):
        
        pw += random.choice(characters)
        
    return pw