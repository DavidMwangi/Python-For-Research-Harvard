def intersect(a,b):

    """
    
    This functions returns the intersect of two lists.
    
    Input: 2 lists
    
    Output: A list with items in both the input lists
    
    
    """

    result = [] #array to track intersect values

    for item in a: #iterate through all items in list a
        
        if item in b: #find for membership of items in a in list b
            
            result.append(item) #append items on both lists to the result list
            
    return result#return results to function caller 
    
    """
    
    Bug report: If two of the same value are in the first list and appear only
    
    once on the second list. The result list captures the two instances instead
    
    of one.
    
    """
    
    