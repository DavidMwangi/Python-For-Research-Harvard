from string import ascii_letters

#sentence = 'Jim quickly realized that the beautiful gowns are expensive'

# Create your function here!

def counter(sentence):

    alphabet = ascii_letters
    
    count_letters = {}
    #write your code here!
    
    count = 0
    
    for letter in sentence:
        
        if letter in alphabet:
            
            if letter in count_letters:
                
                count_letters[letter] += 1
    
            else:
                
                count += 1
                count_letters[letter] = count
                count = 0
            
    return count_letters



#print(counter(sentence))