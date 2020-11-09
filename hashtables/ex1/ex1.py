def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    hash = dict()
    
    if length <= 1:
        return None

    for i in range(length):
        weight = weights[i]

        if weight in hash:
            value = hash[weight]
            return[i, value]
        
        diff = limit - weight
        hash[diff] = i
    
    return None
